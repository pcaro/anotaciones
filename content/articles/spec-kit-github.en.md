---
title: GitHub Spec Kit — Specifications as Source of Truth
slug: spec-kit-github
lang: en
date: 2026-05-10
category: ia
tags: agents, ai, spec-kit, github, spec-driven-development
series: Ingeniería de Programación con Agentes
series_index: 6
featured_image: /images/spec-kit-github-cover.png
---

Sixth installment in the series on software engineering with AI agents. Today we look at the project that GitHub has turned into the de facto standard for specification-driven development: **Spec Kit**.

So far we have covered methodologies for directing agents: compound engineering (Every), discipline skills (Addy Osmani), a complete operating system for agents (Superpowers by Jesse Vincent), and minimal pragmatic skills (Matt Pocock). All of them share one premise: you define how you want the agent to work and it executes.

Spec Kit flips that premise. It does not tell the agent **how** to work. It tells it **what** to build, and lets the agent figure out how. The difference is subtle, but it changes everything.

![GitHub Spec Kit — Specifications as Source of Truth](/images/spec-kit-github-cover.png)

## The Problem It Solves

Every framework we have seen in this series assumes you know what you want to build and the problem is that the agent does not build it well. This is correct: without discipline, agents cut corners, generate generic code, and produce inconsistent results.

But there is another, deeper problem: **what if you do not know exactly what you want?** What if your requirements are vague, contradictory, or incomplete?

If twenty developers ask an agent to "build a user CRUD," they will get twenty different results, and probably none of them will be what they actually needed. Because "user CRUD" is not a specification. It is an idea. And ideas do not get implemented — they get refined.

Spec Kit tackles this problem at the root. It is not a framework for programming with agents. It is a **framework for specifying with agents**. The code comes out on its own.

## The Power Inversion

Spec Kit calls its core idea **The Power Inversion**. The idea itself is not new — it is classic software engineering. When I studied computer science, this was called a DDR (Documento de Definición de Requisitos — Requirements Definition Document). You had user requirements ("As a user I want..."), functional requirements, and system requirements. From there you derived a technical specification, and then the code. At Carto it was our core philosophy: PRD, technical spec document, code.

What changes with Spec Kit is that the specification is no longer a document that guides implementation for a human to execute. It is an **executable** document for an AI agent. The PRD is not context for a developer to write code. It is the input that directly generates implementation.

The difference is that agents are very good at helping you specify. They can ask questions, identify ambiguities, explore existing code for context, and refine requirements with you before writing a single line. That ability to iterate on the specification in seconds instead of days is what makes the workflow practical.

The numbers speak for themselves: 95,000 GitHub stars, 8,200 forks, 30+ supported AI agents, and a community extension ecosystem that grew from 26 to 83 entries in a single month.

## The Workflow

Spec Kit defines six core commands that cover the full feature lifecycle:

| Command                 | What It Does                                             |
| ----------------------- | -------------------------------------------------------- |
| `/speckit.constitution` | Defines the project's governing principles               |
| `/speckit.specify`      | Describes **what** to build (requirements, user stories) |
| `/speckit.clarify`      | Structured questioning to resolve ambiguities            |
| `/speckit.plan`         | Translates the specification into a technical plan       |
| `/speckit.tasks`        | Breaks the plan down into actionable tasks               |
| `/speckit.implement`    | Executes tasks and generates code                        |

There are also optional commands: `/speckit.analyze` for cross-artifact consistency validation, and `/speckit.checklist` for generating custom quality checklists.

### 1. Constitution

Before writing a single line of specification, you define the project's principles. This is not a team document. It is a contract that the agent must honor in every decision.

Spec Kit includes an example constitution with nine articles covering everything from "library-first" (every feature starts as a standalone library) to "test-first imperative" (no code without failing tests first).

The constitution is not optional. It is the project's immune system. Without it, the agent makes coherent but not necessarily consistent decisions. With it, every decision reinforces the architecture.

### 2. Specification

Here is the key to everything: in `/speckit.specify` you only talk about the **what** and the **why**. No tech stack. No APIs. No how.

The specification template enforces this separation explicitly:

```text
- ✅ Focus on WHAT users need and WHY
- ❌ Avoid HOW to implement (no tech stack, APIs, code structure)
```

This is harder than it sounds. As engineers, our instinct is to jump to the "how" as soon as we understand the problem. Spec Kit forces you to stay in the "what" long enough for the specification to be complete.

Additionally, the template includes `[NEEDS CLARIFICATION]` markers that the agent must use when something is unclear. This prevents the most common problem with LLMs: guessing instead of asking.

### 3. Clarification

This is the step I value the most personally. Before moving to the technical plan, `/speckit.clarify` starts a structured dialogue where the agent identifies ambiguities and asks you about them one by one.

It is not a generic questionnaire. The agent has read the specification and knows exactly what it does not understand. It asks you until no branches of the decision tree remain unexplored.

It is the same pattern as Matt Pocock's `/grill-me`, but embedded in a broader workflow and with a structured format that gets recorded in the specification itself.

### 4. Plan

Now it is time for the "how". You tell the agent your tech stack and architectural decisions. The agent generates a detailed implementation plan that includes:

