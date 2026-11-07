# Registro de uso de IA · Rodrigo

Cómo funciona este registro: [docs/ia/GUIA_REGISTRO_IA.md](GUIA_REGISTRO_IA.md).

## Herramientas empleadas

| Herramienta | Versión | Modelo | Entorno |
|---|---|---|---|
| _Por completar_ | | | |

## Prompts

> **Nota:** el hook de registro automático no se llegó a ejecutar, así que los 4 primeros prompts (29 y 30 de octubre de 2026) no se guardaron en su momento. Se añadieron el 3 de noviembre de 2026 copiando del historial de la conversación de Claude Code el texto literal de cada prompt y de cada respuesta. La hora es la que muestra el chat de Claude Code junto a cada respuesta. No incluye segundos, así que puede diferir en uno o dos minutos del envío del prompt. No hay constancia del modelo que respondió esos prompts.

## 2026-10-29 18:17 +0100 · Claude Code

- **Captura:** manual, añadida el 2026-11-03 a partir del historial de la conversación; hora tomada del chat de Claude Code, sin segundos

**Prompt literal**

````text
cómo puedo hacer que al usar describe no se corte la tabla?
````

**Modelo:** no disponible

**Respuesta final**

````markdown
Por defecto pandas oculta columnas (y filas) cuando la tabla es ancha y pone `...` en medio. Para mostrarla entera, sube los límites de visualización antes de llamar a `describe()`:

```python
import pandas as pd

pd.set_option('display.max_columns', None)   # todas las columnas
pd.set_option('display.width', None)         # no partir la tabla en varias líneas
pd.set_option('display.max_colwidth', None)  # no recortar el texto de las celdas

df.describe()
```

Si lo pones en la celda de imports al principio del notebook, se aplica a todas las tablas.

Si solo lo quieres para esa celda:

```python
with pd.option_context('display.max_columns', None, 'display.width', None):
    display(df.describe())
```

Otra opción, cuando hay muchas columnas, es transponer la tabla para que cada variable salga en una fila. Así se lee mejor y no se corta a lo ancho:

```python
df.describe().T
```

Si lo que se corta son las filas, añade también `pd.set_option('display.max_rows', None)`.
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

---

## 2026-10-29 18:18 +0100 · Claude Code

- **Captura:** manual, añadida el 2026-11-03 a partir del historial de la conversación; hora tomada del chat de Claude Code, sin segundos

**Prompt literal**

````text
otra pregunta, en clase nos han comentado tener cuidado con los duplicados, pero revisando los notebooks de la asignatura no lo encuentro, cómo podría comprobar si hay y quitarlos?
````

**Modelo:** no disponible

**Respuesta final**

````markdown
Con pandas se hace con `duplicated()` para detectarlos y `drop_duplicates()` para quitarlos.

**Comprobar si hay**

```python
# Número de filas duplicadas (idénticas en todas las columnas)
df.duplicated().sum()

# Ver las filas duplicadas, incluida la primera aparición de cada una
df[df.duplicated(keep=False)]
```

**Quitarlos**

```python
print("Antes:", df.shape)
df = df.drop_duplicates().reset_index(drop=True)
print("Después:", df.shape)
```

Por defecto se queda la primera aparición de cada fila repetida (`keep='first'`).

**Si el dataset tiene una columna `id`**

Si cada fila tiene un identificador único, `df.duplicated()` nunca va a encontrar nada, porque el `id` hace que todas las filas sean distintas. En ese caso compara todas las columnas menos el `id`:

```python
cols = df.columns.drop('id')
df.duplicated(subset=cols).sum()
df = df.drop_duplicates(subset=cols).reset_index(drop=True)
```

También conviene comprobar que el `id` no se repite: `df['id'].duplicated().sum()`.

**Por qué importa**

Quita los duplicados antes de separar en train y test. Si no, una misma fila puede acabar en los dos conjuntos. El modelo la habrá "visto" al entrenar y la métrica de test saldrá más alta de lo que es en realidad (es una forma de *data leakage*). Te recomiendo poner en el notebook cuántos duplicados había y cuántas filas quedan, para que se vea que lo has revisado.
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

---

## 2026-10-29 18:21 +0100 · Claude Code

- **Captura:** manual, añadida el 2026-11-03 a partir del historial de la conversación; hora tomada del chat de Claude Code, sin segundos

**Prompt literal**

El prompt incluía una captura de pantalla de la salida de `df.info()` del notebook, cortada por VS Code entre las columnas 19 y 26. La imagen no se conserva en este registro. El texto del prompt era:

````text
pese a usar describe.T, se corta
````

**Modelo:** no disponible

**Respuesta final**

````markdown
Esa salida es de `df.info()`, no de `describe()`. Y el corte no lo hace pandas, lo hace VS Code. `info()` saca texto plano, y VS Code limita las salidas de texto de los notebooks a 30 líneas por defecto: enseña el principio y el final y pone `...` en medio. Por eso desaparecen las columnas 20 a 25.

