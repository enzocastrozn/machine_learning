# Registro de uso de IA · Pablo

Cómo funciona este registro: [docs/iaGUIA_REGISTRO_IA.md](GUIA_REGISTRO_IA.md).

## Herramientas empleadas

| Herramienta | Modelo | Entorno |
|---|---|---|---|
| Claude Code | claude-opus-5-5 | Extensión de VS Code en Windows 11 |

## Prompts

## 2026-11-01 · Claude Code

**Prompt literal**

````text
Échale un vistazo a los documentos de la entrega de la práctica 1 de machine learning: @practica1/PR_CTICA_1-_Instrucciones.pdf  y @practica1/Practica_1_Machine_Learning_Cardiovascular.pdf  para que conozcas los requisitos del proyecto el repositorio de trabajo está en  \practica\practica1\machine_learning y ahora tenemos un poco de lío entre lo que está en main y lo que estaba en mi rama. Unos tienen python 3.14 y otros han hecho la instalación de python 3.12 y me gustaría hacer una guía común tanto si se trabaja en Windows o en Linux / WSL. También una guía específica de para que los profesores se puedan instalar el entorno tanto si tienen como si no tienen uv. Échale un vistazo a mis apuntes en C:\Users\pablo\Documents\Pablo's Wiki\MasterIA> en los que tengo mis resúmenes de clase y una guía de uso de uv para que intentemos unificarlo todo. Ya tengo yo modificaciones hechas en @practica1/machine_learning/README.md  pero me gustaría que le de dieras buen formato y estructura y que además modificases el resto de archivos como @practica1/machine_learning/uv.lock , @practica1/machine_learning/.python-version  y @practica1/machine_learning/pyproject.toml . Yo creo que la opción de un python 3.12 para todos es lo más interesante, porque es una versión bastante contrastada. Incluye una sección en la que mis compañeros puedan entender como sincronizarse 

También quiero generar un sistema de registro de prompts de IA individualizado para ir registrándolos de forma automatizada tal y como pide la profesora en sus requisitos que yo he creado en @practica1/machine_learning/docs/ia/registro_ia_pablo.md  , que creo que lo podemos conseguir con un un AGENTS.md genérico para todos. Ayúdame con ello. Y también que se entienda el propósito del trabajo. No se si deberíamos añadir también las instrucciones de la práctica en el repo para trabajar con un buen contexto si se quiere. No se si pegando el PDF directamente o haciendole un markitdown. Sugiéreme y pregúntame en el camino y lo vamos decidiendo.
````

**Respuestas literales a las preguntas del agente**

````text
Enunciado: Solo Markdown (Recommended)

Captura: Tienes que tener en cuenta que no todos tienen Claude Code, 2 sí y uno tiene Github Copilot, así que lo tienes que hacer genérico para que nos funcione a todos. ¿Qué te refieres con los hooks? ¿A mencionar el documentos de agents.md dentro del claude.md no commiteable?

Contenido: Prompt, modelo y respuesta (Recommended)

Carpeta: Abrir el repo directamente (Recommended)
````

**Modelo:** claude-opus-5-5 (versión de la herramienta: 2.1.314)

**Resultado:**
````text
Escrito para: tus compañeros y el profesorado (README, AGENTS.md, guía de IA).

El entorno ya está unificado en Python 3.12 y el registro de prompts está montado, pero no he hecho ningún commit ni push: todo sigue en tu copia local. Con Claude Code, el registro automático empieza en la próxima sesión, con VS Code abierto en practica1/machine_learning. Falta probar el flujo de Copilot.

El lío de ramas y Python
Tu rama local está en el mismo commit que main; solo su copia en GitHub va 2 commits por detrás, así que no hay nada que fusionar. El problema real estaba en main:

uv sync fallaba: en un clon limpio daba error porque pyproject.toml configuraba un paquete que no existe. He quitado esa configuración.
Faltaba scikit-learn: no estaba declarado, y ya está añadido.
Faltaba requirements.txt: se había borrado y es obligatorio en la entrega. Ya está regenerado.
Qué he cambiado
Entorno: pyproject.toml, .python-version, uv.lock y requirements.txt quedan en 3.12, y he añadido .gitattributes para que Windows y WSL usen los mismos saltos de línea.
README.md: incluye el propósito del trabajo, la guía del profesorado con y sin uv, la guía común Windows/WSL, cómo sincronizarse y solución de problemas.
Enunciado: los dos PDF están en Markdown en docs/enunciado/, y todas las palabras de los PDF aparecen en las transcripciones. Añadí una nota porque el apartado 3.2 se contradice: su título dice «4 modelos» y su texto pide 5.
Registro de IA: hay un archivo por persona en docs/ia/. Esta sesión la he apuntado a mano en tu registro, con el análisis crítico pendiente de que lo rellenes tú.
Cómo funciona el registro
Un hook no es mencionar AGENTS.md en CLAUDE.md: es un comando que la herramienta ejecuta sola al enviar un prompt y al terminar la respuesta.

Claude Code (2 de vosotros): el hook se sube al repo, así que funciona sin configurar nada más. Elige el archivo según el nombre o correo de git.
Copilot (1 de vosotros): el agente sigue la regla de AGENTS.md, que es menos fiable que un hook. En modo pregunta hay que copiar el prompt a mano, y el autocompletado solo se declara.
Qué he probado
Prueba	Resultado
Instalación con uv en Windows y WSL	Funciona
Instalación con pip en Windows y WSL	Funciona, con el Python 3.12 llamado directamente, no con py -3.12
Notebook completo en Windows	Se ejecuta sin errores
Hook con una sesión real de Claude Code en Windows	Funciona
Flujo de Copilot	Sin probar: quien lo use debe comprobar en su primera petición que se crea la entrada
Hook en WSL	Sin probar
Lo que tenéis que resolver
Semilla: el notebook usa 42 y tu notebooks/constantes.py, sin subir, usa 123. La profesora considera un error garrafal comparar modelos con semillas distintas, así que acordad una sola; yo no he tocado ninguno de los dos.
Datos de Rodrigo: faltan sus apellidos en el README, y su nombre o correo de git debe contener rodri para que el hook encuentre su archivo.
El repo es público: los registros publicarán todo lo que escribáis al agente, y tu primera entrada ya incluye la ruta de tu wiki. Revisadlos antes de cada commit.
Plazo del 3 de noviembre: el repo ya es público, pero tu guía recoge de clase que hay que compartirlo con Raquel y Pepe. Confirma que lo tienen.
Documento de evolución: las instrucciones piden registrar las decisiones de diseño y los avances, y aún no existe ese documento.
Tu guía de uv en la wiki sigue con ejemplos en 3.13; no la he modificado.
````

**Análisis crítico:**  _(qué se aceptó, qué se rechazó y cómo se corrigió)_

Se aceptan la mayoría de los cambios a nivel de resolución de librerías y la creación del registro automático de IA.
Cambio manualmente la semilla y la unificamos a 42.
Se deja el archivo requirements.txt, aunque con uv no es necesario para que el equipo tenga un entorno unificado. Añado una sección en el README de la raíz para mencionar que al final del desarrollo lo tendremos que actualizar.

## 2026-11-06 19:44:03 +0100 · Claude Code

- **Captura:** automática (hook)
- **Sesión:** d5ddce76

**Prompt literal**

````text
<ide_opened_file>The user opened the file c:\Users\pablo\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\src\eda_pablo.ipynb in the IDE. This may or may not be related to the current task.</ide_opened_file>
Tengo el siguiente notebook @src/eda_pablo.ipynb  y mis compañeros ya han estado trabajando en @src/riesgo_cardiovascular.ipynb  pero yo quiero aportar una visión distinta al trabajo que ya han realizado y es analizar de una forma más enfocada al problema en sí y comprendiendo cada variable como se comporta, que conclusiones podemos ir sacando. En primer lugar quiero centrarme en este punto 3.2 y todo lo que anteriormente he hecho, vamos paso a paso. En primer lugar, quiero sacar la correlación de mi variable objetivo, que es ordinal con el resto de variables numéricas. ¿Cómo lo podría hacer de forma que tenga sentido? Vamos paso a paso, no saltes a más puntos, yo te voy preguntando cuano me atasque.
````

**Modelo:** claude-opus-5-5 (versión de la herramienta: 2.1.318)

**Respuesta final**

````markdown
Para correlacionar una variable objetivo ordinal con variables numéricas, el coeficiente adecuado es **Spearman**, no Pearson.

## Por qué Spearman y no Pearson

- **Pearson** mide relación *lineal* y trata el objetivo como una escala de intervalos: da por hecho que la distancia de bajo a moderado es la misma que de moderado a alto. Con un 0/1/2 clínico eso no está garantizado. Los números solo indican el orden.
- **Spearman** convierte cada variable en rangos y mide si la relación es **monótona**: "a más X, más riesgo", sin suponer distancias ni linealidad. Solo necesita que el objetivo esté ordenado, que es justo lo que tienes.
- Alternativa: **Kendall tau-b**, que trata mejor los empates. Aquí hay muchos, porque el objetivo solo tiene 3 valores. Suele dar valores más bajos que Spearman pero el mismo orden de variables. Puedes usarlo como comprobación, aunque no hace falta. Además, Spearman es coherente con el heatmap que ya tienes en la sección 6.

