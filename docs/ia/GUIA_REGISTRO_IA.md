# Registro de uso de IA

La práctica exige declarar el uso de la IA con la transcripción literal de los prompts, las herramientas y versiones empleadas y un análisis crítico de las respuestas. Cualquier falta de transparencia implica no superarla ([instrucciones, apartado 4.3](../enunciado/instrucciones_entrega.md#43-documento-de-uso-ético-y-responsable-de-inteligencia-artificial)).

Cada miembro tiene su propio archivo, así que nadie pisa el trabajo de los demás ni aparecen conflictos de git:

- [Pablo](registro_ia_pablo.md)
- [Enzo](registro_ia_enzo.md)
- [Rodrigo](registro_ia_rodrigo.md)

## Qué tiene que hacer cada persona

| Herramienta | Cómo se registra | Qué tienes que hacer |
|---|---|---|
| **Claude Code** | Automático: un hook guarda cada prompt, el modelo y la respuesta final | Abrir el repositorio como carpeta raíz y aceptar la confianza en el proyecto la primera vez |
| **GitHub Copilot, modo agente** | El agente sigue la regla de [`AGENTS.md`](../../AGENTS.md) y escribe la entrada | Comprobar en la primera petición que se ha creado la entrada |
| **GitHub Copilot, modo pregunta** o **chats web** (ChatGPT, Claude.ai…) | A mano | Copiar el prompt y la respuesta con la [plantilla](#plantilla-de-una-entrada) |

Además, cada persona debe:

1. Tener en git su nombre o correo reales, porque así se elige el archivo (`git config user.name`). Debe contener `pablo`, `enzo` o `rodri`.
2. Rellenar la tabla de herramientas de su registro, con modelos y versiones.
3. Rellenar `Análisis crítico` en los prompts relevantes: qué se aceptó, qué se rechazó por errores, alucinaciones o ineficiencias y cómo se corrigió. Ni el hook ni el agente lo rellenan.
4. **Revisar el registro antes de cada commit.** El repositorio es público y el archivo contiene todo lo que escribes al agente: elimina contraseñas, tokens o datos personales. Si quitas algo, indícalo con `[retirado: motivo]` para mantener la transparencia.
5. Hacer commit del registro junto con el trabajo al que corresponde.

## Qué es un hook

Un hook es un comando que la propia herramienta ejecuta en un momento concreto, sin pasar por el modelo. Aquí, [`.claude/settings.json`](../../.claude/settings.json) ejecuta [`scripts/registrar_prompt_ia.py`](../../scripts/registrar_prompt_ia.py) al enviar un prompt y al terminar la respuesta. Por eso no depende de que el agente se acuerde.

Las instrucciones de `AGENTS.md`, en cambio, las lee y sigue el modelo, así que pueden fallar alguna vez. Por eso conviene revisarlas si no usas Claude Code.

Copilot también tiene hooks, pero siguen en preview y su documentación avisa de que no garantizan compatibilidad con los de Claude Code. Aún no los usamos: el registro con Copilot se apoya en `AGENTS.md`.

```markdown
@AGENTS.md
```

## Plantilla de una entrada

Añade cada entrada al final de tu archivo:

`````markdown
## AAAA-MM-DD HH:MM:SS +ZZZZ · Herramienta

- **Captura:** manual

**Prompt literal**

````text
Copia aquí el prompt, sin cambiar nada.
````

**Modelo:** nombre y versión

**Respuesta final**

````markdown
Copia aquí el mensaje final del agente.
````

**Análisis crítico:** _pendiente (qué se aceptó, qué se rechazó y cómo se corrigió)_

---
`````

## Del registro al informe final

El informe de uso de IA se entrega en PDF, uno por grupo, el 15 de noviembre. Se elabora a partir de estos tres archivos, con la tabla de herramientas de cada uno, los prompts principales y su análisis crítico.