**Solución: subir el límite en VS Code**

1. Abre la configuración con `Ctrl + ,`.
2. Busca `notebook.output.textLineLimit`.
3. Cámbialo de 30 a un número mayor, por ejemplo 200.

También puedes añadirlo directamente al `settings.json`:

```json
"notebook.output.textLineLimit": 200,
"notebook.output.scrolling": true
```

Con `scrolling` activado, las salidas largas salen en un recuadro con barra de desplazamiento en vez de ocupar toda la pantalla. Después vuelve a ejecutar la celda.

Si no quieres tocar la configuración, al pie de la salida cortada suele aparecer un enlace *"Output is truncated. View as a scrollable element or open in a text editor"* que también la muestra entera.

**Sobre `describe()`**

`df.describe().T` se muestra como tabla HTML, así que a ese límite no le afecta. Pero por defecto solo incluye las columnas numéricas, y en tu caso hay 3 columnas de texto (`str`), como `antecedentes_familiares_tipo`. Para verlas:

```python
df.describe(include='all').T          # todas juntas
df.describe(include='object').T       # solo las categóricas: count, unique, top, freq
```

Por cierto, en tu `info()` ya se ven valores nulos en `colesterol_ldl`, `glucosa_ayunas`, `horas_sueno_diarias` y `proteina_c_reactiva`. Puedes sacar el resumen con `df.isna().sum()`.
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

---

## 2026-10-30 17:42 +0100 · Claude Code

- **Captura:** manual, añadida el 2026-11-03 a partir del historial de la conversación; hora tomada del chat de Claude Code, sin segundos

**Prompt literal**

````text
por qué obtengo este error? cómo lo soluciono? 

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[4], line 1
----> 1 count_classes = pd.value_counts(riesgo_cardiovascular, sort = True)
      2 count_classes.plot(kind = 'bar', rot=0)
      3 
      4 datos['riesgo_cardiovascular'].value_counts()

AttributeError: module 'pandas' has no attribute 'value_counts'
````

**Modelo:** no disponible

**Respuesta final**

````markdown
`pd.value_counts()` era una función de pandas que se marcó como obsoleta en la versión 2.1 y se eliminó en pandas 3.0. Tú tienes pandas 3 (se nota en que `info()` muestra el tipo `str`, que es nuevo de esa versión). El código del notebook de clase está escrito para una versión anterior.

Ahora `value_counts()` se llama como método de la propia columna:

```python
count_classes = datos['riesgo_cardiovascular'].value_counts(sort=True)
count_classes.plot(kind='bar', rot=0)
```

Fíjate también en que `riesgo_cardiovascular` a secas no existe como variable, a no ser que la hayas creado tú antes. Aunque arreglaras lo de `pd.`, te daría un `NameError`. Por eso uso `datos['riesgo_cardiovascular']`.

Si además quieres ver los números y el porcentaje de cada clase (útil para saber si las clases están desbalanceadas):

```python
datos['riesgo_cardiovascular'].value_counts()
datos['riesgo_cardiovascular'].value_counts(normalize=True)  # proporciones
```

Si otras celdas copiadas de los notebooks de clase fallan con un `AttributeError` parecido, probablemente sea el mismo problema: algo que existía en pandas 1.x o 2.x y se quitó en la 3.
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

---

## 2026-11-03 18:21:28 +0100 · Claude Code

- **Captura:** manual

**Prompt literal**

````text
estoy pensando ahora en buscar valores anómalos o que no tengan mucho sentido, una de las condiciones que se me había ocurrido era esta: (datos['edad'] < 18).sum(), con qué más variables podría hacerlo?
````

**Modelo:** Claude Opus 5.5 (claude-opus-5-5)

**Respuesta final**

````markdown
Buena idea. Puedes hacer tres tipos de comprobación, y el diccionario de variables del enunciado te sirve de guía para cada una.

**1. Valores fuera de un rango posible**

Es lo mismo que con `edad`, pero con un rango para cada variable. Los límites de abajo son orientativos y amplios a propósito: buscan valores imposibles o casi, no valores simplemente altos. Antes de ponerlos en la memoria, contrástalos con alguna fuente clínica.