## Código para la celda 3.2

```python
# Correlación de Spearman de cada variable numérica con el riesgo (0 < 1 < 2).
# Spearman trabaja con rangos: solo exige que el objetivo esté ordenado, no que 0→1 y 1→2 sean "igual de lejos".
corr_objetivo = (
    df[numericas]
    .corrwith(df[objetivo], method="spearman")   # una correlación por columna frente al objetivo
    .sort_values(key=abs, ascending=False)       # ordeno por fuerza, sin importar el signo
    .rename("rho_spearman")
)
corr_objetivo.round(3)
```

- `corrwith` calcula la correlación de cada columna de `df[numericas]` con la serie del objetivo.
- Los nulos se ignoran par a par: para `colesterol_ldl` usa los 2.119 pacientes con dato, no los 2.254.
- `key=abs` ordena por magnitud, así una correlación de −0,20 aparece junto a una de +0,20.

Lo he ejecutado y funciona. Te salen estos valores:

| Variable | ρ | | Variable | ρ |
|---|---|---|---|---|
| consumo_alcohol_semanal | **0,39** | | clearance_creatinina | −0,18 |
| hemoglobina_glicosilada | 0,28 | | edad | 0,16 |
| proteina_c_reactiva | 0,28 | | anos_fumador | 0,15 |
| acido_urico | 0,21 | | perimetro_cintura | 0,14 |
| glucosa_ayunas | 0,21 | | horas_sueno_diarias | −0,14 |
| frecuencia_ejercicio_semanal | −0,21 | | presión sist./diast. | 0,14 |
| colesterol_hdl | −0,20 | | colesterol_ldl | 0,13 |
| indice_masa_corporal | 0,20 | | colesterol total / triglic. / FC reposo | ≤ 0,10 |

## Cómo interpretarlo

1. **Fíjate en el signo y en la magnitud, no en el p-valor.** Con 2.254 pacientes, hasta ρ = 0,05 sale "significativo". Lo útil es comparar magnitudes: aquí todas son débiles o moderadas (< 0,4).
2. **Ninguna variable explica el riesgo por sí sola.** Es razonable que el riesgo dependa de varias a la vez, y por eso tiene sentido usar modelos multivariantes.
3. **Los signos encajan con la clínica:** el HDL ("colesterol bueno"), el ejercicio y el filtrado renal van en negativo, y la glucemia, la inflamación (PCR) y el IMC en positivo.
4. **Hay algo llamativo:** el alcohol es la variable más correlacionada, por encima de la presión arterial o el LDL. Además, en la tabla de tu `df.head()` ya aparecen consumos negativos (−4,9, −1,7). Apúntalo como algo a investigar.

## Dos limitaciones para dejar escritas en el markdown

- **Spearman solo detecta relaciones monótonas.** Si una variable tiene relación en U (por ejemplo, dormir muy poco y dormir demasiado son malos los dos), puede dar ρ ≈ 0 aunque la relación sea importante. Una ρ baja no quiere decir que la variable sea inútil.
- **Este cálculo usa el dataset completo.** Como análisis descriptivo vale, pero si más adelante lo usas para **seleccionar variables**, tiene que hacerse solo con el train para no filtrar información del test.

Cuando lo tengas en el notebook, dime cuál es el siguiente punto en el que te atascas.
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

---

## 2026-11-06 21:17:46 +0100 · Claude Code

- **Captura:** automática (hook)
- **Sesión:** d5ddce76

**Prompt literal**

````text
Venga, ahora estoy con las variables numéricas, como puedes ver, el 24% de los registros tienen al menos algún valor nulo y estos se concentran en 4 variables numéricas: colesterol_ldl, glucosa_ayunas, horas_sueno_diarias y proteina_c_reactiva.

De cara a aplicar alguna estrategia para rellenar los valores nulos, ya sea con la media, la mediana o algún método de imputación de valores, quiero explorar distintas estrategias para ver tendría mayor sentido estadístico utilizar para usar esos valores nulos.

En primer lugar, para LDL, vi por internet que existía la fórmula de fiedewald para calcular una aproximación del LDL y del colesterol total. Para ver si podíamos calcular los valores missing a través de datos ya existentes.

Pero he visto que no tienen correlación entre los valores calculados del colesterol total, tengo 2 aproximaciones, primero mirándolo desde la perspectiva del colesterol total y luego mirándolo de la perspectiva del LDL. ¿Cuál sería la aproximación correcta y de que forma podría plantearme resolver los nulls de LDL? ¿Me falta alguna comprobación?
````

**Modelo:** claude-opus-5-5 (versión de la herramienta: 2.1.318)

**Respuesta final**

````markdown
Las dos aproximaciones son la misma comprobación. La fórmula falla, pero no porque falte una variable: el LDL no está relacionado con ninguna otra columna, y los nulos no dependen del riesgo. Por eso basta con rellenar con la mediana.

## 1. Tus dos aproximaciones miden lo mismo

Las dos salen de la misma igualdad, CT = HDL + LDL + TG/5, solo que despejada de dos formas. Los residuos son exactamente iguales con el signo cambiado (lo he comprobado), así que un histograma es el espejo del otro. Las correlaciones salen parecidas (0,03 y 0,035) porque comparan contra variables distintas, pero dicen lo mismo.

**La perspectiva correcta es la del LDL**, porque es la variable que quieres imputar. La pregunta útil es: *si rellenara un LDL con la fórmula, ¿cuánto me equivocaría?* Se responde con los pacientes que sí tienen LDL:

| Rellenar con… | Error absoluto medio |
|---|---|
| Friedewald | **56,4 mg/dL** |
| La mediana del LDL | **29,5 mg/dL** |

La fórmula se equivoca casi el doble que poner a todos la mediana. Es un argumento más fuerte que la correlación de 0,03 para descartarla.

En la celda 28, `ldl_sin_nulos` rellena con la fórmula que acabas de descartar; yo la quitaría. Además, `value_counts()` no aporta nada en una variable continua.

## 2. Comprobaciones que te faltan

Las he ejecutado; estos son los resultados:

1. **Si la fórmula se puede aplicar.** Friedewald supone unidades en mg/dL (los rangos cuadran) y no es válida con TG ≥ 400. Hay 54 pacientes así, y la fórmula da LDL negativo en 10. Aun así, esto no explica una correlación de 0,03.
2. **Coherencia física.** El colesterol total incluye el HDL y el LDL, así que **HDL + LDL nunca puede superar al CT**. Falla en **559 de 2.119 pacientes (26 %)**. También hay HDL negativos (4) y TG negativos (4). Esto va a tu sección 6 de coherencia clínica.
3. **Si el LDL se relaciona con algo.** Esta es la clave. El LDL es el componente principal del colesterol total, y en datos reales están fuertemente correlacionados. Aquí la ρ de Spearman entre LDL y CT es **0,026**, y la variable más relacionada con el LDL (HbA1c) solo llega a **0,078**. Eso refuta tu hipótesis de la celda 29: si faltara una variable, el LDL seguiría relacionado con sus componentes aunque la fórmula fallara. Lo que pasa es que **los lípidos parecen generados de forma independiente entre sí**.
4. **Por qué faltan los datos (MCAR / MAR / MNAR).** MCAR significa que faltan al azar, MAR que la falta depende de otras variables observadas y MNAR que depende del propio valor que falta. Esto decide si la ausencia aporta información:
   - Riesgo entre pacientes **sin LDL**: 53/30/16 %. **Con LDL**: 50/30/20 %. Chi² p = 0,52, sin diferencia.
   - Probé una hipótesis clínica: los laboratorios no informan el LDL calculado cuando TG ≥ 400. No se cumple: hay un 3,7 % de TG ≥ 400 entre los nulos y un 2,3 % entre los demás.
   - Comparé las otras variables entre pacientes con y sin LDL. Solo sueño y HbA1c dan p = 0,01, y con 18 contrastes eso es esperable por azar: con Bonferroni, el umbral queda en ≈ 0,003.
   - Los nulos de LDL casi no coinciden con los de las otras tres variables (4, 7 y 13 pacientes).

   → El patrón es **compatible con MCAR**.

Código para añadir estas comprobaciones al notebook (lo he probado y da los números de arriba):

```python
# 1) Error de la fórmula desde la perspectiva del LDL, solo en los pacientes con LDL medido
ldl_calculado = df["colesterol_total"] - df["colesterol_hdl"] - df["trigliceridos"] / 5
conocido = df["colesterol_ldl"].notna()
ldl_real = df.loc[conocido, "colesterol_ldl"]
print(f"Error medio con Friedewald: {(ldl_real - ldl_calculado[conocido]).abs().mean():.1f} mg/dL")
print(f"Error medio rellenando con la mediana: {(ldl_real - ldl_real.median()).abs().mean():.1f} mg/dL")

# 2) Condiciones de validez de la fórmula y coherencia física (HDL + LDL no puede superar al CT)
print("TG >= 400 (Friedewald no aplica):", (df["trigliceridos"] >= 400).sum())
print("LDL calculado negativo:", (ldl_calculado < 0).sum())
print("HDL + LDL > colesterol total:", (df["colesterol_hdl"] + df["colesterol_ldl"] > df["colesterol_total"]).sum())

# 3) ¿Hay alguna variable que ayude a predecir el LDL?
display(df[numericas + binarias].corrwith(df["colesterol_ldl"], method="spearman")
        .drop("colesterol_ldl").sort_values(key=abs, ascending=False).head(5).round(3))

# 4) ¿Faltan al azar? Si el nulo dependiera del riesgo, la ausencia sería informativa
from scipy.stats import chi2_contingency
nulo_ldl = df["colesterol_ldl"].isna()
display(pd.crosstab(nulo_ldl, df[objetivo], normalize="index").round(2))
print("p-valor chi²:", round(chi2_contingency(pd.crosstab(nulo_ldl, df[objetivo])).pvalue, 3))
```

