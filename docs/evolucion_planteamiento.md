# Evolución del planteamiento, decisiones de diseño y avances

Registro de cómo ha ido cambiando el planteamiento del problema y de las decisiones del grupo, con su motivo y las opciones descartadas. Sirve de base para los apartados de Métodos y de Discusión de la memoria técnica. Se amplía tras cada reunión o cambio importante.

## 1. Punto de partida (hasta el 7 de noviembre)

- **Entorno común:** Python 3.12 con uv, `requirements.txt` exportado desde `uv.lock` y una única semilla (42) en `src/utils/constantes.py` para que todos los experimentos sean comparables.
- **EDA individual:** cada miembro exploró los datos en su notebook (`eda_enzo`, `eda_pablo` y `eda_rodrigo`): distribuciones, desbalanceo (≈ 50/30/20 % en bajo, moderado y alto), nulos, valores imposibles y una lectura clínica de las variables.
- **Problemáticas detectadas:** valores nulos en varias numéricas, valores imposibles (edades de menores, IMC < 10, alcohol negativo, más de 7 días de ejercicio por semana, HDL y triglicéridos negativos, presiones incoherentes),valores repetidos sospechosos que esconden nulos, colas largas con valores extremos, categóricas sin codificar y clases desbalanceadas. La clase de riesgo moderado se solapa con las otras dos; bajo frente a alto se separa mejor.

## 2. Reunión del 8 de noviembre: del EDA al modelado

### Reparto de modelos

| Persona | Modelos |
|---|---|
| Pablo | Regresión logística, Naive Bayes y gradient boosting |
| Enzo | LDA, SVM y un ensemble de stacking o voting |
| Rodrigo | Árbol de decisión, k vecinos y random forest |

Así se cubren los mínimos del enunciado: modelos base de sobra y tres ensembles (gradient boosting, random forest y stacking/voting).

### Diseño experimental común

| Decisión | Motivo |
|---|---|
| Partición 80/20 estratificada y semilla 42, fijadas en `constantes.py` | Mismo train y test para todos; el test se usa una sola vez, al final |
| `StratifiedKFold` de 5 folds, con la opción de probar 10 | Mantener la proporción de clases en cada fold; con pocos datos, más folds pueden estabilizar la estimación |
| Métricas: F1, precisión y recall en macro, y recall y precisión de riesgo alto | En macro las tres clases pesan igual, aunque la de alto sea la minoritaria |
| Métrica crítica: **recall de riesgo alto** | Clínicamente, lo grave es no detectar a un paciente de riesgo alto (falso negativo) |
| `GridSearchCV` optimiza el F1 macro; si dos modelos empatan, gana el de más recall de alto | Optimizar solo el recall de alto premiaría al modelo que predice «alto» a todos |
| Matriz de confusión del modelo final y comparación train/validación (media ± desviación) en todos | Ver dónde se equivoca el modelo y detectar sobreajuste |

### Preprocesamiento

**Limpieza** (sección 1.9 del notebook de Rodrigo, con dos cambios de Enzo):

- Edad de los menores de 18 a nulo, en vez de eliminar a esos pacientes: se conservan los 2.254.
- IMC a nulo solo si es menor de 10.
- HDL y triglicéridos negativos a nulo: son valores imposibles.
- Presión sistólica menor o igual que la diastólica: las dos a nulo, porque no se sabe cuál de las dos está mal.
- Valores repetidos sospechosos a nulo: 449 valores en colesterol total, triglicéridos, presión sistólica y ácido úrico. Son un mismo valor exacto repetido muchas veces, que el EDA de Rodrigo identificó como nulos camuflados.
- Alcohol negativo recortado a 0 y ejercicio de más de 7 días recortado a 7. Pasarlos a nulo y luego imputar con la mediana borraría la información de que beben poco o hacen mucho ejercicio.
- No se eliminan outliers con umbrales clínicos: los valores extremos parecen reales y algunos se asocian a más riesgo alto.

**Codificación:**

- `nivel_actividad`: ordinal de 0 (sedentario) a 3 (muy activo), porque tiene orden.
- `tipo_alimentacion`: one-hot, quitando la dieta mediterránea como categoría de referencia.
- `antecedentes_familiares_tipo`: dos binarias (materno y paterno). «Ambos» activa las dos y «ninguno», ninguna.

**Dentro del `Pipeline`, ajustado solo con el train de cada fold:** imputación con la mediana → `RobustScaler` en las numéricas (SMOTENC mide distancias y la escala robusta no se deforma con los extremos) → `SMOTENC` para el desbalanceo (el SMOTE que respeta las variables categóricas) → modelo.

**Desbalanceo:** se compara sin balancear, `class_weight` y SMOTENC, y se elige según los resultados de validación.

### Opciones descartadas y por qué

| Opción | Motivo del descarte |
|---|---|
| Exportar varios CSV ya imputados o con SMOTE aplicado | Imputar o remuestrear antes de partir filtra información de validación y test al entrenamiento (*data leakage*). Se sustituyó por un único `data/datos.csv` limpio y codificado, sin imputar, y todo lo que aprende de los datos va en el pipeline |
| Imputar con la mediana sobre todo el dataset en el EDA | Misma fuga de datos; se retiró del notebook común |
| Eliminar a los menores de edad | Se perdían pacientes; basta con anular el dato erróneo |
| Pasar a nulo el alcohol negativo y el exceso de ejercicio | La imputación cambiaría el sentido del dato (ver arriba) |
| Umbrales clínicos para recortar outliers | Los extremos parecen reales y aportan señal de riesgo alto |
| Transformación logarítmica y PCA (ideas del EDA de Enzo) | No se adoptan por ahora. El logaritmo corrige la asimetría de las colas largas (no la escala, de la que ya se encarga el `RobustScaler`): a los árboles no les cambia nada y en los modelos lineales no lo hemos probado. PCA resta interpretabilidad. Quedan abiertas como mejora |

### Avances tras la reunión

- `data/datos.csv`: datos limpios y codificados, sin imputar.
- `src/utils/modelado.py`: código común (`cargar_datos`, `validador`, `metricas`, `crear_pipeline` con las tres opciones de balanceo, `crear_busqueda` y `guardar_resultados`, que guarda train y validación con media ± desviación y la nota de cada fold).
- Cada miembro trabaja sus modelos en su rama y su notebook (`modelos_<nombre>.ipynb`): primero con hiperparámetros por defecto y después con ajuste.

## 3. Cuestiones abiertas

- **`class_weight` no existe en todos los modelos** (Naive Bayes, `GradientBoostingClassifier`, LDA y k-NN). Hay que decidir la alternativa (por ejemplo, `HistGradientBoostingClassifier` o los `priors` de Naive Bayes) o justificar que en esos modelos se compara solo «sin balancear frente a SMOTENC».
- **Que la comparación decida el balanceo:** el acta habla de comparar «para justificar SMOTENC», pero en una exploración previa `class_weight` subió el recall de alto sin bajar el F1 macro.
- **Modelos con nulos en crudo:** el árbol y el random forest admiten `NaN`, pero el pipeline común siempre imputa. Si se quiere esa comparación, hace falta una opción sin imputar.
- **Modelo de referencia:** falta un clasificador trivial (clase mayoritaria) como suelo de comparación.
- **5 o 10 folds:** pendiente de comprobar si 10 folds reducen la variabilidad.
