"""Código común del grupo para el preprocesamiento y el modelado."""
from pathlib import Path

import pandas as pd
from imblearn.over_sampling import SMOTENC
from imblearn.pipeline import Pipeline   # como el de sklearn, pero admite SMOTENC como paso
from sklearn.base import clone
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import (ConfusionMatrixDisplay, classification_report, make_scorer,
                             precision_score, recall_score)
from sklearn.model_selection import GridSearchCV, StratifiedKFold, train_test_split
from sklearn.preprocessing import RobustScaler

from . import constantes as cte

# datos limpios y codificados, sin imputar (los genera la sección 2.3 del EDA)
RUTA_DATOS = Path(__file__).resolve().parents[2] / "data" / "datos.csv"
# carpeta donde cada uno guarda los resultados de sus modelos para juntarlos al final
RUTA_RESULTADOS = Path(__file__).resolve().parents[2] / "resultados"


# 1. Datos y partición
def cargar_datos():
    """Lee los datos y hace la partición 80/20 estratificada, igual para todos."""
    datos = pd.read_csv(RUTA_DATOS)
    X = datos.drop(columns=cte.objetivo)
    y = datos[cte.objetivo]
    # stratify=y mantiene la proporción 50/30/20 de las clases en train y en test
    return train_test_split(X, y, test_size=cte.test_size, stratify=y, random_state=cte.semilla)


# 2. Validación y métricas
# folds estratificados y barajados con la semilla: todos validamos con los mismos pacientes
validador = StratifiedKFold(n_splits=cte.n_folds, shuffle=True, random_state=cte.semilla)

# en macro las 3 clases pesan igual, así que un fallo en riesgo alto baja la media
metricas = {
    "f1_macro": "f1_macro",
    "precision_macro": "precision_macro",
    "recall_macro": "recall_macro",
    # labels=[2] calcula la métrica solo para la clase de riesgo alto
    "recall_alto": make_scorer(recall_score, labels=[2], average="macro"),
    "precision_alto": make_scorer(precision_score, labels=[2], average="macro", zero_division=0),
}

# elegimos con F1 macro: con recall_alto ganaría el modelo que dice «riesgo alto» a todos
metrica = "f1_macro"


# 3. Pipeline: todo lo que aprende de los datos se ajusta solo con el train de cada fold
# columnas binarias o categóricas ya codificadas: no se escalan y SMOTENC las trata como categorías
categoricas = [
    "fumador_actual", "hipertension_previa", "diabetes_mellitus",
    "tratamiento_estatinas", "uso_antihipertensivos",
    "nivel_actividad",
    "dieta_baja_en_carbohidratos", "dieta_occidental", "dieta_vegetariana",
    "antecedentes_familiares_paterno", "antecedentes_familiares_materno",
]


# el resto de columnas son numéricas continuas: son las únicas con nulos y las únicas que se escalan
numericas = [
    "edad", "presion_sistolica", "presion_diastolica", "colesterol_total", "colesterol_hdl",
    "colesterol_ldl", "trigliceridos", "glucosa_ayunas", "indice_masa_corporal",
    "frecuencia_cardiaca_reposo", "horas_sueno_diarias", "consumo_alcohol_semanal",
    "anos_fumador", "proteina_c_reactiva", "acido_urico", "clearance_creatinina",
    "frecuencia_ejercicio_semanal", "perimetro_cintura", "hemoglobina_glicosilada",
]