## 3. Cómo resolver los nulos de LDL

- **Imputación simple con la mediana.** Un imputador multivariante (KNN, `IterativeImputer`) estima el valor que falta a partir de otras variables. Si ninguna se relaciona con el LDL (ρ máx. 0,08), no tiene de dónde sacar información y añade complejidad sin ganar nada. La media y la mediana coinciden casi del todo, porque el LDL es simétrico (asimetría −0,05). La mediana es más robusta frente a los valores extremos que ya has visto.
- **Sin indicador de nulo** (`add_indicator=True`). Lo descartaría, porque la ausencia no se relaciona con el riesgo (p = 0,52). Déjalo anotado como opción descartada y con su motivo.
- **Va dentro del `Pipeline`:** `SimpleImputer(strategy="median")` se ajusta solo con el train.
- **Coste:** imputar con la mediana reduce un poco la varianza del LDL y diluye algo su relación con el riesgo. Con un 6 % de nulos el efecto es pequeño.

Si quieres demostrarlo empíricamente, el siguiente paso sería una **simulación de nulos**: ocultar un 10 % de los LDL conocidos, imputarlos con la mediana, con KNN y con `IterativeImputer`, y comparar el error con los valores reales. Además, la celda de la sección 6 que lista las 10 parejas más relacionadas ya deja ver el problema: ninguna correlación entre variables numéricas pasa de 0,11. Cuando quieras, seguimos con la simulación o con la glucosa.
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_
Se acepta explicando las implicaciones que tiene en la decisión.
---

## 2026-11-06 21:59:53 +0100 · Claude Code

- **Captura:** automática (hook)
- **Sesión:** d5ddce76

**Prompt literal**

````text
<ide_opened_file>The user opened the file c:\Users\pablo\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\src\eda_pablo.ipynb in the IDE. This may or may not be related to the current task.</ide_opened_file>
Okay, ahora quiero hacer comprobaciones con el resto de variables, para determinar también con ellas cual es el método más interesante para imputar estos valores missing, pero entiendo que vamos a repetir acciones más de una vez, así que me gustaría que me construyeras una función que fácilmente me comprobase si existe alguna relación con el riesgo el que exista ese valor faltante, ver si existe alguna variable con alta correlación que me pueda ayudar a entender si debo aplicar una fórmula o una imputación multivariante y si es simétrica (usar la media) o tiene cola (usar la mediana).

Para el resto de casos no tengo fórmulas que me puedan ayudar, así que vamos solo con eso y comprobamos rápidamente la aproximación más interesante para cada una de ellas.
````

**Modelo:** claude-opus-5-5 (versión de la herramienta: 2.1.318)

**Respuesta final**

````markdown
He escrito la función y la he probado con las cuatro variables. Para ninguna sale una relación entre el dato faltante y el riesgo, ni una variable que la prediga. Solo la PCR tiene cola: mediana para la PCR y media para las otras tres.

## La función

Tiene parámetros con valor por defecto para que puedas cambiar los umbrales sin tocar el código:

```python
from scipy.stats import chi2_contingency

def diagnostico_nulos(df, variable, objetivo, predictoras,
                      umbral_corr=0.3, umbral_asimetria=0.5, alfa=0.05):
    """Resume las tres comprobaciones que deciden cómo imputar `variable`.

    1. Si que falte el dato se relaciona con el riesgo (chi²) -> ¿añadir un indicador de nulo?
    2. Si alguna otra variable la acompaña (Spearman)          -> ¿imputación multivariante?
    3. Si es simétrica o tiene cola (asimetría)                -> ¿media o mediana?
    """
    nulo = df[variable].isna()              # True en los pacientes a los que les falta el dato
    clase_alta = df[objetivo].max()         # la clase de riesgo alto (2)

    # 1) Tabla "falta el dato (sí/no)" × clase de riesgo. Si el p-valor es bajo, la ausencia es informativa.
    tabla = pd.crosstab(nulo, df[objetivo])
    p_riesgo = chi2_contingency(tabla).pvalue
    reparto = pd.crosstab(nulo, df[objetivo], normalize="index")   # % de cada clase en cada grupo

    # 2) Spearman con el resto de predictoras (sin el objetivo: el imputador del Pipeline no ve la y).
    otras = [c for c in predictoras if c != variable]
    rho = df[otras].corrwith(df[variable], method="spearman")
    mejor = rho.abs().idxmax()              # la que más se relaciona, sea con signo + o −

    # 3) Asimetría con los valores observados: ≈ 0 simétrica, > 0 cola a la derecha, < 0 a la izquierda
    asimetria = df[variable].skew()

    # Decisión: primero miro si hay en qué apoyarse para una imputación multivariante; si no, media o mediana
    if abs(rho[mejor]) >= umbral_corr:
        metodo = "multivariante (KNN / Iterative)"
    elif abs(asimetria) < umbral_asimetria:
        metodo = "media"
    else:
        metodo = "mediana"

    return {
        "variable": variable,
        "% nulos": round(nulo.mean() * 100, 1),
        "% riesgo alto (nulos)": round(reparto.loc[True, clase_alta] * 100, 1),
        "% riesgo alto (con dato)": round(reparto.loc[False, clase_alta] * 100, 1),
        "p chi² riesgo": round(p_riesgo, 3),
        "indicador de nulo": "sí" if p_riesgo < alfa else "no",
        "más correlacionada": mejor,
        "rho": round(rho[mejor], 3),
        "asimetría": round(asimetria, 2),
        "media": round(df[variable].mean(), 2),
        "mediana": round(df[variable].median(), 2),
        "imputación propuesta": metodo,
    }
```

Para aplicarla a todas las variables con nulos a la vez:

```python
con_nulos = [c for c in numericas if df[c].isna().any()]
resumen = pd.DataFrame([diagnostico_nulos(df, v, objetivo, numericas + binarias) for v in con_nulos])
resumen.set_index("variable").T
```

**Umbrales que conviene citar en la memoria:**
- |ρ| ≥ 0,3: según Cohen, 0,1 es un efecto pequeño y 0,3 uno moderado. Por debajo, otra variable no aporta suficiente para estimar la que falta.
- |asimetría| < 0,5: regla habitual para considerar una distribución aproximadamente simétrica.

## Resultados

| | LDL | Glucosa | Sueño | PCR |
|---|---|---|---|---|
| % nulos | 6,0 | 5,0 | 8,0 | 7,0 |
| % riesgo alto (nulos / con dato) | 16 / 20 | **28 / 20** | 19 / 20 | 17 / 20 |
| p chi² | 0,52 | 0,11 | 0,90 | 0,08 |
| Más correlacionada (ρ) | HbA1c (0,08) | ác. úrico (0,08) | ác. úrico (−0,07) | alcohol (0,10) |
| Asimetría | −0,05 | 0,12 | 0,02 | **1,59** |
| Media / mediana | 135,6 / 135,5 | 104,1 / 103,8 | 6,75 / 6,8 | **2,35 / 1,79** |
| **Propuesta** | media | media | media | **mediana** |

### Conclusiones

1. **Que falte un dato no se relaciona con el riesgo en ninguna variable.** El caso más dudoso es la glucosa: entre los pacientes sin dato hay un 28 % de riesgo alto, frente al 20 % del resto. Pero p = 0,11, con solo 112 nulos y 4 contrastes. Yo lo anotaría como un indicio débil. Si quieres asegurarte, puedes probar `add_indicator=True` en la validación cruzada y ver si mejora algo.
2. **Ninguna variable pasa de ρ = 0,10 con las que tienen nulos**, así que se descarta la imputación multivariante en las cuatro. Pasa lo mismo que con el LDL: las variables parecen generadas de forma independiente entre sí.
3. **La elección entre media y mediana solo importa en la PCR.** En las otras tres, media y mediana prácticamente coinciden, así que da igual cuál uses. La PCR tiene una cola larga a la derecha (asimetría 1,59) y su media está un 31 % por encima de la mediana. Rellenar con la media inflaría la inflamación de los pacientes sin dato. Además encaja con la clínica: la PCR suele ser baja en la mayoría y muy alta en unos pocos con inflamación.

**Opción más simple y defendible:** como la media y la mediana coinciden en las variables simétricas, puedes usar **un solo `SimpleImputer(strategy="median")` para todas las numéricas**. Da el mismo resultado y protege frente a los valores extremos que aún no has limpiado.

## Dos cosas que la función no mira

