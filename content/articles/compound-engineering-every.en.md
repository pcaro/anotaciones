---
title: Compound Engineering — Every's Vision for Agent-Driven Engineering
slug: compound-engineering-every
lang: en
date: 2026-05-06
category: ia
tags: agents, ai, compound-engineering, every, claude-code
series: Ingeniería de Programación con Agentes
series_index: 2
featured_image: /images/compound-engineering-every-cover.png
---

In the first part of this series I talked about how AI agents have changed the way I build software. But that was just the warm-up. What follows is the vision of a company that has taken this idea to the extreme: **Every**, the startup from Dan Shipper and Kieran Klaassen, which has built not only products with agents, but a **complete methodology** for doing so.

They call it **compound engineering**.

![Compound Engineering — How Every Codes With Agents](/images/compound-engineering-every-cover.png)

## The problem with traditional engineering

In classic software engineering, every new feature makes the next one harder. More code means more edge cases, more interdependencies, more surprises nobody anticipated. It is a complexity curve that only goes up.

Every realized that with agents writing the code, that premise no longer held. If an agent can generate code in seconds, the bottleneck stops being "write code" and becomes "know what code to write". And if the agent can learn from each iteration, complexity stops being dead weight and becomes fuel.

> In compound engineering, every feature makes the next one easier. Not because the code disappears, but because the system learns from it.

## The compound engineering loop

Every defines four steps that repeat in a cycle. The trick is that the output of each cycle feeds the next one:

### 1. Plan

This is where a compound engineer spends 40% of their time. Not writing code, not reviewing PRs. **Planning**.

The agent investigates the current codebase, reads commit history, searches the internet for best practices, and synthesizes everything into a detailed implementation plan. When it starts writing, it is already warmed up. It already knows the project conventions, the patterns that worked before, and the ones that failed.

This step is critical because an agent without context generates generic code. An agent with context generates code that fits your architecture as if a team member had written it.

### 2. Work

The agent writes code and tests according to the plan. This is what most people imagine when they think about "programming with AI": the agent generates functions, classes, tests. But in compound engineering, this step represents barely 10% of human effort. The code writes itself. The value is in everything surrounding that code.

### 3. Review

The engineer reviews the output. Not just looking for bugs, but extracting **lessons**. Why did the agent choose this abstraction? Was there a pattern it did not recognize? An edge case it forgot?

At Every they use multiple specialized reviewer agents: one for security, another for performance, another for simplicity, another for maintainability. Each one looks at the code from a different angle. The human engineer orchestrates these reviews and decides which feedback to incorporate.

### 4. Compound

This is the step that changes everything. The lessons extracted during review do not stay in the engineer's head. They are documented. They are encoded. They become part of the system.

Every uses files like `CLAUDE.md` and `AGENTS.md` where everything is recorded: approved code patterns, architectural decisions, recurring bugs and their solutions, naming styles, design preferences. The next time an agent works on the project, it reads these files before starting. Each cycle makes the agent smarter.

## A real example: the frustration detector

Kieran Klaassen describes in Every how they built a "frustration detector" for their product Cora, an AI email assistant. The goal: detect when a user is getting frustrated with the app and automatically generate an improvement report.

The flow went like this:

1. **They created a sample conversation** where a user expresses frustration (repeated questions, increasingly terse language).
2. **They asked Claude to write a test** that verifies whether the system detects that frustration.
3. **The test failed** — as it should in TDD.
4. **They asked Claude to write the detection logic**.
5. **It worked partially**. So they asked it to **iterate on the prompt** until the test passed.
6. **To avoid AI non-determinism**, they had Claude run the test 10 times.
7. **It analyzed the 6 failures**, read the chain-of-thought from each one, and discovered a pattern: the system was not detecting hedged language like "Hmm, not quite", which in the context of repetition does signal frustration.
8. **It updated the prompt** to specifically look for that language. In the next iteration, it identified frustration 9 out of 10 times.
9. **They codified the entire flow** into `CLAUDE.md`. The next time they need to detect a user emotion or behavior, they do not start from scratch. They say: "use the frustration detector workflow".

That is compound engineering in action. It is not just solving today's problem. It is teaching the system to solve an entire category of problems.

## The compound engineering plugin

Every has open-sourced their system as a plugin that works with Claude Code, Codex CLI, Cursor, and others. It has more than 50 specialized agents and 38 skills accessible as slash commands.

Some of the most interesting skills:

- `/ce-strategy` — Creates or maintains the product's `STRATEGY.md`: problem, approach, persona, key metrics.
- `/ce-plan` — Generates structured plans for any multi-step task, with automatic confidence checking.
- `/ce-brainstorm` — Interactive Q&A to think through a feature before planning it.
- `/ce-work` — Executes work items systematically.
- `/ce-debug` — Finds root causes and fixes bugs with testable hypotheses.
- `/ce-code-review` — Structured review with multiple reviewer agents in parallel.
- `/ce-compound` — Documents solved problems so the team (and agents) learn from them.
- `/ce-compound-refresh` — Reviews stale learnings and decides whether to update, replace, or archive them.
- `/ce-product-pulse` — Generates reports on usage, performance, errors, and followups.
- `/ce-sessions` — Searches session history across Claude Code, Codex, and Cursor.

And the reviewer agents are specialists: there is one for API contracts, another for data migrations, another for frontend races, another for security, another for performance. Each one applies its specific lens.

## Why this matters

Every runs five software products, each built and maintained primarily by a single person. Products used by thousands of people every day. They are not demos. They are real businesses.

Their metric: a single developer with compound engineering does the work of five traditional developers. Not because they write more code, but because every line they write builds on everything learned before.

The implication is profound. If traditional engineering assumes writing code is hard and engineers are scarce, compound engineering assumes code is cheap and knowledge is the valuable asset. The question is no longer "how do I write this?" but "how do I teach the system to write this, and everything like it, forever?".

## My take

What Every proposes is not a tool, it is a paradigm shift. Software engineering has always had a cumulative component: libraries, frameworks, patterns. But that was accumulation of code. Compound engineering is accumulation of **knowledge about how to build**.

The `CLAUDE.md` is not documentation for humans. It is memory for agents. And that changes the nature of the engineer's work: they stop being the one who writes code and become the one who designs systems that write code, and that also learn from every line they generate.

It is not futurism. Every is already doing it. The plugin is on GitHub with 16k+ stars. The question is not whether this will reach your team, but when.

## Resources

- [Compound Engineering Plugin](https://github.com/EveryInc/compound-engineering-plugin) — Every's open source plugin
- [Compound Engineering: How Every Codes With Agents](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents) — The original article by Dan Shipper and Kieran Klaassen
- [My AI Had Already Fixed the Code Before I Saw It](https://every.to/source-code/my-ai-had-already-fixed-the-code-before-i-saw-it) — Kieran describes the compounding system in action
