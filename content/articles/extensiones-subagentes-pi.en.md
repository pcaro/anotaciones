Title: Pi subagent extensions: TintinWeb, NicoBailon and Taskplane
Date: 2026-05-03 15:23
Category: Programming
Tags: pi, coding-agent, subagents, extensions, CLI, tools
Slug: extensiones-subagentes-pi
Lang: en
Featured_image: /images/pi-subagentes.png
Summary: A comparison of three extensions for running subagents in pi — TintinWeb, NicoBailon, and Taskplane — each with a different approach.

The biggest advantage of [pi](https://pi.dev/) over other coding agents is its **extensions**. Pi doesn't come with subagents, plan mode, or MCP. It gives you the primitives to build what you need. If you don't want to build it yourself, install a [third-party package](https://pi.dev/packages) and you're done.

![Three stylized figures running in parallel, passing a glowing baton](/images/pi-subagentes.png)

I have several custom extensions in [my pcaropi repo](https://github.com/pcaro/pcaropi), but here I'm comparing three different approaches for delegating work to subagents — which is one of the most useful things when working with pi on real projects.

## The three options

|                       | **TintinWeb**                            | **NicoBailon**                                    | **Taskplane (HenryLach)**                               |
| --------------------- | ---------------------------------------- | ------------------------------------------------- | ------------------------------------------------------- |
| **Paradigm**          | Single subagents, Claude Code style      | Generic orchestration (single/chain/parallel)     | Batch orchestration with waves, lanes, and DAG          |
| **Install**           | `pi install npm:@tintinweb/pi-subagents` | `pi install npm:pi-subagents`                     | `pi install npm:taskplane`                              |
| **Built-in agents**   | 3 (Explore, Plan, general-purpose)       | 8 (scout, researcher, planner, worker, reviewer…) | 4 (supervisor, task-worker, task-reviewer, task-merger) |
| **Chains / Parallel** | ❌                                       | ✅ Sequences + fan-out/fan-in                     | ✅ Waves with parallel lanes via DAG                    |
| **Git worktrees**     | ✅ Basic                                 | ✅ Advanced                                       | ✅ Core of the system                                   |
| **Web Dashboard**     | ❌                                       | ❌                                                | ✅ Live dashboard with SSE                              |
| **Maturity**          | Early (0.6.3)                            | Mature (0.24.0)                                   | Initial release                                         |

### TintinWeb — Subagents, Claude Code style

[@tintinweb/pi-subagents](https://github.com/tintinweb/pi-subagents) replicates the Claude Code model: `Agent`, `get_subagent_result`, and `steer_subagent` tools. Few agents (Explore, Plan, general-purpose), but highly polished UX: animated widget, interactive conversation viewer, mid-run steering to redirect running agents.

Its most unique features: **persistent memory** across sessions (project/local/user) and an **RPC event bus** so other extensions can spawn subagents.

Great if you're coming from Claude Code and want something familiar.

### NicoBailon — The full orchestrator

[NicoBailon's pi-subagents](https://github.com/nicobailon/pi-subagents) is the most mature of the three (0.24.0, 20K lines of TypeScript). A single `subagent` tool with single, chain, and parallel modes. Comes with 8 built-in agents, 6 predefined prompt templates, and a preview TUI to edit steps before launching.

Things I like: **cascading model fallback** (if a model fails on quota, it tries the next one), **agent packages** with namespacing, and `pi-intercom` integration for child→parent communication.

This is the one I use day to day. Flexible, battle-tested, well documented.

### Taskplane — Batch orchestration

[Taskplane by HenryLach](https://github.com/HenryLach/taskplane) is a different beast. It's not a generic subagent framework — it's a **batch task orchestration system**. Tasks are defined in `PROMPT.md` + `STATUS.md` files with steps, dependencies, and checkboxes. A DAG organizes tasks into waves, each wave runs lanes in parallel with isolated worktrees, and a merge agent integrates everything at the end.

It has impressive features: a **live web dashboard** with SSE, **multi-step workers** that keep context between steps, automatic **inline reviews**, and **auto-recovery** that retries crashed workers. It even supports **polyrepo** with cross-repo dependencies.

For projects where you have a batch of well-defined features with dependencies, it's unbeatable.

## Which one to use?

- **Delegate individual tasks with a clean UX** → TintinWeb
- **Flexible orchestration with chains, parallel, and templates** → NicoBailon
- **Run a batch of features with dependencies and automatic reviews** → Taskplane

All three install with a single `pi install npm:...`. TintinWeb and NicoBailon can coexist since they use differently named tools. Taskplane has its own paradigm and shouldn't conflict with either.

More pi extensions and configs in [my pcaropi repo](https://github.com/pcaro/pcaropi).

_Fuente original_: [pi.dev](https://pi.dev/)