- **Variables categóricas.** La función solo usa numéricas y binarias. Las he revisado aparte con Kruskal-Wallis, que compara la variable entre los grupos de cada categórica. Hay diferencias significativas, pero pequeñas. La mayor está en el LDL: mediana de 143 con antecedentes en ambos padres frente a 133 sin antecedentes, una diferencia de una cuarta parte de su desviación típica. No justifica un imputador multivariante, pero conviene mencionarlo.
- **El orden de las operaciones.** La media y la mediana se calculan con todos los valores observados, incluidos los imposibles: PCR = 0,0, glucosa = 32 o LDL = 6,1. En el `Pipeline`, primero convierte en nulo lo que sea fisiológicamente imposible (sección 6) y después imputa. Si no, esos valores entran en el cálculo del relleno.

He verificado el código ejecutándolo sobre el dataset completo. No he tocado tu notebook: pégalo en la celda que prefieras.
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

Debemos hacer varios matices a esta función de *diagnostico_nulos*:

1. **Los umbrales (0,3 y 0,5) son arbitrarios**: pero no afectan demasiado porque solo proteina_c_reactiva pasa del umbral de asimetría.

2. La correlación por parejas no prueba que el imputador multivariante falle, pero sí es un indicio que hay que comprobar.

3. El problema de tener 2 imputadores es que nos obliga a aplicar varios transformer sin grandes ganancias, así que es probable que lo más interesante sea usar la mediana para todas.

Cambiamos la lógica para decidir entre mediana y un método de imputación.

---

## 2026-11-07 00:08:48 +0100 · Claude Code

- **Captura:** automática (hook)
- **Sesión:** d5ddce76

**Prompt literal**

````text
<ide_opened_file>The user opened the file c:\Users\pablo\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\src\eda_pablo.ipynb in the IDE. This may or may not be related to the current task.</ide_opened_file>
Okay, ahora me gustaría hacer el experimento para comprobar las conclusiones que he planteado en la celda markdown del apartado 5. Quiero demostrar que realmente la estrategia de imputación más interesante sería la mediana o la media vs knn imputer o iterative imputer.

Para eso habría que usar pacientes sin nulos, esconder un cieto porcentaje a cada una de las variables par que sean parte de nuestro test, y repetirlo varias veces en sorteos distintos  porque un solo sorteo puede engañar. Y para comprobarlo, puedo comprobar puedo usar el MAE. Comparando métodos univariantes con multivariantes. ¿Cómo lo plantearías para el apartado 5.3?
````

## 2026-11-07 00:12:00 +0100 · Claude Code

- **Captura:** automática (hook)
- **Sesión:** d5ddce76

**Prompt literal**

````text
Sería solo para las variables numéricas
````

**Modelo:** claude-opus-5-5 (versión de la herramienta: 2.1.318)

**Respuesta final**

````markdown
He montado el experimento del 5.3 con el mismo esquema que el notebook del profesor, usando solo las 19 numéricas. Confirma tus conclusiones: ningún imputador multivariante mejora de forma apreciable a la mediana, y el KNN con 5 vecinos es claramente peor.

## Diseño del experimento

| Decisión | Por qué |
|---|---|
| Solo los **1.721 pacientes sin ningún nulo** | Así conozco el valor real de cada hueco y puedo medir el error. |
| En cada variable oculto **el mismo % de nulos que tiene de verdad** (103, 86, 137 y 120 valores), elegidos al azar | Imito la situación real. Ocultar al azar es coherente con el chi² del 5.2, que no mostró relación entre faltar y el riesgo. |
| El imputador ve solo las **19 numéricas** | Lo que pediste. Nunca ve el objetivo, igual que dentro del `Pipeline`. |
| **Estandarizo** antes de imputar | KNN mide distancias; sin escalar, las dominarían el colesterol y los triglicéridos. A la media y la mediana no les afecta. |
| **30 sorteos** con un generador creado con `cte.semilla` | Un solo sorteo puede engañar; con 30 tengo media ± desviación y son reproducibles. |
| **KNN con k=5 y k=25** | Así se ve qué pasa al promediar más vecinos. |
| **MAE**, y además RMSE (raíz del error cuadrático medio) | La explicación está en la conclusión 3. |

## Celdas para el notebook

He ejecutado este código tal cual desde `src/` (unos 13 s) y da las tablas de abajo.

```python
from sklearn.experimental import enable_iterative_imputer  # habilita IterativeImputer (sigue siendo experimental)
from sklearn.impute import SimpleImputer, KNNImputer, IterativeImputer

predictoras = numericas                                     # solo las 19 numéricas (sin binarias ni objetivo)
completos = df[predictoras].dropna().reset_index(drop=True)  # pacientes sin ningún nulo: conozco el valor real
pct_nulos = df[con_nulos].isna().mean()                      # oculto el mismo % que falta de verdad
print(f"Pacientes completos: {len(completos)}")
print("Valores que se ocultan en cada sorteo:", (pct_nulos * len(completos)).round().astype(int).to_dict())

imputadores = {
    "media": SimpleImputer(strategy="mean"),
    "mediana": SimpleImputer(strategy="median"),
    "KNN (k=5)": KNNImputer(n_neighbors=5),
    "KNN (k=25)": KNNImputer(n_neighbors=25),
    "Iterative": IterativeImputer(max_iter=10, random_state=cte.semilla),
}
```

```python
def un_sorteo(datos, pct_nulos, imputadores, rng):
    """Oculta valores al azar, los reconstruye con cada imputador y mide el error en los huecos."""
    # 1) Máscara: en cada variable marco al azar el mismo % de pacientes que tiene nulos en el dataset real
    mascara = pd.DataFrame(False, index=datos.index, columns=datos.columns)
    for variable, p in pct_nulos.items():
        filas = rng.choice(len(datos), size=round(p * len(datos)), replace=False)
        mascara.loc[filas, variable] = True
    huecos = datos.mask(mascara)                       # pongo NaN donde la máscara es True

    # 2) Estandarizo para que KNN no mida distancias dominadas por las variables de mayor escala
    #    (colesterol, triglicéridos). A la media y la mediana no les afecta: el cambio de escala se deshace al final.
    centro, escala = huecos.mean(), huecos.std()
    z = (huecos - centro) / escala

    # 3) Reconstruyo con cada imputador y comparo con el valor real solo en las celdas ocultas
    filas_resultado = []
    for nombre, imputador in imputadores.items():
        reconstruido = pd.DataFrame(imputador.fit_transform(z), columns=datos.columns) * escala + centro
        for variable in pct_nulos.index:
            ocultos = mascara[variable]
            error = reconstruido.loc[ocultos, variable] - datos.loc[ocultos, variable]
            filas_resultado.append({"método": nombre, "variable": variable,
                                    "MAE": error.abs().mean(),
                                    "RMSE": np.sqrt((error ** 2).mean())})
    return filas_resultado
```

```python
n_sorteos = 30
rng = np.random.default_rng(cte.semilla)   # un generador con la semilla del proyecto: 30 sorteos distintos pero reproducibles
resultados = pd.DataFrame([
    {**fila, "sorteo": i}
    for i in range(n_sorteos)
    for fila in un_sorteo(completos, pct_nulos, imputadores, rng)
])

def media_desv(metrica):
    """Tabla variable × método con 'media ± desviación' de la métrica en los 30 sorteos."""
    r = resultados.groupby(["variable", "método"])[metrica].agg(["mean", "std"])
    texto = r["mean"].map("{:.2f}".format) + " ± " + r["std"].map("{:.2f}".format)
    return texto.unstack()[list(imputadores)]

display(media_desv("MAE"))
print("Referencia, desviación típica de cada variable:", completos[con_nulos].std().round(2).to_dict())
```

```python
# Comparación por parejas: en cada sorteo todos los métodos rellenan los mismos huecos,
# así que puedo contar en qué % de sorteos cada método mejora a la mediana.
mae = resultados.pivot_table(index=["variable", "sorteo"], columns="método", values="MAE")
victorias = mae.drop(columns="mediana").lt(mae["mediana"], axis=0).groupby("variable").mean()
display((victorias * 100).round(0)[[m for m in imputadores if m != "mediana"]])
```

```python
display(media_desv("RMSE"))
```

## Resultados

**MAE (media ± desviación en 30 sorteos):**

| | media | mediana | KNN k=5 | KNN k=25 | Iterative | desv. típica |
|---|---|---|---|---|---|---|
| LDL | 29,01 ± 1,95 | 29,03 ± 1,95 | **31,79** ± 2,32 | 29,50 ± 2,20 | 29,06 ± 1,97 | 36,7 |
| Glucosa | 20,28 ± 1,86 | 20,29 ± 1,86 | **21,87** ± 1,95 | 20,44 ± 2,01 | 20,08 ± 1,84 | 25,3 |
| Sueño | 1,26 ± 0,07 | 1,26 ± 0,07 | **1,36** ± 0,08 | 1,27 ± 0,07 | 1,26 ± 0,07 | 1,58 |
| PCR | 1,56 ± 0,11 | **1,48** ± 0,14 | 1,67 ± 0,13 | 1,57 ± 0,11 | 1,55 ± 0,11 | 2,01 |

