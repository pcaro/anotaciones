Title: AgentsView: analíticas locales para tus coding agents
Date: 2026-06-10
Category: Herramientas
Tags: agentsview, ai, coding agents, analytics, claude code, pi, codex, open-source
Slug: agentsview-analytics-agentes
Lang: es
Summary: AgentsView es una herramienta open-source que indexa las sesiones de más de 20 coding agents en una base de datos SQLite local y ofrece dashboards de analíticas, tracking de costes y búsqueda full-text sin enviar datos fuera de tu máquina.
Featured_image: /images/agentsview-dashboard.png

Si usas varios coding agents (Claude Code, Codex, Pi, Cursor...) sabes lo que es perder el hilo de cuánto has gastado, qué herramientas usas más o en qué proyecto pasas más horas. Cada agente guarda sus sesiones en su propio formato y directorio, y hasta ahora no había una forma unificada de verlo todo junto.

[AgentsView](https://github.com/kenn-io/agentsview) resuelve esto. Es una herramienta open-source (Go + Svelte 5, MIT) que indexa todas tus sesiones de coding agents en una SQLite local y te da dashboards de analíticas, tracking de costes y búsqueda full-text. Sin cuentas, sin telemetría, sin que los datos salgan de tu máquina.

![AgentsView dashboard](/images/agentsview-dashboard.png)

## Instalación

```bash
# macOS / Linux
curl -fsSL https://agentsview.io/install.sh | bash

# O con Homebrew (app de escritorio)
brew install --cask agentsview
```

Una vez instalado, arrancas el servidor y abre el dashboard en `http://127.0.0.1:8080`:

```bash
agentsview serve
```

En el primer arranque descubre automáticamente las sesiones de todos los agentes que tengas instalados.

## Qué te muestra

- **Dashboard de costes**: gasto diario por agente y por modelo, con precios vía LiteLLM. Calcula también los cache tokens (tanto de creación como de lectura).
- **Mapa de calor de actividad**: visualiza tus días y horas más productivos.
- **Búsqueda full-text (FTS5)**: busca en el contenido de todas tus sesiones pasadas. Ideal para recuperar ese comando o solución que usaste hace semanas.
- **Visor de sesiones**: navega sesión por sesión, exporta a HTML o publícala como GitHub Gist.
- **Estadísticas por proyecto**: tokens usados, herramientas más frecuentes, duración media de sesión.
- **Live updates vía SSE**: si tienes sesiones activas, el dashboard se actualiza solo.

## CLI para costes

Además del dashboard web, tiene una CLI muy rápida que reemplaza a `ccusage`:

```bash
# Resumen diario de costes (últimos 30 días)
agentsview usage daily

# Desglose por modelo
agentsview usage daily --breakdown

# Filtrar por agente y fechas
agentsview usage daily --agent claude --since 2026-05-01

# Salida JSON para scripts
agentsview usage daily --json
```

Como los datos ya están indexados en SQLite, las consultas son mucho más rápidas que reparsear los archivos de sesión cada vez.

## Agentes soportados

AgentsView auto-detecta sesiones de más de 20 agentes: Claude Code, Codex, Pi, Cursor, Copilot CLI, Gemini CLI, OpenCode, OpenHands, Qwen Code, Kimi, Warp, Forge, Zencoder y varios más. La lista completa está en el [README](https://github.com/kenn-io/agentsview#supported-agents).

## PostgreSQL para equipos

Si trabajas en equipo, puedes sincronizar los datos a una PostgreSQL compartida:

```bash
agentsview pg push --watch   # sincronización continua
agentsview pg serve           # servir UI desde PostgreSQL
```

La UI en modo PostgreSQL es read-only, así que cualquiera del equipo puede ver los dashboards sin modificar datos.

## Lo que no hace

- No envía datos a ningún servidor externo. El único tráfico saliente opcional es un check de actualizaciones al arrancar (se desactiva con `--no-update-check`).
- No requiere cuenta ni login.
- No es un reemplazo del agente en sí. Es una capa de analíticas sobre lo que ya tienes.

AgentsView cubre un vacío real en el ecosistema de coding agents: tener visibilidad unificada sobre cómo y cuánto usas estas herramientas. Si usas más de un agente, merece la pena.
