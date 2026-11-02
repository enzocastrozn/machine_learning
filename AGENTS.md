# AGENTS.md

Instrucciones para cualquier agente de IA que trabaje en este repositorio (GitHub Copilot, Claude Code u otros). Responde en español. Los términos técnicos habituales se pueden dejar en inglés.

## Propósito del proyecto

Práctica 1 de Machine Learning del Máster en Inteligencia Artificial de la Universidad de Murcia (curso 2026/2027). Hay que clasificar a pacientes adultos en tres niveles de riesgo cardiovascular (0: bajo, 1: moderado, 2: alto) con una cohorte del Hospital Morales Meseguer: 2.254 pacientes, 27 variables de entrada y 1 objetivo.

La nota depende del proceso y de su justificación, no solo de la métrica final. Todos los miembros del grupo deben poder explicar todo el código en la entrevista.

## Documentos de referencia

Léelos antes de proponer decisiones sobre el trabajo o la entrega:

- [Enunciado y diccionario de variables](docs/enunciado/enunciado_riesgo_cardiovascular.md)
- [Instrucciones y entregables](docs/enunciado/instrucciones_entrega.md)
- [Cómo funciona el registro de IA](docs/ia/GUIA_REGISTRO_IA.md)

Estos documentos son transcripciones. Si hay dudas sobre un requisito, avisa de que manda el PDF oficial.

## Registro obligatorio de prompts

La práctica se suspende si falta transparencia en el uso de la IA, así que **este registro es obligatorio en cada petición**.

1. **Identifica a la persona** con `git config user.name` y usa su archivo:

   | Si el nombre o el correo de git contiene | Archivo |
   |---|---|
   | `pablo` | `docs/ia/registro_ia_pablo.md` |
   | `enzo` | `docs/ia/registro_ia_enzo.md` |
   | `rodri` | `docs/ia/registro_ia_rodrigo.md` |

   Si no coincide con nadie, pregunta a quién corresponde el registro.
2. **Al empezar a trabajar en una petición,** lee el final del archivo. Si la última entrada ya contiene ese prompt con `Captura: automática (hook)`, la herramienta lo está registrando sola y no debes añadir nada. Si no, añade una entrada al final con la [plantilla](docs/ia/GUIA_REGISTRO_IA.md#plantilla-de-una-entrada) y copia el prompt **literalmente**, sin resumirlo ni corregirlo.
3. **Al terminar, si has creado tú la entrada,** complétala con el modelo y la versión que estés usando y con tu mensaje final. Si no sabes el modelo, escribe `no disponible`: no lo deduzcas.
4. **Deja `Análisis crítico` como pendiente.** Solo lo rellena la persona: no inventes qué se aceptó o se rechazó.
5. No edites entradas anteriores ni registros de otros miembros, y no copies contraseñas, tokens ni otros secretos.
6. Si tu modo de trabajo no permite editar archivos, recuérdale a la persona que copie el prompt y la respuesta a mano.

## Entorno

- Python **3.12** y **uv** para todo el grupo. Las dependencias están en `pyproject.toml` y `uv.lock`.
- Para añadir o quitar librerías, usa `uv add` o `uv remove`, nunca `pip install` ni `uv pip install`. No edites `uv.lock` a mano.
- Cada vez que cambien las librerías, regenera `requirements.txt` y súbelo en el mismo commit que `pyproject.toml` y `uv.lock`:

  ```bash
  uv export --format requirements-txt --no-hashes --no-dev -o requirements.txt
  ```

- Ejecuta con `uv run` o con el `.venv` del proyecto. No cambies la versión de Python sin que el grupo lo haya decidido.

## Reglas metodológicas

- Usa una única semilla y un único esquema de validación para todos los modelos y fíjalos en un solo sitio. Comparar modelos con esquemas o semillas distintos invalida la comparación.
- El conjunto de test se usa una sola vez, al final. Nada se ajusta mirándolo.
- Todo lo que se aprende de los datos (imputación, escalado, remuestreo, selección de variables) va dentro de un `Pipeline` y se ajusta solo con el train.
- Mínimos del enunciado: 3 técnicas de preprocesamiento, 2 modelos base, 3 ensembles, 3 métricas con la crítica justificada clínicamente y ajuste de hiperparámetros en todos los modelos.
- Analiza el sobreajuste de todos los modelos comparando train y validación con media ± desviación.
- Justifica cada decisión y anota también las opciones que se descartan y por qué.
- Encontrar las problemáticas del dataset forma parte de la tarea: no las des por sabidas, compruébalas con los datos.

## Forma de trabajar

- Explica el código que propongas y comenta los bloques: quien lo usa debe poder defenderlo línea a línea.
- Cada commit debe hacerlo su autor desde su cuenta, con un mensaje descriptivo. No hagas commits ni push si no te lo piden.
- Evita los cambios masivos: la profesora audita el historial y penaliza subirlo todo al final.
- No subas datos nuevos ni archivos personales sin avisar: el repositorio es público.

## Fechas (comunicadas en clase)

| Fecha | Hito |
|---|---|
| 3 de noviembre de 2026 | Repositorio creado |
| 15 de noviembre de 2026 | Entrega de la memoria y del informe de uso de IA |
| 18 de noviembre de 2026, por la mañana | Entrega del vídeo |
| 18 y 19 de noviembre de 2026 | Entrevistas, con todos los miembros |