```python
# Rangos fisiológicamente plausibles (orientativos: hay que justificarlos en la memoria)
rangos = {
    'edad': (18, 110),                     # la cohorte es de adultos
    'presion_sistolica': (60, 260),        # mmHg
    'presion_diastolica': (30, 160),       # mmHg
    'colesterol_total': (50, 600),         # mg/dL
    'colesterol_hdl': (5, 150),            # mg/dL
    'colesterol_ldl': (10, 400),           # mg/dL
    'trigliceridos': (20, 3000),           # mg/dL
    'glucosa_ayunas': (30, 600),           # mg/dL
    'indice_masa_corporal': (12, 70),      # kg/m²
    'frecuencia_cardiaca_reposo': (30, 200),  # lpm
    'horas_sueno_diarias': (0, 24),        # un día tiene 24 horas
    'consumo_alcohol_semanal': (0, 200),   # unidades, no puede ser negativo
    'anos_fumador': (0, 90),
    'proteina_c_reactiva': (0, 500),       # mg/L
    'acido_urico': (1, 20),                # mg/dL
    'clearance_creatinina': (5, 200),      # mL/min
    'frecuencia_ejercicio_semanal': (0, 7),   # días de la semana
    'perimetro_cintura': (40, 200),        # cm
    'hemoglobina_glicosilada': (3, 20),    # %
}

# Para cada variable, cuántos valores caen fuera de su rango (los NaN no cuentan)
fuera = {col: ((datos[col] < lo) | (datos[col] > hi)).sum()
         for col, (lo, hi) in rangos.items()}
pd.Series(fuera).sort_values(ascending=False)
```

Para ver los casos concretos de una variable: `datos.loc[datos['presion_sistolica'] > 260, 'presion_sistolica']`.

**2. Valores que no encajan con el tipo de variable**

- `edad` va en años cumplidos y `frecuencia_ejercicio_semanal` en días a la semana, así que las dos deberían ser enteras. En tu `info()` salen como `float64` y sin nulos, así que conviene comprobar si tienen decimales:
  ```python
  (datos['edad'] % 1 != 0).sum()
  (datos['frecuencia_ejercicio_semanal'] % 1 != 0).sum()
  ```
- Las booleanas solo pueden valer 0 o 1, y el objetivo solo 0, 1 o 2:
  ```python
  booleanas = ['fumador_actual', 'hipertension_previa', 'diabetes_mellitus',
               'tratamiento_estatinas', 'uso_antihipertensivos']
  (~datos[booleanas].isin([0, 1])).sum()
  datos['riesgo_cardiovascular'].value_counts()
  ```
- Las categóricas solo deberían tener los 4 valores del diccionario. Busca erratas, mayúsculas distintas o espacios de más:
  ```python
  for col in ['tipo_alimentacion', 'nivel_actividad', 'antecedentes_familiares_tipo']:
      print(datos[col].value_counts(dropna=False), '\n')
  ```

**3. Combinaciones incoherentes entre variables**

A veces cada valor es posible por separado, pero la combinación no:

```python
# Cada condición marca las filas cuyos valores no tienen sentido juntos
incoherencias = {
    'sistólica <= diastólica': datos['presion_sistolica'] <= datos['presion_diastolica'],
    'HDL + LDL > colesterol total': datos['colesterol_hdl'] + datos['colesterol_ldl'] > datos['colesterol_total'],
    'años fumando > edad': datos['anos_fumador'] > datos['edad'],
    'fumador actual con 0 años fumando': (datos['fumador_actual'] == 1) & (datos['anos_fumador'] == 0),
    'sedentario que hace ejercicio 5+ días': (datos['nivel_actividad'] == 'Sedentario') & (datos['frecuencia_ejercicio_semanal'] >= 5),
}
pd.Series({nombre: cond.sum() for nombre, cond in incoherencias.items()})
```

El colesterol total es la suma de HDL, LDL y VLDL, así que HDL + LDL no debería superarlo (dejando algo de margen por el error de medida). En `años fumando > edad` puedes ser más estricto y comparar con `edad - 10`, porque nadie fuma desde que nace.

Otras combinaciones son raras pero **no** son errores. No conviene tocarlas, aunque sí comentarlas:
- `diabetes_mellitus == 0` con glucosa ≥ 126 o HbA1c ≥ 6,5 %: puede ser una diabetes sin diagnosticar.
- `uso_antihipertensivos == 1` con `hipertension_previa == 0`: algunos de esos fármacos se recetan por otros motivos.

**Qué hacer después**

Distingue entre valores imposibles y valores extremos pero posibles:

- **Imposibles:** en vez de borrar la fila entera, conviértelos en `NaN` (`datos.loc[condicion, col] = np.nan`) para que se imputen después dentro del `Pipeline`. Esta conversión es una regla fija que no aprende nada de los datos, así que puedes hacerla antes de separar train y test.
- **Extremos posibles** (por ejemplo, una PCR muy alta): son información clínica real. Mejor no quitarlos y tenerlos en cuenta al elegir el escalado.

He añadido este prompt a mano en [docs/ia/registro_ia_rodrigo.md](docs/ia/registro_ia_rodrigo.md) porque el hook no lo había guardado. Puede que se arregle reiniciando la sesión y aceptando la confianza en el proyecto. El `Análisis crítico` tienes que rellenarlo tú.
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

---

## 2026-11-03 18:24:41 +0100 · Claude Code

- **Captura:** manual

**Prompt literal**

````text
puedes añadir al documento de ia que no se registro nuestros prompt anteriores?
````

