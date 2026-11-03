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
