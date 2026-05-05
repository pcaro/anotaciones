Title: Extensiones de subagentes para pi: TintinWeb, NicoBailon y Taskplane
Date: 2026-05-03 15:23
Category: IA
Tags: pi, coding-agent, subagentes, extensiones, cli, herramientas
Slug: extensiones-subagentes-pi
Lang: es
Featured_image: /images/pi-subagentes.png
Summary: Comparativa de tres extensiones para ejecutar subagentes en pi — TintinWeb, NicoBailon y Taskplane — cada una con un enfoque distinto.

La mayor ventaja de [pi](https://pi.dev/) frente a otros coding agents son sus **extensiones**. Pi no trae subagentes, no trae plan mode, no trae MCP. Te da las primitivas para que montes lo que necesites. Si no quieres montarlo tú, instalas un [paquete de terceros](https://pi.dev/packages) y listo.

![Tres figuras estilizadas corriendo en paralelo, pasándose un testigo brillante](/images/pi-subagentes.png)

Tengo varias extensiones propias en [mi repo pcaropi](https://github.com/pcaro/pcaropi), pero aquí voy a comparar tres enfoques distintos para delegar trabajo a subagentes — que es de lo más útil cuando trabajas con pi en proyectos serios.

## Las tres alternativas

|                       | **TintinWeb**                              | **NicoBailon**                                    | **Taskplane (HenryLach)**                               |
| --------------------- | ------------------------------------------ | ------------------------------------------------- | ------------------------------------------------------- |
| **Paradigma**         | Subagentes individuales estilo Claude Code | Orquestración genérica (single/chain/parallel)    | Orquestración por batches con waves, lanes y DAG        |
| **Instalación**       | `pi install npm:@tintinweb/pi-subagents`   | `pi install npm:pi-subagents`                     | `pi install npm:taskplane`                              |
| **Agentes built-in**  | 3 (Explore, Plan, general-purpose)         | 8 (scout, researcher, planner, worker, reviewer…) | 4 (supervisor, task-worker, task-reviewer, task-merger) |
| **Chains / Parallel** | ❌                                         | ✅ Cadenas + fan-out/fan-in                       | ✅ Waves con lanes paralelas según DAG                  |
| **Git worktrees**     | ✅ Básico                                  | ✅ Avanzado                                       | ✅ Nucleo del sistema                                   |
| **Web Dashboard**     | ❌                                         | ❌                                                | ✅ Dashboard en vivo con SSE                            |
| **Madurez**           | Early (0.6.3)                              | Maduro (0.24.0)                                   | Initial release                                         |

### TintinWeb — Subagentes al estilo Claude Code

[@tintinweb/pi-subagents](https://github.com/tintinweb/pi-subagents) replica el modelo de Claude Code: herramientas `Agent`, `get_subagent_result` y `steer_subagent`. Pocos agentes (Explore, Plan, general-purpose), pero experiencia muy pulida: widget animado, conversation viewer interactivo, steering en caliente para redirigir agentes en ejecución.

Lo más diferencial: **memoria persistente** entre sesiones (project/local/user) y un **event bus RPC** para que otras extensiones spawneen subagentes.

Ideal si vienes de Claude Code y quieres algo familiar.

### NicoBailon — El orquestador completo

[pi-subagents de NicoBailon](https://github.com/nicobailon/pi-subagents) es el más maduro de los tres (0.24.0, 20K líneas de TypeScript). Una sola herramienta `subagent` con modos single, chain y parallel. Viene con 8 agentes built-in, 6 prompt templates predefinidos, y una TUI de preview para editar steps antes de lanzar.

Cosas que me gustan: **model fallback** en cascada (si un modelo falla por quota, prueba el siguiente), **agent packages** con namespacing, e integración con `pi-intercom` para comunicación hijo→padre.

Es el que uso yo en el día a día. Flexible, probado, bien documentado.

### Taskplane — Orquestración por batches

[Taskplane de HenryLach](https://github.com/HenryLach/taskplane) es otra cosa. No es un framework de subagentes genérico: es un **sistema de orquestración de tareas por lotes**. Las tareas se definen en archivos `PROMPT.md` + `STATUS.md` con pasos, dependencias y checkboxes. Un DAG organiza las tareas en waves, cada wave ejecuta lanes en paralelo con worktrees aislados, y un merge agent integra todo al final.

Tiene cosas brutales: **dashboard web en vivo** con SSE, **workers multi-paso** que mantienen contexto entre pasos, **reviews inline** automáticas, y **auto-recovery** que reintenta workers caídos. Incluso soporta **polyrepo** con dependencias cross-repo.

Para proyectos donde tienes un batch de features bien definidas con dependencias, es imbatible.

## ¿Cuál usar?

- **Delegar tareas sueltas con una experiencia limpia** → TintinWeb
- **Orquestación flexible con chains, parallel y templates** → NicoBailon
- **Ejecutar un batch de features con dependencias y reviews automáticas** → Taskplane

Los tres se pueden instalar con un `pi install npm:...`. TintinWeb y NicoBailon pueden coexistir porque usan herramientas con nombres distintos. Taskplane tiene su propio paradigma y no debería conflictuar con ninguno.

Más extensiones y configuraciones de pi en [mi repo pcaropi](https://github.com/pcaro/pcaropi).

_Fuente original_: [pi.dev](https://pi.dev/)