**Modelo:** Claude Opus 5.5 (claude-opus-5-5)

**Respuesta final**

````markdown
He añadido una nota al principio de la sección `Prompts` de [registro_ia_rodrigo.md](docs/ia/registro_ia_rodrigo.md). Dice que los 4 prompts anteriores, del 29 de octubre al 3 de noviembre, no se registraron, y resume de qué trataban. No he tocado la entrada que ya había. Este prompt también lo he registrado a mano, porque el hook sigue sin guardar nada.

Si quieres, puedo añadir esos 4 prompts con su texto literal y mis respuestas, porque siguen en esta conversación. Así el informe de IA quedaría completo.
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

---

## 2026-11-03 18:25:32 +0100 · Claude Code

- **Captura:** manual

**Prompt literal**

````text
registralos no solo resumen
````

**Modelo:** Claude Opus 5.5 (claude-opus-5-5)

**Respuesta final**

````markdown
He añadido a [registro_ia_rodrigo.md](docs/ia/registro_ia_rodrigo.md) los 4 prompts anteriores con su texto literal y mis respuestas completas, copiados del historial de la conversación. Están antes de la entrada de las 18:21, para que el registro siga en orden cronológico. También he cambiado la nota para explicar que esas entradas se añadieron más tarde.

Las propias entradas indican tres cosas que no se pueden recuperar:
- **La hora:** solo se sabe el día. Los tres primeros prompts son del 29 de octubre y el cuarto, del 30.
- **El modelo:** he puesto `no disponible`, porque no puedo comprobar que fuera el mismo que ahora.
- **La captura de pantalla del tercer prompt:** el registro la describe, pero no incluye la imagen.

Además, he corregido un error de la nota anterior: decía que los prompts iban del 29 de octubre al 3 de noviembre, pero son del 29 y el 30 de octubre. Este prompt también está registrado.
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

---

## 2026-11-03 18:28:06 +0100 · Claude Code

- **Captura:** manual

**Prompt literal**

````text
hoy es 3 de noviembre
````

**Modelo:** Claude Opus 5.5 (claude-opus-5-5)

**Respuesta final**

````markdown
Sí, hoy es 3 de noviembre, y las entradas de hoy (18:21, 18:24, 18:25 y esta) llevan esa fecha.

Las fechas de los 4 prompts anteriores (29 y 30 de octubre) no me las he inventado: son las que tenía la sesión de Claude Code cuando los enviaste. El repositorio también encaja con esas fechas. En esos prompts el notebook estaba en `notebooks/practica1_riesgo_cardiovascular.ipynb`. Esa ruta ya no existe: ahora está en `src/riesgo_cardiovascular.ipynb`, y `src/` tiene archivos creados el 1 y el 2 de noviembre.

Si de verdad enviaste esos prompts hoy, dímelo y cambio las fechas. Si te referías a otra cosa, dime qué quieres corregir.
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

---

## 2026-11-03 19:12:55 +0100 · Claude Code

- **Captura:** manual

**Prompt literal**

````text
te pego el chat para que registres las horas de los que no se registraron automáticamente: 

[omitido: transcripción pegada del chat de Claude Code de esta misma conversación, desde el prompt «cómo puedo hacer que al usar describe no se corte la tabla?» hasta la respuesta de las 18:28. Incluye las horas de cada respuesta y las llamadas a herramientas. Los prompts y respuestas que contiene ya están en las entradas anteriores de este registro.]
````

**Modelo:** Claude Opus 5.5 (claude-opus-5-5)

**Respuesta final**

````markdown
He añadido a las 4 entradas reconstruidas las horas del chat que me has pegado:

| Prompt | Fecha y hora |
|---|---|
| `describe` se corta | 29/10/2026, 18:17 |
| Duplicados | 29/10/2026, 18:18 |
| `describe.T` se sigue cortando | 29/10/2026, 18:21 |
| Error de `pd.value_counts` | 30/10/2026, 17:42 |

Hay dos cosas que he anotado también en las entradas y en la nota del principio:
- **Precisión:** el chat muestra la hora junto a cada respuesta y sin segundos, así que puede diferir uno o dos minutos del momento en que enviaste el prompt.
- **Fecha:** el chat no muestra el día. He dejado la fecha que registró la sesión, y tu transcripción la confirma: justo después del prompt de `pd.value_counts` pone «Idle 3d 23h», es decir, casi 4 días sin actividad antes de los prompts de hoy.

En la entrada de este prompt he copiado tu mensaje, pero no la transcripción pegada, porque es muy larga y repite las entradas que ya están en el registro. En su lugar hay una marca `[omitido: …]` que explica qué contenía. Si prefieres que esté entera para que sea literal del todo, dímelo y la añado.
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

---

## 2026-11-06 17:07:31 +0100 · Claude Code

- **Captura:** manual

**Prompt literal**

