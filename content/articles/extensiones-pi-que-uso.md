---
title: Las extensiones de pi que uso en mi día a día
slug: extensiones-pi-que-uso
lang: es
date: 2026-05-21
category: ia
tags: pi, coding-agent, extensiones, skills, subagentes, cli
series: Pi: el agente de código
series_index: 3
featured_image: /images/pi-extensiones.png
---

Tercera y última entrega de la serie sobre [pi](https://pi.dev/). En la [primera parte](https://pablocaro.es/que-es-pi-coding-agent) expliqué qué es pi y lo comparé con otros agents. En la [segunda](https://pablocaro.es/pi-de-principiante-a-avanzado) hice una guía completa de uso. Ahora toca lo que realmente diferencia a pi de todo lo demás: **las extensiones**.

Tengo más de 20 paquetes instalados, skills de varios repositorios, y mis propias extensiones en [pcaropi](https://github.com/pcaro/pcaropi). Aquí desgloso lo que uso realmente en el día a día.

![Extensiones de pi](/images/pi-extensiones.png)

## Subagentes — pi-subagents

El [pi-subagents de NicoBailon](https://github.com/nicobailon/pi-subagents) es la extensión que más uso. Es un orquestador completo de subagentes con tres modos: single, chain y parallel.

```bash
pi install npm:pi-subagents
```

Viene con 8 agentes incorporados (scout, researcher, planner, worker, reviewer…) y una TUI de preview donde puedes editar los pasos antes de lanzarlos. El modelo fallback en cascada es muy útil: si un modelo falla por quota, prueba el siguiente automáticamente.

[Ya comparé esta extensión con otras alternativas](https://pablocaro.es/extensiones-subagentes-pi) (TintinWeb y Taskplane), pero mi elección diaria es NicoBailon sin duda.

## Utilidades del sistema

### pi-processes

```bash
pi install npm:@aliou/pi-processes
```

Gestiona procesos en segundo plano: servidores de desarrollo, watchers de tests, logs. El agente puede arrancar `npm run dev` en background, seguir trabajando, y recibir una alerta si el proceso falla. Esencial para cualquier flujo de desarrollo.

### pi-inspect

```bash
pi install npm:pi-inspect
```

Consola de depuración para pi. Muestra el estado interno, las herramientas registradas, los eventos que se están disparando. Útil cuando desarrollas tus propias extensiones o cuando algo no funciona como esperas.

### pi-slim

```bash
pi install npm:pi-slim
```

Reduce el tamaño del prompt de sistema eliminando descripciones que el modelo no necesita. Cada token cuenta, y esta extensión recorta silenciosamente lo superfluo.

## Gestión de sesiones

### pi-smart-sessions (HazAT)

```bash
pi install git:github.com/HazAT/pi-smart-sessions
```

Añade gestión inteligente de sesiones: compactación automática, nombrado inteligente, y resumen de ramas abandonadas. Hace que trabajar con sesiones largas sea mucho más llevadero.

### pi-slopchop

```bash
pi install npm:pi-slopchop
```

Compresión agresiva de contexto. Reduce el uso de tokens hasta un 98% comprimiendo mensajes antiguos sin perder información crítica. Cuando trabajas con sesiones de días, esto es un salvavidas.

### pi-add-dir (itisbryan)

```bash
pi install https://github.com/itisbryan/pi-add-dir
```

Añade un directorio externo a la sesión para que el agente pueda trabajar con archivos fuera del directorio actual. Imprescindible cuando tienes que tocar código en varios repositorios.

## Búsqueda y navegación web

### @aliou/pi-linkup

```bash
pi install npm:@aliou/pi-linkup
```

Tres herramientas de búsqueda web: `linkup_web_search` para descubrir fuentes, `linkup_web_answer` para respuestas sintetizadas con citas, y `linkup_web_fetch` para extraer contenido de URLs concretas. Lo uso constantemente para consultar documentación, investigar APIs, o verificar información durante una sesión de código.

### agent-browser skill

Instalado como skill desde el [repositorio de Vercel Labs](https://github.com/vercel-labs/agent-browser). Permite al agente navegar por páginas web como un humano: hacer clic, rellenar formularios, tomar capturas. [Ya escribí sobre ello](https://pablocaro.es/agent-browser-navegacion-agentes).

### chrome-cdp skill

```bash
pi install git:github.com/pasky/chrome-cdp-skill@v1.0.1
```

Alternativa a agent-browser usando Chrome DevTools Protocol directamente. Más ligero y con control más granular sobre el navegador.

## Productividad y UI

### pi-powerline-footer

```bash
pi install npm:pi-powerline-footer
```

Personaliza la barra de estado de pi con información adicional: estado de CI, rama de git, tiempo de sesión. Lo tengo configurado con ítems personalizados:

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

### @tmustier/pi-code-actions

```bash
pi install npm:@tmustier/pi-code-actions
```

Añade acciones de código rápidas: formatear archivo, organizar imports, ejecutar linter. El agente puede dispararlas sin tener que escribir comandos Bash manualmente.

### @aliou/pi-guardrails

```bash
pi install npm:@aliou/pi-guardrails
```

Guarda raíles de seguridad: bloquea comandos peligrosos (`rm -rf`, `sudo`), protege archivos sensibles (`.env`, `node_modules/`), y confirma antes de operaciones destructivas. Tranquilidad mental cuando el agente trabaja autónomamente.

### pi-ask-user y pi-schedule-prompt

```bash
pi install npm:pi-ask-user
pi install npm:pi-schedule-prompt
```

`pi-ask-user` permite al agente hacer preguntas al usuario con opciones estructuradas. `pi-schedule-prompt` programa ejecuciones periódicas (cada hora, cada día) para tareas de mantenimiento.

### pi-interactive-shell

```bash
pi install npm:pi-interactive-shell
```

Lanza agentes CLI interactivos (Claude Code, Cursor, Gemini CLI) desde dentro de pi. Modos dispatch, hands-free, monitor. Útil para delegar tareas específicas a otros agentes sin salir de pi.

## Skills que uso todos los días

### Del repositorio oficial de pi

- **commit**: Misión crítica. Cada commit que hago pasa por este skill, que genera mensajes descriptivos y bien estructurados. Lo tengo activado siempre.
- **brainstorm**: Para sesiones de diseño estructurado. Sigue una cadena completa: investigar → clarificar → explorar → validar diseño → escribir plan → crear TODOs.
- **learn-codebase**: Cuando entro en un proyecto nuevo, este skill escanea convenciones, agent config files y posibles problemas de seguridad.
- **uv, ruff, ty**: El trío Python. `uv` para gestión de paquetes, `ruff` para linting+formato, `ty` para type checking. Rápidos, modernos, sin fricción.
- **github**: Interactuar con issues, PRs, CI runs y queries avanzadas de GitHub API, todo desde `gh`.
- **frontend-design**: Para cuando construyo interfaces. Genera componentes con alta calidad de diseño.

### De mi repositorio pcaropi

Todas mis extensiones y skills personalizadas están en [github.com/pcaro/pcaropi](https://github.com/pcaro/pcaropi):

#### Extensiones

- `answer.ts` — Q&A interactivo. Extrae preguntas de mensajes del asistente y las responde una a una (`/answer` o `Ctrl+.`).
- `context.ts` — Visualización del uso de contexto (tokens, coste, archivos/skills cargados) vía `/context`.
- `files.ts` — Navegador de archivos interactivo (`/files` o `Ctrl+Shift+o`) con estado git y vista rápida.
- `notify.ts` — Notificaciones de escritorio (Linux/notify-send) cuando el agente completa un turno.
- `session-breakdown.ts` — Historial de sesiones visualizado en 7/30/90 días (`/session-breakdown`).
- `todos.ts` — Gestor de TODOs en Markdown con TUI, bloqueo de archivos y asignación de tareas (`/todos`).
- `uv.ts` — Intercepta comandos Python (`pip`, `poetry`) y sugiere usar `uv` en su lugar.

#### Skills

- `cli-tools` — Documenta las herramientas CLI disponibles en mi sistema (jq, fx, gh, httpie, etc.)
- `google-workspace` — Acceso a APIs de Google (Drive, Docs, Calendar, Gmail) sin MCP.
- `summarize` — Convierte URLs o archivos locales a Markdown usando `uvx markitdown`.
- `update-changelog` — Skill para mantener el changelog del repositorio actualizado.
- `web-browser` — Interacción con páginas web mediante Chrome DevTools Protocol.
- `linkedin-post-formatter` — Formatea posts para LinkedIn con Unicode bold/italic.

#### Prompt templates

- `pr-create.md` — Template para crear PRs con estructura consistente.
- `pr-fix-checks.md` — Para arreglar checks fallidos en PRs.
- `review.md` — Template para revisiones de código estructuradas.

## MCP

### pi-mcp-adapter (NicoBailon)

```bash
pi install git:github.com/nicobailon/pi-mcp-adapter
```

Adaptador para conectar servidores MCP estándar. Pi no trae MCP nativo (por diseño), pero con este adaptador puedes usar cualquier servidor MCP del ecosistema.

*Fuente original*: [pi.dev](https://pi.dev/) | [pcaropi](https://github.com/pcaro/pcaropi)