- **Data model**: schemas, relationships, constraints
- **API contracts**: endpoints, events, formats
- **Research**: library comparisons, benchmarks, technical decisions with rationale
- **Quickstart**: key validation scenarios

Every technical choice links back to concrete requirements in the specification. Nothing is left untraced.

### 5. Tasks

The plan gets broken down into individual tasks, each with exact file paths, complete code, and verification steps. Independent tasks are marked as parallelizable.

Spec Kit's task system is notable because it distinguishes between HITL (human-in-the-loop, requires a human decision) and AFK (fully automatable from start to finish) tasks. This lets the human intervene only where they actually add value.

### 6. Implementation

The agent executes tasks in order, respecting dependencies and following TDD. Each task produces evidence: passing tests, clean builds, validated contracts.

If something fails, the agent does not proceed. It stops, reports, and waits for instructions. This is the principle that runs through the entire series materialized: **verification is not negotiable**.

## The Constitutional Foundation

Spec Kit imposes a high level of detail in its constitution. These are not vague principles. They are nine articles with concrete clauses that the agent cannot ignore.

**Article I — Library-First**: Every feature starts as a standalone library. This forces modularity from the first commit. No "we will refactor later."

**Article II — CLI Interface**: Every library must expose a command-line interface. This guarantees observability: you can invoke any functionality from a script without touching the UI.

**Article III — Test-First Imperative**: Non-negotiable. Tests first. Failing tests. Then the minimal implementation to make them pass.

**Articles VII & VIII — Simplicity and Anti-Abstraction**: Maximum 3 projects in the initial implementation. Use the framework directly, do not wrap it. Nothing "just in case."

**Article IX — Integration-First Testing**: Tests in real environments. Real databases. Real services. No mocks if you can avoid them.

The key detail is how these articles are enforced through **gates** in the implementation plan template. Before the agent writes a single line, it goes through a "pre-implementation gates" phase that checks every article. If something fails, the agent must justify it in writing in a "Complexity Tracking" section.

This turns the constitution from a passive document into an **active enforcement system**. It is not that the agent "should" follow the rules. It is that it cannot skip them without leaving evidence.

## Comparison with the Rest of the Series

Each project we have seen in this series occupies a different niche:

| Project         | Approach                | Strength                                             |
| --------------- | ----------------------- | ---------------------------------------------------- |
| **Every**       | Compound engineering    | Knowledge accumulation in CLAUDE.md                  |
| **Addy Osmani** | Harness engineering     | Senior engineer discipline with anti-rationalization |
| **Superpowers** | Methodology engineering | Complete operating system for agents                 |
| **Matt Pocock** | Skills engineering      | Minimal skills anyone can adopt                      |
| **Spec Kit**    | **Spec engineering**    | Specifications are the source of truth               |

Spec Kit is the only one that does not start with the agent. It starts with the specification. The agent is the last step, not the first.

## My Take

Spec Kit is the project that comes closest to classical software engineering among those I have covered in this series. Not for its technical complexity (which is minor: it is basically a Python CLI that generates markdown files), but because it formalizes something we always should have done: specify before building.

Inverting the relationship between specification and code is an idea that sounds good in the abstract but has deep implications. If code is a generated artifact, what does it mean to "maintain" software? It means evolving specifications. Debugging means fixing specifications that generate incorrect code. Refactoring means restructuring specifications for clarity.

The software engineer profile has always been different from that of a programmer. It was never someone who just writes code. It is someone who **writes specifications that generate code**. Close to what is now called a Product Owner in Scrum, but with the technical ability to know what is feasible and what is not.

I do not know if this vision will fully materialize. But Spec Kit has something none of the other projects have: GitHub's institutional backing. With 95,000 stars and growing, with an adoption rate that has doubled Superpowers in months, Spec Kit is not an experiment. It is a movement.

And the most interesting part is that GitHub is not building Spec Kit to sell you anything. It is open source, it is free, and it works with any agent: Claude Code, Gemini CLI, Cursor, Codex, Copilot, whichever you use. It is a bet on an open standard for AI-assisted development, and it is working.

The question you should ask yourself is not "which agent do I use" or "what methodology do I use with my agents," but rather "what specification do I write so that my agents build the right thing." Spec Kit provides an answer: write the specification first. The rest is implementation.

## Resources

- [GitHub Spec Kit](https://github.com/github/spec-kit) — The official repository (95K+ stars)
- [Spec-Driven Development — the methodology](https://github.com/github/spec-kit/blob/main/spec-driven.md) — The document defining SDD
- [Spec Kit Community Extensions](https://speckit-community.github.io/extensions/) — Community extensions catalog
- [Matt Pocock — Skills That Work](https://pablocaro.es/en/matt-pocock-skills) — Previous article in the series
- [Superpowers — Jesse Vincent](https://pablocaro.es/en/superpowers-obra-jesse-vincent) — Previous article in the series
- [Agent Skills — Addy Osmani](https://pablocaro.es/en/agent-skills-addy-osmani) — Previous article in the series
- [Compound Engineering — Every](https://pablocaro.es/en/compound-engineering-every) — Previous article in the series