````text
Para seguir con el analisis, quiero hacer una matriz de correlación, sé que se hace con .corr, pero qué opciones podría meterle? Cuáles pueden convenir más?
````

**Modelo:** Claude Opus 5.5 (claude-opus-5-5)

**Respuesta final**

````markdown
`DataFrame.corr()` tiene tres parámetros:

| Parámetro | Valores | Para qué sirve |
|---|---|---|
| `method` | `'pearson'` (por defecto), `'spearman'`, `'kendall'` o una función propia | Tipo de correlación |
| `numeric_only` | `False` (por defecto) o `True` | Usar solo las columnas numéricas |
| `min_periods` | un entero | Mínimo de pares sin `NaN` para calcular cada valor |

**`method`: el que más importa**

- **Pearson** mide relaciones *lineales*. Le afectan mucho los valores extremos y las distribuciones asimétricas.
- **Spearman** aplica Pearson a los rangos (la posición de cada valor una vez ordenados), así que mide relaciones *monótonas*: si una variable sube, la otra tiende a subir (o a bajar), aunque no sea en línea recta. Aguanta mejor los outliers y la asimetría.
- **Kendall** también usa rangos y es todavía más robusto, pero es más lento y suele dar valores más pequeños en valor absoluto, así que cuesta compararlo con los otros dos. Con 2.254 filas, Spearman suele ser suficiente.

¿Cuál te conviene? En datos clínicos es habitual que variables como los triglicéridos, la PCR o el consumo de alcohol estén sesgadas y tengan valores extremos. Además, el objetivo (0, 1, 2) es ordinal. Las dos cosas favorecen a **Spearman**. Eso sí, compruébalo con tus datos (histogramas, `datos.skew()`) antes de afirmarlo en la memoria. Lo mejor es calcular Pearson y Spearman: si para un par de variables dan valores muy distintos, es una pista de que hay outliers o una relación no lineal.

**`numeric_only=True`: en tu caso, casi obligatorio**

Tienes 3 columnas de texto. En pandas 3, si no lo pones, `corr()` da error al intentar convertir `'Mediterránea'` en un número.

**`min_periods`**

`corr()` calcula cada par solo con las filas en las que ninguna de las dos variables es `NaN`. Con tus nulos no hace falta tocarlo. Solo serviría si alguna variable tuviera muchísimos.

**Qué variables entran y cuáles no**

- Las booleanas (0/1) sí. La correlación de Pearson entre una variable binaria y una continua equivale a la correlación punto-biserial, así que tiene sentido.
- Las categóricas nominales, como `tipo_alimentacion`, no. No tienen orden, así que la correlación no significa nada aunque las codifiques como 0, 1, 2, 3. Para relacionarlas con el objetivo se usa una tabla de contingencia (`pd.crosstab`) con chi-cuadrado o la V de Cramér.
- `nivel_actividad` sí tiene orden (de Sedentario a Muy activo). Si la codificas respetándolo, puedes meterla con Spearman.

**Código**

```python
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Correlación de Spearman entre todas las variables numéricas (incluye booleanas y objetivo)
corr = datos.corr(method='spearman', numeric_only=True)

# Máscara para ocultar el triángulo superior, que repite el inferior
mascara = np.triu(np.ones_like(corr, dtype=bool))

plt.figure(figsize=(16, 13))
sns.heatmap(corr, mask=mascara, cmap='coolwarm', vmin=-1, vmax=1, center=0,
            annot=True, fmt='.2f', annot_kws={'size': 7}, square=True)
plt.title('Matriz de correlación (Spearman)')
plt.tight_layout()
plt.show()
```

- `vmin=-1, vmax=1, center=0` fijan la escala de colores: el blanco siempre es 0 y puedes comparar los colores entre gráficos.
- Con 25 variables, los números salen pequeños. Si molestan, quita `annot=True` y mira los valores en las tablas de abajo.

Estas dos tablas se leen mejor que el mapa de calor:

```python
# Correlación de cada variable con el objetivo, ordenada por valor absoluto
corr['riesgo_cardiovascular'].drop('riesgo_cardiovascular').sort_values(key=abs, ascending=False)

# Pares de variables de entrada muy correlacionadas entre sí (posible redundancia)
entradas = corr.drop(index='riesgo_cardiovascular', columns='riesgo_cardiovascular')
inferior = np.tril(np.ones_like(entradas, dtype=bool), k=-1)  # triángulo inferior, sin la diagonal
pares = entradas.where(inferior).stack().dropna()  # en pandas 3, stack() no quita los NaN solo
pares[pares.abs() > 0.7].sort_values(key=abs, ascending=False)
```

El umbral de 0,7 es una convención habitual, no una regla fija.

**Cómo interpretarla**