def crear_pipeline(modelo, balanceo="smotenc"):
    """Pipeline imputar -> escalar -> balancear -> modelo; balanceo: "smotenc", "class_weight" o None."""
    # clone devuelve una copia sin entrenar: así no modificamos el modelo que nos pasan
    modelo = clone(modelo)

    # numéricas: mediana (robusta a las colas largas) y RobustScaler (usa mediana e IQR,
    # así los valores extremos que hemos dejado no deforman la escala)
    tratamiento_numericas = Pipeline([
        ("imputar", SimpleImputer(strategy="median")),
        ("escalar", RobustScaler()),
    ])
    # categóricas: no tienen nulos y ya están codificadas como 0/1 (o 0-3), se dejan tal cual
    preprocesado = ColumnTransformer([
        ("num", tratamiento_numericas, numericas),
        ("cat", "passthrough", categoricas),
    ])

    pasos = [("preprocesado", preprocesado)]

    if balanceo == "smotenc":
        # tras el ColumnTransformer las columnas salen en orden: primero numéricas, luego categóricas,
        # así que las categóricas ocupan las posiciones len(numericas) ... final
        posiciones_cat = list(range(len(numericas), len(numericas) + len(categoricas)))
        # va después de imputar (SMOTENC no admite nulos) y de escalar (usa distancias entre pacientes)
        pasos.append(("balanceo", SMOTENC(categorical_features=posiciones_cat,
                                          random_state=cte.semilla)))
    elif balanceo == "class_weight":
        # no crea pacientes: da más peso en el entrenamiento a los errores en las clases pequeñas
        if "class_weight" not in modelo.get_params():
            raise ValueError(f"{type(modelo).__name__} no admite class_weight; usa 'smotenc' o None")
        modelo.set_params(class_weight="balanced")
    elif balanceo is not None:
        raise ValueError("balanceo debe ser 'smotenc', 'class_weight' o None")

    pasos.append(("modelo", modelo))
    # el Pipeline de imblearn aplica SMOTENC solo al entrenar (en cada fold de train),
    # nunca al validar ni al predecir: la validación se hace con pacientes reales
    return Pipeline(pasos)


# 4. Ajuste de hiperparámetros y resultados
def crear_busqueda(pipeline, param_grid):
    """GridSearchCV común; los hiperparámetros llevan el prefijo "modelo__" (p. ej. "modelo__max_depth")."""
    return GridSearchCV(pipeline, param_grid, scoring=metricas, refit=metrica,
                        cv=validador, return_train_score=True, n_jobs=-1)


def tabla_resultados(busqueda, nombre):
    """Fila con media ± desviación en train y validación ("test" en cv_results_ es el fold de validación)."""
    r = busqueda.cv_results_
    i = busqueda.best_index_   # posición de la mejor combinación (la elegida con `metrica`)

    fila = {}
    for m in metricas:
        fila[f"{m}_train"] = r[f"mean_train_{m}"][i]
        fila[f"{m}_train_std"] = r[f"std_train_{m}"][i]
        fila[f"{m}_val"] = r[f"mean_test_{m}"][i]
        fila[f"{m}_val_std"] = r[f"std_test_{m}"][i]
    # sobreajuste: cuánto peor va en validación que en train con la métrica de selección
    fila["diferencia_train_val"] = fila[f"{metrica}_train"] - fila[f"{metrica}_val"]
    fila["mejores_parametros"] = str(busqueda.best_params_)

    # una fila por modelo: luego pd.concat junta las de todo el grupo en una sola tabla
    return pd.DataFrame([fila], index=pd.Index([nombre], name="modelo"))


def guardar_resultados(busqueda, nombre):
    """Guarda la tabla y la nota de cada fold en resultados/ para juntar luego los modelos de todo el grupo."""
    RUTA_RESULTADOS.mkdir(exist_ok=True)
    tabla_resultados(busqueda, nombre).to_csv(RUTA_RESULTADOS / f"{nombre}.csv")
    # nota de la mejor combinación en cada fold (la necesita el test estadístico opcional)
    r, i = busqueda.cv_results_, busqueda.best_index_
    folds = pd.DataFrame({m: [r[f"split{k}_test_{m}"][i] for k in range(cte.n_folds)] for m in metricas})
    folds.index.name = "fold"
    folds.to_csv(RUTA_RESULTADOS / f"{nombre}_folds.csv")


# 5. Evaluación final
def evaluar_test(modelo, X_test, y_test):
    """Evaluación en test: solo una vez, con el modelo ya elegido."""
    nombres = ["bajo", "moderado", "alto"]
    y_pred = modelo.predict(X_test)
    print(classification_report(y_test, y_pred, target_names=nombres, digits=3))
    ConfusionMatrixDisplay.from_predictions(y_test, y_pred, display_labels=nombres)