**% de sorteos en que cada método mejora a la mediana:** KNN k=5 entre el 0 y el 3 %. Iterative: 47 % en LDL, 73 % en glucosa, 47 % en sueño y 3 % en PCR.

### Cómo leerlo

1. **El KNN con 5 vecinos es el peor en las cuatro variables**: entre un 8 y un 10 % más de error, y pierde frente a la mediana en el 97-100 % de los sorteos. Con 25 vecinos se acerca a la media. Cuantos más vecinos promedia, más se parece al promedio global, lo que indica que los vecinos no aportan información.
2. **Iterative empata con la media.** Hace una regresión con coeficientes casi nulos, así que acaba prediciendo la media. Su única ventaja es en la glucosa: 0,2 mg/dL (un 1 %), muy por debajo de la variación entre sorteos (±1,8). Es una mejora constante pero irrelevante, y no justifica un imputador experimental.
3. **En la PCR, la elección entre media y mediana depende de la métrica.** Con el MAE gana la mediana (1,48 frente a 1,56, en el 100 % de los sorteos). Con el RMSE gana la media (2,08 frente a 2,17). Es una propiedad matemática: entre los valores constantes, la mediana es el que minimiza el error absoluto y la media el que minimiza el error cuadrático. Si eliges el MAE, conviene justificarlo en la memoria: está en mg/L y no lo dominan los pocos pacientes con PCR muy alta.
4. **En todos los métodos, el MAE es ≈ 0,8 veces la desviación típica.** Es lo que se espera al rellenar siempre con el centro de la distribución. Ningún método recupera el valor individual del paciente: solo estiman ese centro.

**Conclusión:** `SimpleImputer(strategy="median")` para las cuatro variables, como habías propuesto. Es igual o mejor que las alternativas, es el más simple y no necesita escalado.

## Dos matices para el markdown

- Aquí el imputador se ajusta con todos los pacientes completos, porque mido la calidad de la reconstrucción, no el modelo. En el `Pipeline` se ajustará solo con el train.
- La prueba definitiva es la que anotaste en el 5.1: comparar `SimpleImputer` y `KNNImputer` dentro del pipeline con validación cruzada, porque lo que importa al final es el recall de riesgo alto, no el MAE.

**Ojo:** la salida guardada de la tabla del 5.2 sigue diciendo "media" en LDL, glucosa y sueño. Viene de la versión anterior de la función; vuelve a ejecutar esa celda para que coincida con el código actual, que ya propone "mediana".

No he tocado tu notebook. Las pruebas están en `C:\Users\pablo\AppData\Local\Temp\claude\1c89b8a32de7a558\d5ddce76-2842-4d52-9bf7-f49c77e483c9\scratchpad\exp_final.py`.
````

**Análisis crítico:** _(qué se aceptó, qué se rechazó y cómo se corrigió)_

El código es robusto, así que se acepta en su mayoría, las conclusiones; aunque me las adelanta en parte la IA las
desarrollo yo y le dedico tiempo a asegurarme entenderalas.

---

## 2026-11-09 21:39:08 +0100 · Claude Code

- **Captura:** automática (hook)
- **Sesión:** 8bea045d

**Prompt literal**

````text
Échale un vistazo a @estrategia_ml.txt . son los apuntes que tomó Rodri en la última reunión que tuvimos, yo también tomé algunos apuntes de esa reunión, echales un vistazo y creame un resumen no muy extenso en un archivo mardown que nos pueda servir para cuando construyamos la memoria técnica al exponer la evolución del planteamiento del problema, decisiones de diseño y avances tal y como pide @docs/enunciado/instrucciones_entrega.md
````

**Modelo:** claude-opus-5-5 (versión de la herramienta: 2.1.319)

**Respuesta final**

````markdown
Escrito para: el equipo (Pablo, Enzo y Rodrigo), como base de la memoria técnica.

He creado [docs/evolucion_planteamiento.md](docs/evolucion_planteamiento.md) a partir del acta de Rodrigo ([estrategia_ml.txt](estrategia_ml.txt)) y de tus apuntes de la reunión del 8 de noviembre. Tiene tres partes:

1. **Punto de partida:** el entorno común, el EDA de cada uno y los problemas que encontrasteis en los datos.
2. **Reunión del 8 de noviembre:**
   - el reparto de modelos;
   - el diseño experimental, con el motivo de cada decisión;
   - la limpieza y la codificación de los datos;
   - el pipeline;
   - una tabla de **opciones descartadas y por qué**, que el acta de Rodrigo no recogía y que conviene para la memoria y la entrevista;
   - lo que se ha hecho después de la reunión.
3. **Cuestiones abiertas:**
   - `class_weight` no funciona en Naive Bayes ni en `GradientBoostingClassifier`, que son dos de tus modelos;
   - el balanceo debe decidirlo la comparación, no darse por hecho que gana SMOTENC;
   - no hay forma de probar el árbol y el random forest sin imputar;
   - falta un modelo de referencia que prediga siempre la clase mayoritaria;
   - queda por decidir si usar 5 o 10 folds.

Queda revisar los siguientes motivos que no se dijeron en la reunión:

- Las razones para **no usar el logaritmo y PCA** («el `RobustScaler` ya controla las escalas» y «PCA resta interpretabilidad») las he añadido yo. 
- En la reunión **solo quedó un «PCA, probablemente no»**. Confirmadlas o cambiadlas antes de llevarlas a la memoria.

No he hecho commit. El hook ya ha registrado este prompt en tu registro de IA.
````

**Análisis crítico:** _(qué se aceptó, qué se rechazó y cómo se corrigió)_

Se revisa el esqueleto y contenido. La aproximación que hace la IA es muy certera dado que tiene acceso a parte
a nuestros apuntes de la reunión, al propio repo y puede contrastar las decisiones tomadas con la realidad actual
del repo, en el que ya hemos empezado a implementar los cambios que se propusieron durante la misma.

Queda a la espera también de revisión de mis compañeros por si ellos se acordasen de algún detalle más o quisieran
resumir un poco más.

---

## 2026-11-11 00:41:00 +0100 · Claude Code

- **Captura:** automática (hook)
- **Sesión:** 2ae22ad1

**Prompt literal**

````text
<ide_opened_file>The user opened the file c:\Users\pablo\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\src\modelos_pablo.ipynb in the IDE. This may or may not be related to the current task.</ide_opened_file>
Estoy intentando aplicar un ajuste de hiperparámetros sobre la regresión logística en @src/modelos_pablo.ipynb  usando @src/utils/modelado.py   pero no se por qué me da el siguiente error:

<pasted_content id="42c8">
---------------------------------------------------------------------------
_RemoteTraceback                          Traceback (most recent call last)
_RemoteTraceback: 
"""
Traceback (most recent call last):
  File "c:\Users\pablo\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\.venv\Lib\site-packages\joblib\externals\loky\process_executor.py", line 490, in _process_worker
    r = call_item()
        ^^^^^^^^^^^
  File "c:\Users\pablo\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\.venv\Lib\site-packages\joblib\externals\loky\process_executor.py", line 291, in __call__
    return self.fn(*self.args, **self.kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\pablo\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\.venv\Lib\site-packages\joblib\parallel.py", line 607, in __call__
    return [func(*args, **kwargs) for func, args, kwargs in self.items]
            ^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\pablo\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\.venv\Lib\site-packages\sklearn\utils\parallel.py", line 184, in __call__
    return self.function(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\pablo\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\.venv\Lib\site-packages\sklearn\model_selection\_validation.py", line 832, in _fit_and_score
    estimator = estimator.set_params(**clone(parameters, safe=False))
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\pablo\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\.venv\Lib\site-packages\sklearn\pipeline.py", line 289, in set_params
    self._set_params("steps", **kwargs)
  File "c:\Users\pablo\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\.venv\Lib\site-packages\sklearn\utils\metaestimators.py", line 75, in _set_params
    super().set_params(**params)
  File "c:\Users\pablo\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\.venv\Lib\site-packages\sklearn\base.py", line 428, in set_params
    raise ValueError(
ValueError: Invalid parameter 'C' for estimator Pipeline(steps=[('preprocesado',
                 ColumnTransformer(transformers=[('num',
                                                  Pipeline(steps=[('imputar',
                                                                   SimpleImputer(strategy='median')),
                                                                  ('escalar',
                                                                   RobustScaler())]),
                                                  ['edad', 'presion_sistolica',
                                                   'presion_diastolica',
                                                   'colesterol_total',
                                                   'colesterol_hdl',
                                                   'colesterol_ldl',
                                                   'trigliceridos',
                                                   'glucosa_ayunas',
                                                   'indice_masa_corporal',
                                                   'frecuencia_cardiaca_reposo',
                                                   'h...
                                                 ('cat', 'passthrough',
                                                  ['fumador_actual',
                                                   'hipertension_previa',
                                                   'diabetes_mellitus',
                                                   'tratamiento_estatinas',
                                                   'uso_antihipertensivos',
                                                   'nivel_actividad',
                                                   'dieta_baja_en_carbohidratos',
                                                   'dieta_occidental',
                                                   'dieta_vegetariana',
                                                   'antecedentes_familiares_paterno',
                                                   'antecedentes_familiares_materno'])])),
                ('modelo',
                 LogisticRegression(max_iter=5000, random_state=42,
                                    solver='saga'))]). Valid parameters are: ['memory', 'steps', 'transform_input', 'verbose'].
"""

