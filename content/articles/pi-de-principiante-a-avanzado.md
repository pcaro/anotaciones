---
title: Pi de novato a avanzado — La guía completa
slug: pi-de-principiante-a-avanzado
lang: es
date: 2026-05-21
category: ia
tags: pi, coding-agent, guia, tutorial, cli, terminal
series: Pi: el agente de código
series_index: 2
featured_image: /images/pi-aprendizaje.jpg
Summary: Guía completa de pi: desde la instalación y primeros pasos hasta sesiones en árbol, branching, skills, extensiones, y trucos de power user.
---

Esta es la segunda entrega de la serie sobre [pi, el agente de código](https://pi.dev/). En la [primera parte](https://pablocaro.es/que-es-pi-coding-agent) comparé pi con otros coding agents. Ahora toca ponerse manos a la obra: desde la instalación hasta trucos de power user, pasando por sesiones, branching, skills y extensiones.

![Pi de novato a avanzado](/images/pi-aprendizaje.jpg)

## Nivel 1: Novato — Primeros pasos

### Instalación

Pi es un paquete npm. La forma más rápida:

```bash
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
```

O con el instalador oficial (Linux/macOS):

```bash
curl -fsSL https://pi.dev/install.sh | sh
```

Windows requiere WSL o Git Bash. Más detalles en la [documentación](https://pi.dev/docs/latest/windows).

### Autenticación

Arranca pi en el directorio de tu proyecto:

```bash
cd /ruta/a/tu/proyecto
pi
```

La primera vez verás la pantalla de bienvenida. Usa `/login` para elegir un proveedor:

- **Suscripciones**: Claude Pro/Max, ChatGPT Plus/Pro o GitHub Copilot.
- **API keys**: Anthropic, OpenAI, DeepSeek, Groq, Mistral, Google, OpenRouter, Azure, Bedrock...

También puedes pasar la API key como variable de entorno:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
pi
```

Yo, personalmente, tengo todas mis API keys almacenadas en Bitwarden y uso [kitty rbw](https://pablocaro.es/rbw-env-exportar-variables) para cargarlas automáticamente al abrir el terminal. Así las claves están disponibles sin tener que escribirlas a mano cada vez.

### Tu primer prompt

Ya dentro de pi, escribe algo y pulsa Enter:

```
Explícame este repositorio y dime cómo ejecutar sus tests.
```

Por defecto, pi tiene cuatro herramientas: `read`, `write`, `edit` y `bash`. Con eso ya puedes hacer prácticamente cualquier cosa.

### Archivos de contexto (AGENTS.md)

Pi carga `AGENTS.md` o `CLAUDE.md` al arrancar. Es la forma de darle instrucciones globales a tu agente. Crea un archivo en la raíz de tu proyecto:

```markdown
# Instrucciones del proyecto

- Ejecuta `npm run check` después de cada cambio de código.
- No ejecutes migraciones en producción localmente.
- Mantén las respuestas concisas.
```

Pi busca estos archivos en:
- `~/.pi/agent/AGENTS.md` — instrucciones globales
- Subiendo desde el directorio actual hasta la raíz
- El directorio actual

Después de modificar un archivo de contexto —o de instalar o cambiar una extensión— ejecuta `/reload` para que pi lo recoja sin reiniciar.

### Referenciar archivos con @

Usa `@` en el editor para buscar archivos con fuzzy-search:

```
@README.md "Resume esto"
@src/app.ts @src/app.test.ts "Revisa estos juntos"
```

También puedes pasar imágenes pegadas con Ctrl+V.

## Nivel 2: Intermedio — Navegación y productividad

### Atajos de teclado essenciales

| Atajo | Acción |
|---|---|
| Ctrl+L | Seleccionar modelo |
| Ctrl+P | Ciclar entre modelos rápido |
| Shift+Tab | Cambiar nivel de thinking |
| Ctrl+G | Abrir editor externo (VS Code, vim...) |
| Ctrl+V | Pegar imagen en el prompt |

### Bash desde la TUI

Pi ejecuta comandos Bash sin salir de la interfaz:

- **`!comando`** — Ejecuta y envía la salida al LLM.
- **`!!comando`** — Ejecuta de forma local *sin* enviar la salida al LLM (útil para comandos silenciosos como `git status`).

Esta distinción es muy útil: `!` para cuando quieres que el agente vea el resultado de un comando y reaccione, `!!` para cosas que solo necesitas tú como `git status` sin añadir ruido al contexto.

```text
!npm run lint
!!git status
```

### La barra de estado

En la parte inferior de pi verás:

- Directorio de trabajo actual
- Nombre de la sesión
- Uso de tokens y caché
- Coste acumulado
- Porcentaje de contexto usado
- Modelo activo

### Cola de mensajes

Puedes enviar mensajes mientras el agente está trabajando:

- **Enter** — Encola un mensaje de steering (se envía cuando termina la ronda actual de tool calls).
- **Alt+Enter** — Encola un follow-up (se envía cuando el agente termina todo el trabajo).
- **Escape** — Cancela y restaura los mensajes encolados al editor.

### Sesiones y branching

Esta es una de las funcionalidades más potentes y exclusivas de pi.

Las sesiones se guardan automáticamente en `~/.pi/agent/sessions/`. Puedes reanudarlas con:

```bash
pi -c                  # Continuar la sesión más reciente
pi -r                  # Navegar y seleccionar sesiones anteriores
pi --session <path|id> # Abrir una sesión específica
```

Dentro de pi:

- **`/session`** — Muestra info de la sesión actual (archivo, ID, tokens, coste).
- **`/tree`** — Navega el árbol de la sesión. Puedes saltar a cualquier punto anterior y continuar desde ahí, creando una rama alternativa sin perder el progreso previo.
- **`/fork`** — Crea una nueva sesión desde un mensaje de usuario anterior.
- **`/clone`** — Duplica la rama activa en un nuevo archivo de sesión.
- **`/compact`** — Resumir mensajes antiguos para liberar contexto.
- **`/resume`** — Explorar sesiones anteriores.
- **`/name <nombre>`** — Poner nombre a la sesión para encontrarla después.

El branching con `/tree` es una funcionalidad que distingue a pi de cualquier otro agente de código cerrado. Puedes tener varias líneas de exploración en el mismo archivo de sesión, y si abandonas una rama, pi puede resumirla automáticamente para no perder el contexto.

### Intercambio rápido de modelos

Usa `Ctrl+P` para ciclar entre modelos rápidamente. Configura tu selección con `--models`:

```bash
pi --models "claude-*,gpt-4o,deepseek-*"
```

O en `settings.json`:

```json
{
  "defaultProvider": "opencode-go",
  "defaultModel": "deepseek-v4-flash",
  "defaultThinkingLevel": "high"
}
```

### Mensajes de sistema

Puedes reemplazar o extender el prompt de sistema por defecto:

- **`~/.pi/agent/SYSTEM.md`** — Reemplaza globalmente.
- **`.pi/SYSTEM.md`** — Reemplaza por proyecto.
- **`~/.pi/agent/APPEND_SYSTEM.md`** — Añade al final sin reemplazar.
- **`.pi/APPEND_SYSTEM.md`** — Añade por proyecto.

## Nivel 3: Avanzado — Skills, templates y extensiones

### Skills

Los skills son archivos Markdown con frontmatter que se inyectan en el contexto del agente. Son la forma más sencilla de enseñar a pi comportamientos reutilizables.

[Ya comparé ambos métodos](https://pablocaro.es/instalando-skills-de-github) en detalle, pero por resumir: puedes instalarlos con `npx skills` (mi método preferido) o `gh skill`:

```bash
# Instalar skills de Matt Pocock
npx skills add mattpocock/skills --skill grill-me --skill tdd

# Buscar skills disponibles
npx skills find
```

También puedes crear tus propios skills. Un skill es un archivo `SKILL.md` con frontmatter:

```markdown
---
name: my-skill
description: Una skill de ejemplo
---

Esta es mi skill personalizada. Cuando el usuario la invoque con /skill:my-skill,
este contenido se inyecta en el contexto del agente.
```

Los skills se guardan en `~/.pi/agent/skills/` (global) o `.pi/skills/` (proyecto). [Ya escribí sobre cómo instalarlos](https://pablocaro.es/instalando-skills-de-github).

### Prompt templates

Son comandos personalizados con barra `/`. Crea un archivo Markdown en `.pi/prompts/` o `~/.pi/agent/prompts/`:

```markdown
---
name: review-pr
description: Revisa un PR y deja comentarios en GitHub
---

Review this PR and leave inline comments on GitHub using `gh`. Check for:
- Breaking changes
- Missing error handling
- Test coverage
- Consistency with project conventions
```

Después de `/reload`, puedes usar `/review-pr` y el contenido se expandirá en el editor.

### Extensiones (pi packages)

Las extensiones son módulos TypeScript que pueden registrar herramientas, interceptar eventos, mostrar UI personalizada, y mucho más. Es lo que diferencia a pi de cualquier otro agente.

```bash
# Instalar paquetes
pi install npm:@aliou/pi-linkup       # Búsqueda web
pi install npm:@aliou/pi-processes    # Procesos en background
pi install npm:pi-subagents           # Subagentes
pi install npm:pi-lens                # AST search + LSP
pi install npm:pi-slopchop            # Optimización de contexto

# Listar paquetes instalados
pi list
```

Las extensiones se descubren automáticamente desde `~/.pi/agent/extensions/` y `.pi/extensions/`. Puedes escribir la tuya propia en TypeScript:

```typescript
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

export default function (pi: ExtensionAPI) {
  pi.registerTool({
    name: "saludar",
    description: "Saluda a alguien",
    parameters: Type.Object({
      nombre: Type.String({ description: "Nombre a saludar" }),
    }),
    async execute(toolCallId, params, signal, onUpdate, ctx) {
      return {
        content: [{ type: "text", text: `¡Hola, ${params.nombre}!` }],
      };
    },
  });
}
```

### Compaction

Cuando la ventana de contexto se llena, puedes compactar:

- **Automático**: Pi compacta cuando se acerca al límite de contexto.
- **Manual**: `/compact [instrucciones]` para compactar con enfoque personalizado.
- **Extensiones**: `pi-slopchop` puede reducir el uso de tokens hasta un 98%.

### Temas

Pi soporta temas personalizados. Puedes instalar varios, yo uso [pi-powerline-footer](https://pablocaro.es/powerline-footer-hidden-gems) que personaliza la barra de estado:

```bash
pi install npm:pi-powerline-footer
```

Configura el tema en `settings.json`:

```json
{
  "powerline": {
    "preset": "default",
    "customItems": [
      { "id": "ci", "statusKey": "ci", "position": "right", "color": "success" }
    ]
  }
}
```

## Nivel 4: Power user — Configuración total

### Keybindings personalizados

Pi permite mapear atajos de teclado en `keybindings.json`:

```json
{
  "ctrl+shift+f": { "type": "files" },
  "alt+o": { "type": "command", "command": "ask-user" }
}
```

### Modo no interactivo

Para prompts de un solo uso desde scripts:

```bash
pi -p "Resume este código"
cat README.md | pi -p "Resume este texto"
pi -p @captura.png "¿Qué hay en esta imagen?"
```

### Modos programáticos

- **`--mode json`**: Salida estructurada como JSON lines (ideal para pipelines).
- **`--mode rpc`**: Comunicación bidireccional sobre stdin/stdout.
- **SDK**: Integra pi en aplicaciones Node.js.

### Modo read-only

```bash
pi --tools read,grep,find,ls -p "Revisa el código sin modificarlo"
```

### Mi setup personal

Este artículo está escrito desde dentro de pi, usando exactamente la configuración que describo. Mi `settings.json` incluye más de 20 paquetes, skills personalizadas, y extensiones propias de [mi repositorio pcaropi](https://github.com/pcaro/pcaropi). También lanzo pi desde scripts con personalidades concretas: `pi -p @prompt.md "Haz X"` para tareas repetitivas sin necesidad de entrar en modo interactivo.

En la **[tercera y última entrega](https://pablocaro.es/extensiones-pi-que-uso)** de esta serie, desgloso todas las extensiones que uso en mi día a día, desde subagentes hasta skills de productividad, pasando por búsqueda web, navegación con agente, y mucho más.

*Fuente original*: [pi.dev](https://pi.dev/)