- Si una variable tiene una correlación alta con el objetivo, es informativa. Pero que la tenga baja no basta para descartarla: Pearson y Spearman solo detectan relaciones monótonas, y los modelos de árboles pueden aprovechar otro tipo de relaciones e interacciones.
- Si dos variables de entrada están muy correlacionadas, aportan información parecida (multicolinealidad). Afecta sobre todo a los modelos lineales, como la regresión logística: sus coeficientes se vuelven inestables y difíciles de interpretar. A los ensembles de árboles les afecta mucho menos.
- Para explorar y describir el dataset puedes usar todos los datos. Pero si usas la correlación para decidir qué variables quitar, esa decisión aprende de los datos y, según [AGENTS.md](AGENTS.md), tiene que tomarse solo con el train o dentro del `Pipeline`.

He registrado este prompt a mano en [docs/ia/registro_ia_rodrigo.md](docs/ia/registro_ia_rodrigo.md), porque el hook sigue sin guardar nada.
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

---

## 2026-11-07 11:28:38 +0100 · Claude Code

- **Captura:** manual

**Prompt literal**

````text
mi compañero ha hecho eda tmb en una rama aparte, la rama es pablo/eda-clinico, puedes revisarlo y ver si se puede usar algo para mi eda o en el caso de ser conveptos muy diferentes, dejarlo por separado?
````

**Modelo:** Claude Opus 5.5 (claude-opus-5-5)

**Respuesta final**

````markdown
He revisado `pablo/eda-clinico`. Pablo no ha tocado tu notebook: su trabajo está en otro archivo, `src/eda_clinico.ipynb`, que solo existe en su rama. Así que no hay conflictos de git.

**Recomendación:** no son conceptos tan distintos. Los dos estáis haciendo el EDA, pero cada uno ha profundizado en una parte, así que se complementan bastante. Aun así, yo no copiaría ahora su código en tu notebook: duplicaría trabajo y, como la profesora audita el historial, quedaría como tuyo algo que hizo él. Mantened los notebooks separados por ahora y decidid en la reunión cómo juntarlos. Él mismo termina con una tabla de «conclusiones abiertas para la reunión».

**Qué aporta Pablo que tú no tienes**

| Parte | Qué hace | Cómo te sirve |
|---|---|---|
| 4.1 Categóricas frente al riesgo | Porcentaje de cada clase de riesgo por categoría (`pd.crosstab`) | Es lo que te faltaba para las variables de texto, que no entran en la correlación, y justifica la codificación |
| 4.2 Binarias frente al riesgo | Media de cada binaria por clase | Pone números a tus countplots |
| 5.1 y 5.2 Nulos | Test chi-cuadrado para ver si que falte el dato depende del riesgo (todos los p > 0,05) | Respalda con un test tu frase de la 1.5: «no parece que la aparición de datos nulos dependa del tipo de paciente» |
| 5.3 Experimento de imputación | Oculta valores conocidos, los rellena con media, mediana, KNN e Iterative y mide el error en 30 sorteos | Es una prueba mucho más sólida para la fila «Valores faltantes» de tu tabla 1.8, donde dices que kNN aportaría poco |
| 5.4 Distribución antes y después de imputar | Compara media, mediana y desviación típica | Lo pidieron en clase y no lo tienes |

**Qué aportas tú que él no tiene**

Todo el análisis de calidad de datos (1.6): valores negativos e imposibles, incoherencias entre variables, decimales en variables que deberían ser enteras y valores repetidos que parecen nulos camuflados. También las distribuciones (1.3), la matriz de correlación completa (1.7) y la tabla resumen de problemáticas (1.8).

**En qué no coincidís (para la reunión)**

1. **Pablo ha analizado los nulos sobre los datos sin limpiar, y eso cambia sus resultados.** Tú propones pasar a `NaN` los valores imposibles y los repetidos sospechosos. Si lo hacéis, habrá nulos en bastantes más variables que las 4 actuales (`presion_sistolica`, `colesterol_total`, `trigliceridos`, `acido_urico`, `colesterol_hdl`, `indice_masa_corporal`…), y habrá que repetir su experimento, porque cambian los pacientes completos y los porcentajes de nulos. Por ejemplo, en la comprobación de Friedewald cuenta los pacientes con triglicéridos ≥ 400, y tú has visto que 452,7 es uno de los valores repetidos sospechosos: parte de ese recuento sale de datos que vais a tratar como nulos. Seguramente su conclusión se mantenga (no usar Friedewald e imputar con la mediana), pero hay que recalcular los números después de limpiar.
2. **`antecedentes_familiares_tipo`:** tú propones one-hot, y Pablo, dos binarias (`antecedente_materno` y `antecedente_paterno`, con «Ambos» = 1 y 1). Sus datos apoyan esta opción: el riesgo alto pasa del 12 % (ninguno) al 22 % (materno), al 28 % (paterno) y al 40 % (ambos), casi la suma de los dos efectos. Además, genera 2 columnas en vez de 4. Podéis elegir una o probar las dos y compararlas en validación.
3. **Trabajo repetido:** la distribución de clases y la correlación de Spearman con el objetivo aparecen en los dos notebooks, con los mismos resultados (alcohol 0,39, etc.). En la versión final deberían salir una sola vez.

