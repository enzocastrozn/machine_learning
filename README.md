# Predicción Multiclase de Riesgo Cardiovascular en Población Adulta

Práctica 1 de Machine Learning · Máster en Inteligencia Artificial · Universidad de Murcia · Curso 2026/2027

| Autores | GitHub |
|---|---|
| Enzo Castro | [enzocastrozn](https://github.com/enzocastrozn) |
| Rodrigo | [Rodri17013](https://github.com/Rodri17013) |
| Pablo Sánchez Mérida | [pablo-sanchez](https://github.com/pablo-sanchez) |

## Índice

- [Descripción del proyecto](#descripción-del-proyecto)
- [Estructura del repositorio](#estructura-del-repositorio)
- [Reproducir el proyecto (profesorado)](#reproducir-el-proyecto-profesorado)
- [Guía para el equipo](#guía-para-el-equipo)
  - [Instalar uv](#instalar-uv)
  - [Preparar el proyecto](#preparar-el-proyecto)
  - [Windows y Linux / WSL: qué cambia](#windows-y-linux--wsl-qué-cambia)
  - [Sincronizarse con el equipo](#sincronizarse-con-el-equipo)
  - [Añadir o quitar librerías](#añadir-o-quitar-librerías)
  - [Archivos del entorno](#archivos-del-entorno)
- [Registro de uso de IA](#registro-de-uso-de-ia)
- [Solución de problemas](#solución-de-problemas)
- [Actualizar requirements.txt](#)

## Descripción del proyecto

Las enfermedades cardiovasculares son una de las principales causas de morbimortalidad en el mundo, y detectar pronto el nivel de riesgo de cada persona permite adaptar la prevención y aprovechar mejor los recursos sanitarios.

Este proyecto desarrolla y compara modelos de machine learning que clasifican a pacientes adultos en tres niveles de riesgo cardiovascular:

| Clase | Riesgo |
|---|---|
| 0 | Bajo |
| 1 | Moderado |
| 2 | Alto |

Los datos son una cohorte clínica del Hospital Morales Meseguer, con 2.254 pacientes, 27 variables de entrada sociodemográficas, clínicas, analíticas y de estilo de vida y 1 variable objetivo.

La práctica pide:

- Un análisis exploratorio que identifique las problemáticas del dataset y al menos 3 técnicas de preprocesamiento para resolverlas.
- Al menos 2 modelos base y 3 ensembles, con ajuste de hiperparámetros en todos.
- Un esquema de validación que evalúe todas las combinaciones de preprocesamiento y modelo, con al menos 3 métricas y la más crítica justificada clínicamente.
- Conclusiones razonadas sobre el mejor modelo y, de forma opcional, test estadísticos.

Los requisitos completos están en el [enunciado](docs/enunciado/enunciado_riesgo_cardiovascular.md) y en las [instrucciones de entrega](docs/enunciado/instrucciones_entrega.md).

## Estructura del repositorio

```text
machine_learning/
├── data/
│   └── enfermedad_cardiovascular.csv    # Dataset de la práctica
├── docs/
│   ├── enunciado/                       # Enunciado e instrucciones en Markdown
│   ├── ia/                              # Registros individuales de uso de IA
│   └── memoria.tex                      # Memoria técnica
├── scripts/
│   └── registrar_prompt_ia.py           # Guarda los prompts en el registro de IA
├── src/
│   └── practica1_riesgo_cardiovascular.ipynb    # Notebook principal
├── .claude/settings.json                # Hooks del registro de IA en Claude Code
├── .gitattributes                       # Saltos de línea comunes en todos los sistemas
├── .python-version                      # Versión de Python del proyecto
├── AGENTS.md                            # Instrucciones para agentes de IA
├── pyproject.toml                       # Dependencias que declara el proyecto
├── requirements.txt                     # Versiones exactas, para instalar con pip
└── uv.lock                              # Versiones exactas, para instalar con uv
```

## Reproducir el proyecto (profesorado)

Instalación probada con **Python 3.12** en Windows 11 y en Ubuntu 24.04 (WSL). Se puede hacer con uv o sin él, y las dos opciones instalan las mismas versiones.

```bash
git clone https://github.com/enzocastrozn/machine_learning.git
cd machine_learning
```

### Opción A: con uv

No hace falta tener Python 3.12: uv lo descarga si no lo encuentra. Estos comandos valen en Windows, Linux y WSL.

```bash
uv sync --locked
uv run jupyter lab
```

### Opción B: sin uv

Hace falta tener Python 3.12 instalado.

**Windows (PowerShell):**

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
jupyter lab
```

**Linux o WSL:**

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter lab
```

En Ubuntu, si `venv` da error, instala antes el paquete que falta: `sudo apt install python3.12-venv`.

### Ejecutar el notebook

Abre [`src/practica1_riesgo_cardiovascular.ipynb`](src/practica1_riesgo_cardiovascular.ipynb) y ejecuta todas las celdas en orden.

## Guía para el equipo

Usamos [uv](https://docs.astral.sh/uv/), el gestor de proyectos y paquetes de Python de Astral, escrito en Rust. Instala la versión de Python indicada, crea el entorno y deja a todo el grupo con las mismas versiones exactas de cada librería, en cualquier sistema.

**Todo el grupo trabaja con Python 3.12.** La regla básica es: usa `uv add` para las librerías, nunca `pip install`, y ejecuta `uv sync` después de cada `git pull`.

### Instalar uv

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Linux o WSL:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc
```

Después comprueba la instalación y actualízala. Si instalaste uv con otro método, como `winget`, actualízalo con ese mismo método.

```bash
uv --version
uv self update
```

En WSL hay que instalarlo aparte: el uv de Windows no sirve dentro de Linux.

### Preparar el proyecto

```bash
git clone https://github.com/enzocastrozn/machine_learning.git
cd machine_learning
uv sync
```

`uv sync` descarga Python 3.12 si hace falta, crea `.venv` e instala las versiones de `uv.lock`. No ejecutes `uv init`: el proyecto ya está creado.

Para ejecutar notebooks en VS Code, abre la carpeta `machine_learning` como raíz y elige **Select Kernel → Python Environments → `.venv`**.

### Windows y Linux / WSL: qué cambia

Los comandos de uv son iguales en todos los sistemas. Solo cambia lo siguiente:

| | Windows (PowerShell) | Linux / WSL (Bash) |
|---|---|---|
| Activar el entorno | `.venv\Scripts\Activate.ps1` | `source .venv/bin/activate` |
| Desactivar el entorno | `deactivate` | `deactivate` |
| Borrar el entorno | `Remove-Item -Recurse -Force .venv` | `rm -rf .venv` |

No hace falta activar el entorno si antepones `uv run`, por ejemplo `uv run python script.py`.

**Si trabajas en WSL:**

1. Clona el repositorio dentro de Linux (por ejemplo, en `~/proyectos/`), no en `/mnt/c/...`: es mucho más rápido.
2. No compartas `.venv` entre Windows y WSL, porque cada `uv sync` rompería el entorno del otro sistema. Si usas los dos, ten un clon en cada uno.
3. Configura git también en WSL, con el correo de tu cuenta de GitHub. Si no, tus commits no aparecerán como tuyos, y la profesora audita el historial de cada miembro:

   ```bash
   git config --global user.name "Tu nombre"
   git config --global user.email "correo-de-tu-cuenta-de-github"
   ```

4. Abre el proyecto en VS Code con `code .` desde la terminal de WSL, con la extensión WSL instalada.

### Sincronizarse con el equipo

#### Primera vez: pasar a Python 3.12

Hazlo una sola vez, cuando este cambio esté en `main`. Antes, sube o guarda en una rama lo que tengas sin terminar.

```bash
git switch main
git pull
uv self update
uv sync
uv run python --version    # Debe mostrar Python 3.12.x
```

`uv sync` sustituye por sí solo un `.venv` con otra versión de Python. Después:

1. Borra cualquier otro entorno que creases para esta práctica, como `venv312`.
2. Vuelve a seleccionar en VS Code el kernel `.venv` del proyecto.
3. Si tienes una rama abierta, actualízala:

   ```bash
   git switch mi-rama
   git merge main
   uv sync
   ```

#### Día a día

```bash
# Antes de empezar
git switch main
git pull
uv sync

# Crea una rama para cada tarea
git switch -c nombre/tema

# Durante el trabajo: commits pequeños y descriptivos, desde tu cuenta
git add <archivos>
git commit -m "Añade el análisis de valores nulos"
git push -u origin nombre/tema
```

Después, abre un pull request hacia `main` en GitHub. Para traer a tu rama lo que hayan subido los demás:

```bash
git switch main
git pull
git switch nombre/tema
git merge main
uv sync
```

**Haz `uv sync` después de cada `pull` o `merge`,** y reinicia el kernel del notebook si han cambiado las librerías.

#### Conflicto en `uv.lock`

Ocurre si dos personas añaden librerías a la vez. No lo arregles a mano. Resuelve primero el conflicto de `pyproject.toml`, conservando las librerías de ambos, y después regenera el resto:

```bash
git checkout --theirs uv.lock
uv lock
uv export --format requirements-txt --no-hashes --no-dev -o requirements.txt
git add pyproject.toml uv.lock requirements.txt
git commit
```

### Añadir o quitar librerías

```bash
uv add xgboost      # O bien: uv remove xgboost
uv export --format requirements-txt --no-hashes --no-dev -o requirements.txt
git add pyproject.toml uv.lock requirements.txt
git commit -m "Añade xgboost para los modelos de boosting"
```

Sube siempre esos tres archivos juntos. `requirements.txt` es obligatorio en la entrega, y es lo que usa quien no tiene uv.

No uses `pip install` ni `uv pip install`: la librería no quedaría registrada, tus compañeros no la tendrían y el siguiente `uv sync` la desinstalaría.

### Archivos del entorno

| Archivo | Qué es | ¿Se sube a git? |
|---|---|---|
| `pyproject.toml` | Versión de Python admitida y librerías que pide el proyecto | **Sí** |
| `uv.lock` | Versiones exactas de todos los paquetes, para todos los sistemas. No se edita a mano | **Sí** |
| `.python-version` | Versión de Python con la que uv crea `.venv` | **Sí** |
| `requirements.txt` | Las mismas versiones, para instalar con pip. Se genera con `uv export` | **Sí** |
| `.venv/` | El entorno instalado. Se puede borrar y recrear con `uv sync` | **No** |

## Registro de uso de IA

La práctica exige declarar los prompts, las herramientas y un análisis crítico de las respuestas. Cada miembro tiene su registro en [`docs/ia/`](docs/ia/GUIA_REGISTRO_IA.md):

- **Con Claude Code,** se rellena solo mediante un hook.
- **Con GitHub Copilot en modo agente,** lo rellena el agente siguiendo [`AGENTS.md`](AGENTS.md).
- **En chats web o en modo pregunta,** se copia a mano.

Los detalles, la plantilla y lo que debe revisar cada persona antes de hacer commit están en la [guía del registro](docs/ia/GUIA_REGISTRO_IA.md).

## Solución de problemas

| Problema | Causa probable | Solución |
|---|---|---|
| `uv` no se reconoce | La terminal se abrió antes de instalarlo | Abre otra terminal y reinicia VS Code |
| `ModuleNotFoundError` tras un `git pull` | Alguien ha añadido una librería | Ejecuta `uv sync` y reinicia el kernel |
| Un compañero no tiene una librería que tú sí | Se instaló con `pip` o `uv pip install` | Añádela con `uv add` y sube los tres archivos |
| `uv sync --locked` falla | `uv.lock` no coincide con `pyproject.toml` | Ejecuta `uv lock` y sube el resultado |
| Aviso de uv sobre `VIRTUAL_ENV` | Hay otro entorno activo, por ejemplo de conda | Es inofensivo. Para quitarlo, desactiva ese entorno |
| `Activate.ps1 cannot be loaded` | Política de ejecución de PowerShell | Usa `uv run` o ejecuta `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| El notebook usa otro Python | Kernel equivocado | Elige **Select Kernel → `.venv`** con la carpeta del proyecto abierta como raíz |
| En WSL, el `.venv` se rompe al usar Windows | Los dos sistemas comparten carpeta | Ten un clon en cada sistema |
| Tus commits de WSL no salen en tu perfil | git en WSL no tiene tu correo de GitHub | Configura `user.email` dentro de WSL |
| Algo sigue fallando en el entorno | `.venv` en mal estado | Borra `.venv` y ejecuta `uv sync` |

## Actualizar requirements

En esta primera iteración, vamos a dejar un requirements.txt preliminar para tenerlo presente, sin embargo, es probable que las versiones del entorno evolucionen con el desarrollo, y en el día a día no lo actualizaremos. Pero hay que tener presente que al final del desarrollo lo tendremos que hacer con:

```bash
uv export --format requirements-txt --no-hashes --no-dev -o requirements.txt

```