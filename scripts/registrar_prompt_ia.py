"""Añade prompts y respuestas al registro individual de IA (docs/ia/registro_ia_<persona>.md).

Lo ejecutan los hooks de .claude/settings.json, que pasan por stdin el JSON de cada evento.
Solo usa la biblioteca estándar. No escribe nada en stdout: Claude Code lo añadiría a su contexto.
"""
import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]

# Fragmento del nombre o correo de git -> sufijo del archivo de registro.
PERSONAS = {"pablo": "pablo", "enzo": "enzo", "rodri": "rodrigo"}


def persona_actual():
    forzada = os.environ.get("REGISTRO_IA_PERSONA")
    if forzada:
        return forzada
    identidad = ""
    for clave in ("user.name", "user.email"):
        salida = subprocess.run(["git", "-C", str(RAIZ), "config", clave], capture_output=True, text=True)
        identidad += " " + salida.stdout.lower()
    for fragmento, persona in PERSONAS.items():
        if fragmento in identidad:
            return persona
    return None


def bloque_literal(texto, lenguaje):
    # La valla es más larga que cualquier secuencia de comillas del texto, para no romper el Markdown.
    mayor = max((len(m) for m in re.findall(r"`+", texto)), default=0)
    valla = "`" * max(4, mayor + 1)
    return f"{valla}{lenguaje}\n{texto}\n{valla}\n"


def entrada_prompt(datos, herramienta):
    fecha = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z")
    sesion = str(datos.get("session_id", "desconocida"))[:8]
    return (
        f"\n## {fecha} · {herramienta}\n\n"
        f"- **Captura:** automática (hook)\n"
        f"- **Sesión:** {sesion}\n\n"
        f"**Prompt literal**\n\n{bloque_literal(datos['prompt'], 'text')}"
    )


def modelo_y_version(ruta_transcripcion):
    """Busca el último modelo usado en la transcripción de la sesión."""
    if not ruta_transcripcion or not Path(ruta_transcripcion).exists():
        return "no disponible"
    lineas = Path(ruta_transcripcion).read_text(encoding="utf-8", errors="replace").splitlines()
    for linea in reversed(lineas):
        try:
            registro = json.loads(linea)
        except json.JSONDecodeError:
            continue
        mensaje = registro.get("message")
        modelo = mensaje.get("model") if isinstance(mensaje, dict) else None
        if modelo and not modelo.startswith("<"):
            version = registro.get("version")
            return f"{modelo} (versión de la herramienta: {version})" if version else modelo
    return "no disponible"


def entrada_respuesta(datos):
    respuesta = datos.get("last_assistant_message") or "(no disponible)"
    return (
        f"\n**Modelo:** {modelo_y_version(datos.get('transcript_path'))}\n\n"
        f"**Respuesta final**\n\n{bloque_literal(respuesta, 'markdown')}\n"
        f"**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_\n\n---\n"
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--herramienta", default="Claude Code")
    args = parser.parse_args()

    datos = json.loads(sys.stdin.buffer.read().decode("utf-8"))
    persona = persona_actual()
    if persona is None:
        print("registro IA: la identidad de git no coincide con ningún miembro; no se registra", file=sys.stderr)
        return

    if datos.get("hook_event_name") == "Stop":
        entrada = entrada_respuesta(datos)
    elif "prompt" in datos:
        entrada = entrada_prompt(datos, args.herramienta)
    else:
        return

    registro = RAIZ / "docs" / "ia" / f"registro_ia_{persona}.md"
    with registro.open("a", encoding="utf-8", newline="\n") as archivo:
        archivo.write(entrada)


if __name__ == "__main__":
    main()