En lo demás coincidís: imputar con la mediana dentro del `Pipeline`, no eliminar filas con nulos, codificación ordinal para `nivel_actividad`, particiones estratificadas y el recall de la clase de riesgo alto como métrica clave.

**Un cambio que sí te recomiendo hacer ya**

Pablo toma la semilla de [src/utils/constantes.py](src/utils/constantes.py), y tú escribes `semilla=42` en el notebook. AGENTS.md pide fijarla en un solo sitio, así que cambia tu celda de imports para usar el mismo módulo:

```python
import utils.constantes as cte

np.random.seed(cte.semilla)
```

Y en el resto del notebook, usa `cte.semilla` donde haga falta una semilla.

**Sobre tus cambios guardados**

Al cambiar a la rama de Pablo, GitHub Desktop guardó tus cambios sin commit en un stash, y al volver a `rodrigo/eda` no los restauró. Ya están restaurados (el notebook y la entrada del registro del 6 de noviembre). Para que no vuelva a pasar, haz commit antes de cambiar de rama o mira la rama del otro en GitHub desde el navegador.

He registrado este prompt a mano en [docs/ia/registro_ia_rodrigo.md](docs/ia/registro_ia_rodrigo.md).
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

---

## 2026-11-07 11:32:56 +0100 · Claude Code

- **Captura:** manual

**Prompt literal**

````text
entonces ahora tengo sus cambios tmb?
````

**Modelo:** Claude Opus 5.5 (claude-opus-5-5)

**Respuesta final**

````markdown
No. Tu rama `rodrigo/eda` no tiene nada de Pablo. Lo he comprobado: su commit no está en tu rama y en `src/` no aparece su `eda_clinico.ipynb`.

- **Su rama la he leído, no la he copiado.** Saqué su notebook con `git show` a una carpeta temporal fuera del repositorio, solo para revisarlo. No he hecho merge ni he copiado nada a tu rama.
- **Lo que restauré del stash eran tus propios cambios.** GitHub Desktop los guardó al cambiar de rama: tu notebook `src/riesgo_cardiovascular.ipynb` y tu registro de IA. No tienen nada de Pablo.

Ahora mismo tienes esos dos archivos modificados y sin commit, como estaban antes de cambiar de rama.

Si en la reunión decidís juntar los dos EDA, lo normal es que Pablo abra un pull request de su rama, o que hagáis merge de las dos ramas en una común. Así cada parte queda en el historial con su autor.
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

---

## 2026-11-07 11:58:03 +0100 · Claude Code

- **Captura:** manual

**Prompt literal**

````text
podrías hacer tu el merge de su eda al mío para que sea así más limpio y en el casod e conflcitos los resuelvas y ya tener una versión unificada?
````

**Modelo:** Claude Opus 5.5 (claude-opus-5-5)

**Respuesta final**

````markdown
Hecho. He hecho el merge de `origin/pablo/eda-clinico` en tu rama `rodrigo/eda`, con el commit `c052238` («Merge del EDA clínico de Pablo (pablo/eda-clinico) en rodrigo/eda»).

- **No ha habido conflictos.** La rama de Pablo solo trae dos archivos suyos, `src/eda_clinico.ipynb` y `docs/ia/registro_ia_pablo.md`, y ninguno coincide con los tuyos.
- **La autoría se mantiene.** El commit de Pablo entra en tu rama con su nombre, así que en el historial se ve qué hizo cada uno.
- **Tus cambios sin commit siguen intactos:** `src/riesgo_cardiovascular.ipynb` y tu registro de IA.
- **No he hecho push.** El merge solo está en tu equipo. Cuando quieras subirlo, haz primero commit de tus cambios y luego push desde GitHub Desktop.

**Lo que el merge no hace:** no junta los dos notebooks en uno. Ahora tu rama tiene los dos EDA uno al lado del otro: `src/riesgo_cardiovascular.ipynb` (el tuyo) y `src/eda_clinico.ipynb` (el de Pablo). Convertirlos en un único notebook ya no es cosa de git, sino de decidir el contenido, y hay dos puntos en los que no coincidís:

1. El análisis de nulos de Pablo se hizo antes de limpiar los valores anómalos que encontraste tú, así que hay que repetirlo con los datos limpios.
2. Tú propones one-hot para `antecedentes_familiares_tipo`, y él, dos binarias.

Si quieres, puedo preparar un notebook unificado con tu análisis de calidad de datos (1.2-1.7), sus apartados de categóricas, binarias e imputación y una sola tabla de problemáticas, y dejar marcados esos dos puntos como pendientes de la reunión. Para el historial quedaría más limpio hacerlo después de la reunión, con esos dos puntos ya decididos.

