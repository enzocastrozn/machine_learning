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
---