The above exception was the direct cause of the following exception:

ValueError                                Traceback (most recent call last)
Cell In[16], line 12
      8 
      9 busquedas, tablas = {}, []
     10 for balanceo in balanceos:
     11     busqueda = mod.crear_busqueda(mod.crear_pipeline(logistica, balanceo=balanceo), parametros_logistica)
---> 12     busquedas[balanceo] = busqueda.fit(X_train, y_train)
     13     tablas.append(mod.tabla_resultados(busqueda, f"{nombre} | {balanceo}"))
     14 
     15 tabla = pd.concat(tablas)[["f1_macro_val", "f1_macro_val_std", "recall_alto_val", "recall_alto_val_std",

File ~\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\.venv\Lib\site-packages\sklearn\base.py:1403, in _fit_context.<locals>.decorator.<locals>.wrapper(estimator, *args, **kwargs)
   1393     estimator._validate_params()
   1395 with (
   1396     config_context(
   1397         skip_parameter_validation=(
   (...)   1401     callback_management_context(estimator),
   1402 ):
-> 1403     return fit_method(estimator, *args, **kwargs)

File ~\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\.venv\Lib\site-packages\sklearn\model_selection\_search.py:1134, in BaseSearchCV.fit(self, X, y, **params)
   1131     return results
   1133 if "callback_ctx" in signature(self._run_search).parameters:
-> 1134     self._run_search(evaluate_candidates, callback_ctx=root_callback_ctx)
   1135 else:
   1136     # custom search classes
   1137     self._run_search(evaluate_candidates)

File ~\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\.venv\Lib\site-packages\sklearn\model_selection\_search.py:1721, in GridSearchCV._run_search(self, evaluate_candidates, callback_ctx)
   1713 candidate_params = ParameterGrid(self.param_grid)
   1715 search_ctx = callback_ctx.subcontext(
   1716     task_name="search",
   1717     max_subtasks=len(candidate_params) * self.n_splits_,
   1718     sequential_subtasks=False,
   1719 ).call_on_fit_task_begin(estimator=self)
-> 1721 evaluate_candidates(ParameterGrid(self.param_grid), callback_ctx=search_ctx)
   1723 search_ctx.call_on_fit_task_end(estimator=self)

File ~\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\.venv\Lib\site-packages\sklearn\model_selection\_search.py:1083, in BaseSearchCV.fit.<locals>.evaluate_candidates(candidate_params, cv, more_results, callback_ctx)
   1080 else:
   1081     evaluation_contexts = [None] * len(candidate_split_pairs)
-> 1083 out = parallel(
   1084     delayed(_fit_and_score)(
   1085         clone(base_estimator),
   1086         X,
   1087         y,
   1088         train=train,
   1089         test=test,
   1090         parameters=parameters,
   1091         split_progress=(split_idx, n_splits),
   1092         candidate_progress=(cand_idx, n_candidates),
   1093         **fit_and_score_kwargs,
   1094         caller=self,
   1095         callback_ctx=evaluation_ctx,
   1096     )
   1097     for (
   1098         ((cand_idx, parameters), (split_idx, (train, test))),
   1099         evaluation_ctx,
   1100     ) in zip(candidate_split_pairs, evaluation_contexts)
   1101 )
   1103 if len(out) < 1:
   1104     raise ValueError(
   1105         "No fits were performed. "
   1106         "Was the CV iterator empty? "
   1107         "Were there no candidates?"
   1108     )

File ~\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\.venv\Lib\site-packages\sklearn\utils\parallel.py:91, in Parallel.__call__(self, iterable)
     79 warning_filters = (
     80     filters_func() if filters_func is not None else warnings.filters
     81 )
     83 iterable_with_config_and_warning_filters = (
     84     (
     85         _with_config_and_warning_filters(delayed_func, config, warning_filters),
   (...)     89     for delayed_func, args, kwargs in iterable
     90 )
---> 91 return super().__call__(iterable_with_config_and_warning_filters)

File ~\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\.venv\Lib\site-packages\joblib\parallel.py:2098, in Parallel.__call__(self, iterable)
   2092 # The first item from the output is blank, but it makes the interpreter
   2093 # progress until it enters the Try/Except block of the generator and
   2094 # reaches the first `yield` statement. This starts the asynchronous
   2095 # dispatch of the tasks to the workers.
   2096 next(output)
-> 2098 return output if self.return_generator else list(output)

File ~\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\.venv\Lib\site-packages\joblib\parallel.py:1704, in Parallel._get_outputs(self, iterator, pre_dispatch)
   1701     yield
   1703     with self._backend.retrieval_context():
-> 1704         yield from self._retrieve()
   1706 except GeneratorExit:
   1707     # The generator has been garbage collected before being fully
   1708     # consumed. This aborts the remaining tasks if possible and warn
   1709     # the user if necessary.
   1710     self._exception = True

File ~\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\.venv\Lib\site-packages\joblib\parallel.py:1806, in Parallel._retrieve(self)
   1800 while self._wait_retrieval():
   1801     # If the callback thread of a worker has signaled that its task
   1802     # triggered an exception, or if the retrieval loop has raised an
   1803     # exception (e.g. `GeneratorExit`), exit the loop and surface the
   1804     # worker traceback.
   1805     if self._aborting:
-> 1806         self._raise_error_fast()
   1807         break
   1809     nb_jobs = len(self._jobs)

File ~\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\.venv\Lib\site-packages\joblib\parallel.py:1885, in Parallel._raise_error_fast(self)
   1881 # If this error job exists, immediately raise the error by
   1882 # calling get_result. This job might not exists if abort has been
   1883 # called directly or if the generator is gc'ed.
   1884 if error_job is not None:
-> 1885     error_job.get_result(self.timeout)

File ~\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\.venv\Lib\site-packages\joblib\parallel.py:780, in BatchCompletionCallBack.get_result(self, timeout)
    774 backend = self.parallel._backend
    776 if backend.supports_retrieve_callback:
    777     # We assume that the result has already been retrieved by the
    778     # callback thread, and is stored internally. It's just waiting to
    779     # be returned.
--> 780     return self._return_or_raise()
    782 # For other backends, the main thread needs to run the retrieval step.
    783 try:

File ~\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\.venv\Lib\site-packages\joblib\parallel.py:795, in BatchCompletionCallBack._return_or_raise(self)
    793 try:
    794     if self.status == TASK_ERROR:
--> 795         raise self._result
    796     return self._result
    797 finally:

ValueError: Invalid parameter 'C' for estimator Pipeline(steps=[('preprocesado',
                 ColumnTransformer(transformers=[('num',
                                                  Pipeline(steps=[('imputar',
                                                                   SimpleImputer(strategy='median')),
                                                                  ('escalar',
                                                                   RobustScaler())]),
                                                  ['edad', 'presion_sistolica',
                                                   'presion_diastolica',
                                                   'colesterol_total',
                                                   'colesterol_hdl',
                                                   'colesterol_ldl',
                                                   'trigliceridos',
                                                   'glucosa_ayunas',
                                                   'indice_masa_corporal',
                                                   'frecuencia_cardiaca_reposo',
                                                   'h...
                                                 ('cat', 'passthrough',
                                                  ['fumador_actual',
                                                   'hipertension_previa',
                                                   'diabetes_mellitus',
                                                   'tratamiento_estatinas',
                                                   'uso_antihipertensivos',
                                                   'nivel_actividad',
                                                   'dieta_baja_en_carbohidratos',
                                                   'dieta_occidental',
                                                   'dieta_vegetariana',
                                                   'antecedentes_familiares_paterno',
                                                   'antecedentes_familiares_materno'])])),
                ('modelo',
                 LogisticRegression(max_iter=5000, random_state=42,
                                    solver='saga'))]). Valid parameters are: ['memory', 'steps', 'transform_input', 'verbose'].
</pasted_content id="42c8">

¿Qué falla en mi planteamiento?
````

**Modelo:** claude-opus-5-5 (versión de la herramienta: 2.1.319)

**Respuesta final**

````markdown
El fallo está en la rejilla, no en `modelado.py`. Los hiperparámetros llevan el nombre de la regresión logística sin prefijo, pero `GridSearchCV` no recibe la `LogisticRegression` directamente: recibe el `Pipeline` entero.

## Por qué falla

`GridSearchCV` hace en cada combinación algo así:

```python
pipeline.set_params(C=0.001, l1_ratio=0)
```

El `Pipeline` no tiene ningún parámetro `C`. Solo tiene `memory`, `steps`, `transform_input` y `verbose`, que son justo los que lista el error. Para llegar a un parámetro de un paso hay que indicar la ruta con el nombre del paso y doble guion bajo: `<paso>__<parámetro>`. En `crear_pipeline` el modelo es el paso `"modelo"` ([modelado.py:106](src/utils/modelado.py#L106)), así que el parámetro es `modelo__C`. Lo indica también el docstring de `crear_busqueda` ([modelado.py:114](src/utils/modelado.py#L114)).

## Corrección

```python
parametros_logistica = {
    "modelo__C": [0.001, 0.01, 0.1, 1, 10, 100],
    "modelo__l1_ratio": [0, 0.5, 1],
}
```

Con esto vale para los tres balanceos: el paso final se llama `"modelo"` aunque haya un paso `"balanceo"` antes.

## Otro problema en esa celda

```python
tablas.append(mod.tabla_resultados(busqueda, f"{nombre} | {balanceo}"))
```

`nombre` no está definido en esta celda. Viene del bucle `for nombre, modelo in modelos.items()` del apartado 2, así que vale `"hist_gradient_boosting"`, el último modelo de ese diccionario. La tabla saldría con las filas de la logística etiquetadas como HistGradientBoosting. Pon el nombre directamente:

```python
tablas.append(mod.tabla_resultados(busqueda, f"regresion_logistica | {balanceo or 'sin_balanceo'}"))
```

He puesto `balanceo or 'sin_balanceo'` para que coincida con las etiquetas del apartado 2. Si no, la fila sin balanceo aparecería como `None`.
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

---

## 2026-11-11 01:03:59 +0100 · Claude Code

- **Captura:** automática (hook)
- **Sesión:** 2ae22ad1

**Prompt literal**

````text
<ide_opened_file>The user opened the file c:\Users\pablo\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\src\modelos_rodrigo.ipynb in the IDE. This may or may not be related to the current task.</ide_opened_file>
Vale, ya funciona, pero ahora me gustaría que viendo que voy a tener que repetir el proceso varias veces cada vez que ajuste parametros (con Bayes, logística o con HistGradient Boosting) y quiera sacar los mejores parámetros, me gustaría sacar una función general que me permitiera pasarle distintos modelos y que me saque además de los valores que tenemos definidos en la variable columnas, los mejores parámetros, inyectandole el nombre desde fuera y aprovechando el código de @src/utils/modelado.py
````

## 2026-11-11 01:04:21 +0100 · Claude Code

- **Captura:** automática (hook)
- **Sesión:** 2ae22ad1

**Prompt literal**

````text
En @src/modelos_pablo.ipynb
````

**Modelo:** claude-opus-5-5 (versión de la herramienta: 2.1.319)

**Respuesta final**

````markdown
He añadido la función `ajustar_modelo` a [modelos_pablo.ipynb](src/modelos_pablo.ipynb), en una celda nueva al final del apartado 2. También he reescrito la celda de la logística para que la use. La he probado con Naive Bayes y funciona. No he ejecutado la rejilla completa de la logística porque con `saga` tarda: vuelve a ejecutar el notebook desde arriba.

## Qué hace

```python
busquedas, tabla = ajustar_modelo(nombre, modelo, parametros)
```

- **Recorre los tres balanceos** y monta cada pipeline con `mod.crear_pipeline`. La búsqueda la hace `mod.crear_busqueda`, así que la validación, la semilla y las métricas son las comunes del grupo.
- **Se salta los balanceos que el modelo no admite**, con el mismo `try/except` del apartado 2. Por ejemplo, `GaussianNB` no tiene `class_weight`.
- **Pone a las filas la misma etiqueta que en el apartado 2** (`logistica_smotenc`, `naive_bayes_sin_balanceo`…), así puedes comparar el modelo ajustado con el de por defecto.
- **Devuelve dos cosas:**
  - `busquedas`: un diccionario `etiqueta → GridSearchCV` ya entrenado, del que luego sacas el `best_estimator_` para test.
  - `tabla`: las `columnas` del apartado 2 más `mejores_parametros`, ordenada por F1 macro de validación.
- **No corta los parámetros en la tabla:** `pd.set_option("display.max_colwidth", None)` evita que pandas los recorte con «...».

Resultado de la prueba con Naive Bayes y una rejilla pequeña:

```
                          f1_macro_train  f1_macro_val  ...  mejores_parametros
naive_bayes_sin_balanceo           0.664         0.641  ...  {'modelo__var_smoothing': 1e-09}
naive_bayes_smotenc                0.633         0.602  ...  {'modelo__var_smoothing': 1e-09}
```

## Uso con los otros modelos

```python
busquedas_nb, tabla_nb = ajustar_modelo("naive_bayes", GaussianNB(), parametros_nb)
busquedas_hgb, tabla_hgb = ajustar_modelo(
    "hist_gradient_boosting", HistGradientBoostingClassifier(random_state=cte.semilla), parametros_hgb)
```

Dale a cada modelo sus propias variables (`busquedas_logistica`, `busquedas_nb`…) para que una rejilla no sobrescriba la anterior.

## Lo que tienes que saber para defenderla

- **Usa variables del notebook sin recibirlas como parámetro:** `X_train`, `y_train` y `columnas`. Necesita que estén definidas antes, así que funciona si ejecutas el notebook en orden.
- **`balanceos=balanceos` toma la lista del apartado 2.** Python la lee al crear la función, no en cada llamada.
- **Algunas celdas de prueba de debajo ya no funcionan:**
  - `busquedas.keys()`: ese diccionario ahora se llama `busquedas_logistica`.
  - `busqueda["logistica_sin_balanceo"]` y `modelos_por_defecto`: esos nombres no existen en el notebook.
  - El bucle de `evaluar_test`: también usa `busqueda` y `modelos_por_defecto`, y además mira el test, que solo debe usarse una vez al final. Conviene borrarlo o dejarlo para el último apartado.
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

---

## 2026-11-11 20:37:12 +0100 · Claude Code

- **Captura:** automática (hook)
- **Sesión:** 2ae22ad1

**Prompt literal**

````text
He decidido que voy a meter un dummy classifier dentro de la primera iteración de los valores por defecto, para probar que mis modelos lo superan. Pero me está dando un keyerror, ¿cómo lo podría solucionar?
````

**Modelo:** claude-opus-5-5 (versión de la herramienta: 2.1.322)

**Respuesta final**

````markdown
El `KeyError` venía de que el `if` del suelo envolvía también la creación del pipeline. Lo he corregido en la celda 2 de [modelos_pablo.ipynb](src/modelos_pablo.ipynb). No he vuelto a ejecutar la celda, así que vuelve a correrla para confirmarlo.

## Por qué daba `KeyError`

Tal como estaba, solo se creaba pipeline cuando el modelo era el suelo **y** tenía balanceo. Para los demás casos el `try` no se ejecutaba y `pipeline` se quedaba sin esa etiqueta. Pero la línea `busqueda_por_defecto[...] = ...pipeline[etiqueta]` está fuera del `if` y se ejecuta siempre. La primera vuelta es `logistica` sin balanceo, y por eso pedía `pipeline["logistica_sin_balanceo"]`, que no existía.

## Cambio

Ahora el `if` solo salta los casos que no quieres, y el `try` vuelve a su sitio:

```python
# el suelo solo se mide sin balanceo: siempre predice la clase mayoritaria, así que balancear no aporta nada
if nombre == "suelo" and balanceo is not None:
    continue
try:
    pipeline[etiqueta] = mod.crear_pipeline(modelo, balanceo)
except ValueError:
    ...
```

Sin el `if`, `class_weight` ya se saltaría solo, porque `DummyClassifier` no tiene ese parámetro y `crear_pipeline` lanza `ValueError`. Con SMOTENC, en cambio, sí se entrenaría. Como las clases quedan empatadas, `most_frequent` seguiría prediciendo la clase 0 y saldría una fila repetida. El `if` lo deja claro.

## Qué esperar del suelo

El suelo siempre predice «riesgo bajo», que es el 50 % de los pacientes:

| Métrica | Valor esperado | Por qué |
|---|---|---|
| F1 macro | ≈ 0,22 | 0,67 en la clase 0, 0 en las otras dos, dividido entre 3 |
| `recall_alto` | 0 | Nunca predice riesgo alto |
| `precision_alto` | 0 | Sale 0 y no da aviso, porque el scorer lleva `zero_division=0` |

`precision_macro` no lleva `zero_division`, así que verás avisos `UndefinedMetricWarning` al ajustar el suelo. Son normales: este modelo nunca predice las clases 1 y 2. Tus modelos tienen alrededor de 0,64 de F1 macro, así que lo superan con mucho margen. Con F1 macro ese suelo es muy fácil de batir, y es el valor que conviene citar en la memoria.
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

---

## 2026-11-11 20:45:23 +0100 · Claude Code

- **Captura:** automática (hook)
- **Sesión:** 2ae22ad1

**Prompt literal**

````text
<ide_opened_file>The user opened the file c:\Users\pablo\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\src\modelos_pablo.ipynb in the IDE. This may or may not be related to the current task.</ide_opened_file>
Okay, ya estoy con la comparación de modelos, ¿cómo podría generar una tabla de comparación siguiendo el criterio acordado en @docs/evolucion_planteamiento.md  : F1 macro y, si dos modelos quedan dentro de la desviación entre folds, el recall de riesgo alto?
````

**Modelo:** claude-opus-5-5 (versión de la herramienta: 2.1.322)

**Respuesta final**

````markdown
He añadido la tabla de comparación en la celda de la sección 6 de [modelos_pablo.ipynb](src/modelos_pablo.ipynb). No la he ejecutado, porque necesita las búsquedas de las secciones anteriores en memoria. Lo que sigue lo he calculado con los CSV que guardaste en `resultados/`.

## Cómo aplica el criterio

1. **Primero ordena por F1 macro** en validación.
2. **Marca como empatados** los modelos cuyo F1 queda dentro de la desviación entre folds del mejor, es decir, con F1 ≥ F1 del mejor − su desviación. La columna `empata_en_f1` lo indica.
3. **Entre los empatados, ordena por recall de riesgo alto.** Los que no empatan siguen ordenados por F1, y el suelo queda al final como referencia.

El texto previo a la tabla muestra el umbral, así puedes citar el número en la memoria.

## Qué va a salir

| Modelo | F1 macro val | Recall alto val | ¿Empata? |
|---|---|---|---|
| naive_bayes | 0,627 | **0,751** | sí |
| logistica | **0,651** ± 0,034 | 0,748 | sí |
| hist_gradient_boosting | 0,645 | 0,723 | sí |
| suelo | ≈ 0,22 | 0 | no |

El umbral es 0,651 − 0,034 = 0,617, así que **los tres empatan en F1** y, aplicando el criterio al pie de la letra, gana Naive Bayes.

## Un problema del criterio

Naive Bayes gana el desempate por solo 0,003 de recall (0,751 frente a 0,748). Esa diferencia es mucho menor que la desviación del recall, que es de 0,05-0,06. En los mismos folds, Naive Bayes saca más recall en 2, la logística en 1 y en otros 2 empatan:

| fold | logistica | naive_bayes | hgb |
|---|---|---|---|
| 0 | 0,722 | 0,722 | 0,694 |
| 1 | 0,767 | **0,781** | 0,753 |
| 2 | 0,667 | 0,667 | 0,681 |
| 3 | **0,847** | 0,819 | 0,722 |
| 4 | 0,736 | **0,764** | 0,764 |

Es decir, también empatan en recall, y el criterio acordado no dice qué hacer en ese caso. Tienes dos opciones:

- **Aplicar el criterio tal cual** y elegir Naive Bayes, reconociendo en la memoria que la diferencia de recall es ruido.
- **Proponer al grupo un tercer criterio** para cuando también empaten en recall. Por ejemplo, quedarse con el de mayor F1 (la logística), o con el más simple e interpretable, que también es la logística por sus coeficientes. Este cambio afecta a la comparación de todo el grupo, así que conviene acordarlo antes de cerrar la tabla final.

Para ver la tabla por folds en el notebook, puedes reutilizar tu función:

```python
por_fold({n: busquedas[n] for n in empatados.index}).round(3)
```
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

---

## 2026-11-11 20:57:10 +0100 · Claude Code

- **Captura:** automática (hook)
- **Sesión:** 2ae22ad1

**Prompt literal**

````text
<ide_opened_file>The user opened the file c:\Users\pablo\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\src\modelos_pablo.ipynb in the IDE. This may or may not be related to the current task.</ide_opened_file>
Okay, tengo en cuenta esa igualdad entre bayes y regresión logística, antes de decidir, me gustaría demostrar cuanto aporta la optimización de parámetros a cada uno de los modelos por defecto vs el modelo ajustado seleccionado en cada uno. Pero de nuevo tengo un keyerror.
````

**Modelo:** claude-opus-5-5 (versión de la herramienta: 2.1.322)

**Respuesta final**

````markdown
Era otra vez un problema de etiquetas. Lo he corregido en la celda de «¿Cuánto aporta el ajuste?» de [modelos_pablo.ipynb](src/modelos_pablo.ipynb). No he ejecutado la celda.

## Por qué daba `KeyError`

La celda buscaba `busqueda_por_defecto["logistica | class_weight"]`, con el formato de etiqueta que usabas antes. En el apartado 2 las claves se guardan como `f"{nombre}_{balanceo or 'sin_balanceo'}"`, es decir, `"logistica_class_weight"`. El cambio está en una sola línea:

```python
defecto = mod.tabla_resultados(busqueda_por_defecto[f"{nombre}_{balanceo}"], nombre).iloc[0]
```

`balanceo_elegido` nunca contiene `None`, así que no hace falta el `or 'sin_balanceo'`.

## Qué debería salir

Lo he sacado de las salidas que ya tienes en el apartado 2 y en cada sección:

| Modelo | F1 val: defecto → ajustado | Recall alto: defecto → ajustado | Sobreajuste: defecto → ajustado |
|---|---|---|---|
| logistica | 0,648 → 0,651 | 0,737 → 0,748 | 0,025 → 0,024 |
| naive_bayes | 0,602 → 0,627 | 0,734 → 0,751 | 0,031 → 0,023 |
| hist_gradient_boosting | 0,621 → 0,645 | 0,657 → 0,723 | 0,379 → 0,289 |

## Cómo leerlo

- **Logística:** el ajuste casi no aporta. Mejora el F1 en 0,003, muy por debajo de la desviación de 0,03. Cuadra con que la búsqueda eligiera L2 con `C = 0,1`, muy cerca de los valores por defecto (L2 y `C = 1`).
- **Naive Bayes:** el ajuste sí aporta, +0,025 de F1. Con SMOTENC, `var_smoothing` es lo que más importa.
- **HistGradientBoosting:** es donde más se nota. Sube el F1 y el recall de riesgo alto, y el sobreajuste baja de 0,38 a 0,29, aunque sigue siendo alto.

## Un matiz para la memoria

En la logística, la versión por defecto usa el solver `lbfgs` con `max_iter=100`, y la ajustada usa `saga` con `max_iter=5000`. Así que la diferencia no se debe solo a `C` y `l1_ratio`. Como apenas hay diferencia, no cambia la conclusión, pero conviene mencionarlo por si te preguntan en la entrevista.
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

---

## 2026-11-11 23:25:48 +0100 · Claude Code

- **Captura:** automática (hook)
- **Sesión:** 2ae22ad1

**Prompt literal**

````text
<ide_opened_file>The user opened the file c:\Users\pablo\Documents\master_ia_umu\machine_learning\practica\practica1\machine_learning\src\modelos_pablo.ipynb in the IDE. This may or may not be related to the current task.</ide_opened_file>
Okay, me gustaría refactorizar un poco la parte de comparación de mis modelos, para escribir los resultados en un csv y hacer esta última parte más eficiente
````

**Modelo:** claude-opus-5-5 (versión de la herramienta: 2.1.322)

**Respuesta final**

````markdown
He refactorizado la sección 6 de [modelos_pablo.ipynb](src/modelos_pablo.ipynb). Ahora hay una sola tabla `comparacion`, de la que salen todas las vistas, y la última celda la guarda en CSV. He comprobado la lógica de la tabla con datos simulados y cuadra. No he ejecutado el notebook, porque necesita las búsquedas en memoria: vuelve a ejecutar la sección 6 desde el principio.

## Fallo que he corregido

La celda de las matrices de confusión recorría `busquedas.items()`, que empieza por el suelo, con solo 3 ejes. Dibujaba suelo, logística y Naive Bayes, así que **HistGradientBoosting se quedaba sin matriz**. Revisa esa figura y la conclusión que escribiste a partir de ella. Ahora recorre `mis_modelos`.

## Qué hace cada celda

1. **Tabla de comparación:** define `balanceo_elegido`, `mis_modelos` y `busquedas` una sola vez. Antes `mis_modelos` se definía en la celda de las matrices, pero `por_fold(mis_modelos)` lo usaba antes, así que solo funcionaba si ejecutabas en desorden.
   - Junta los modelos ajustados con las columnas por defecto (`*_por_defecto`) y añade `mejora_f1_ajuste`.
   - Aplica tu criterio (`empata_en_f1`, `empata_en_recall`) sin cambiarlo y muestra las columnas del criterio.
2. **Celda de `por_fold`:** sin cambios. Ya funciona porque `mis_modelos` está definido antes.
3. **Cuánto aporta el ajuste:** ya no recalcula nada. Lee las columnas de la tabla que ya existe.
4. **Matrices de confusión:** además de dibujarlas, apunta en la tabla cuántos pacientes de riesgo alto clasifica como bajo (`alto_como_bajo`).
5. **Celda nueva:** guarda `resultados/comparacion_pablo.csv`.

## Dónde gana en eficiencia

La versión por defecto ya no se recalcula: se lee de la tabla `por_defecto` del apartado 2. El único entrenamiento que queda en la sección es el de `cross_val_predict` (5 folds por modelo), que hace falta para las matrices de confusión.

## El CSV

`resultados/comparacion_pablo.csv` lleva todo: train y validación con media ± desviación de todas las métricas, mejores parámetros, balanceo, valores por defecto, mejora, empates y `alto_como_bajo`. En el suelo, las columnas por defecto y `alto_como_bajo` quedan vacías, porque no se ajusta ni se dibuja su matriz.

He usado un nombre propio para no pisar los CSV por modelo (`logistica.csv`…) que lee el grupo, ni colisionar con los de Rodrigo (`arbol`, `knn`, `random_forest`). Si el grupo junta los resultados leyendo todos los CSV de la carpeta, este se colaría. Ahora mismo los lee por nombre, así que no pasa.
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

---