Un detalle menor para Pablo: su notebook importa `scipy` (`chi2_contingency`), que no está en `pyproject.toml`. Ahora funciona porque viene instalado con scikit-learn, pero lo correcto sería añadirlo con `uv add scipy`.
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

---

## 2026-11-07 12:00:59 +0100 · Claude Code

- **Captura:** manual

**Prompt literal**

````text
lo que quiero es unificar, tomando lo mejor de ambos
````

**Modelo:** Claude Opus 5.5 (claude-opus-5-5)

**Respuesta final**

````markdown
Hecho. El EDA unificado está en [src/riesgo_cardiovascular.ipynb](src/riesgo_cardiovascular.ipynb). Lo he ejecutado entero y no da ningún error (tarda 1 min 20 s).

**Antes de nada: no guardes el notebook desde la pestaña que tengas abierta.** Hoy VS Code ya sobrescribió tu notebook con una versión antigua: a las 11:57 guardó encima la versión del último commit, y desaparecieron tu sección de correlaciones y la tabla resumen. Las he recuperado del stash, que seguía en git. Si tienes el notebook abierto, ciérralo sin guardar (o usa *Revert File*) y vuelve a abrirlo. Si no, puede volver a pasar.

**Estructura**

| Apartado | Origen |
|---|---|
| 1.1-1.2 Carga y descripción | Rodrigo |
| 1.3 Tipos de variables (listas que usa todo el notebook) | Pablo |
| 1.4 Variable objetivo | Tus gráficos y el razonamiento de Pablo sobre el recall de la clase de riesgo alto |
| 1.5 Distribuciones | Tus gráficos y las tablas de Pablo: medianas por clase y binarias y categóricas frente al riesgo, con sus hipótesis |
| 1.6-1.8 Nulos, calidad de datos y correlaciones | Rodrigo |
| 1.9 Limpieza de errores de registro | **Nuevo:** aplica las reglas que proponías en tu tabla resumen |
| 1.10 Tratamiento de nulos | Pablo, repetido sobre los datos limpios |
| 1.11 Resumen y decisiones para la reunión | Tu tabla con la evidencia de Pablo, y su tabla de preguntas abiertas |

He quitado lo repetido (la distribución de clases y la correlación con el objetivo salían dos veces) y he unificado los nombres (`datos` y las listas de variables de Pablo). La semilla ahora sale de `utils/constantes.py`.

**Qué cambia al repetir el análisis de Pablo con los datos limpios**

- Los 54 pacientes con triglicéridos ≥ 400 que, según Pablo, impedían aplicar Friedewald eran justo el valor camuflado 452,7. Con los datos limpios no queda ninguno. Aun así, Friedewald falla más que la mediana (47,4 frente a 29,5 mg/dL de error), así que se descarta igual.
- Ahora hay nulos en 11 variables en vez de 4, y el 39 % de los pacientes tiene alguno (antes, el 24 %).
- Su conclusión se mantiene: la mediana iguala o mejora a KNN e Iterative en todas las variables.
- Hay una excepción aparente en el chi-cuadrado: en `colesterol_hdl`, 3 de sus 4 nulos son de riesgo alto (p = 0,018). He escrito que no es fiable, porque son solo 4 casos y esos nulos los creó la limpieza. Es una interpretación mía, revísala.

**Una corrección en tu parte**

En «Observaciones» decías que en las variables de texto había categorías nuevas, pero la salida de la 1.7 muestra solo las 4 del diccionario en cada variable. Lo he corregido.

**Lo que te toca revisar o decidir**

- La 1.9 aplica tus reglas tal como las escribiste en la tabla. Comprueba que es lo que querías. Por ejemplo, en las presiones incoherentes anulo las dos, porque no se sabe cuál está mal.
- `antecedentes_familiares_tipo` (dos binarias u one-hot) queda pendiente para la reunión, igual que el resto de la tabla final.
- [src/eda_clinico.ipynb](src/eda_clinico.ipynb) sigue ahí, sin tocar. Su contenido ya está en el unificado, pero si se borra o no lo decidís con Pablo.
- El notebook importa `scipy`, que no está en `pyproject.toml`. Funciona porque lo instala scikit-learn, pero lo correcto es `uv add scipy` y regenerar `requirements.txt`.
- No he hecho commit. En la entrevista os pueden preguntar por cualquier parte, así que repasa la 1.9 y la 1.10 antes de subirlo. En el mensaje del commit, indica que incluye el trabajo de Pablo.

Si hay que volver atrás, tu versión completa de antes de unificar está en `C:\Users\rodma\AppData\Local\Temp\claude\3c6d5242b56aed6d\6209e179-4546-4d3b-819e-becedaa5ce97\scratchpad\rodrigo_stash.ipynb`.

He registrado este prompt a mano en [docs/ia/registro_ia_rodrigo.md](docs/ia/registro_ia_rodrigo.md).
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

---
