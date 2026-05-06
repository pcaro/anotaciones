---
title: Superpowers — Jesse Vincent Imposes Methodology on Coding Agents
slug: superpowers-obra-jesse-vincent
lang: en
date: 2026-05-06
category: ia
tags: agents, ai, superpowers, jesse-vincent, claude-code, prime-radiant
series: Ingeniería de Programación con Agentes
series_index: 4
featured_image: /images/superpowers-obra-cover.png
---

Fourth installment in the series on agent-driven software engineering. Today I am covering a project that has changed the game: **Superpowers**, by Jesse Vincent.

With 180,000 stars on GitHub and 16,000 forks, Superpowers is the most popular agent skills framework today. But what makes it special is not the star count. It is its obsession: imposing a complete software engineering methodology on coding agents, from the first prompt to the last commit.

![Superpowers — Jesse Vincent](/images/superpowers-obra-cover.png)

## Who is Jesse Vincent

Jesse Vincent is a well-known figure in open source software. He created **Perl 6** (now Raku), co-founded **Best Practical**, and built **RT** (Request Tracker), the ticketing system used by organizations like the Free Software Foundation and the Linux kernel. Today he works at **Prime Radiant**, a company building tools for agent-driven engineering.

His blog has been a reference point in the coding agents community since October 2025, when he published the first article about Superpowers. Since then, every release has been an event.

## The core idea

Superpowers is not just another plugin. It is a **complete development methodology** for coding agents, built on composable skills that activate automatically based on context.

The basic workflow:

1. **Brainstorming** — The agent does NOT start coding. It asks questions, explores alternatives, and refines the idea before touching a line of code.
2. **Using-git-worktrees** — Creates an isolated workspace on a new branch.
3. **Writing-plans** — Breaks work into 2-5 minute tasks, each with exact file paths, complete code, and verification steps.
4. **Subagent-driven-development or executing-plans** — Dispatches agents to implement or executes in batches with human checkpoints.
5. **Test-driven-development** — Mandatory RED-GREEN-REFACTOR. Tests first, always.
6. **Requesting-code-review** — Review against the plan, with Critical/Nit/Optional severities.
7. **Finishing-a-development-branch** — Tests, merge or PR, cleanup.

The mantra that sums it all up: **if the agent starts coding without asking questions, Superpowers has failed**.

## Visual Brainstorming

The most striking new feature of version 5 is the **Visual Brainstorming Companion**: a local web server that the agent spins up to show you mockups, diagrams, and visual comparisons in the browser as you converse.

The origin story is interesting. Jesse found himself asking Claude over and over: _"Hey, why don't you write that out as HTML so I can see what you're talking about."_ Until he remembered the most important mantra of agentic coding: **"Why am I doing this?"**

The agent now asks if you want to try the visual companion, and if you accept, it opens a browser with interactive content. Behind the scenes, a WebSocket server serves chunks of HTML that the agent writes to disk, with JavaScript to capture clicks and feedback.

Jesse used it to brainstorm a logo for Prime Radiant with Claude. He says imagining what that would have looked like in ASCII art gives him chills.

## Spec Review: the adversarial loop

Another v5 advancement is the **spec review loop**. Jesse noticed that agents were leaving "TBD" or "Fill this in later" sections in planning documents — and that it went about as poorly as you would imagine.

The solution: after planning, Superpowers launches a subagent that reads the design documentation looking for gaps and oddities. It is not a substitute for reading it yourself, but it dramatically improves plan quality.

It is the same pattern we have seen in other tools in this series: **an adversarial review loop**. The planner produces, the reviewer criticizes, the planner corrects. It repeats until no objections remain.

## Subagent Driven Development

Up to v4, Superpowers offered the user a choice between subagents or sequential execution with human checkpoints. That ambiguity came from a time when subagents were new and Jesse did not trust them.

As of v5, if your harness supports subagents, **Subagent Driven Development is mandatory**. If it does not support them, Superpowers warns you that a different harness would do a better job, then does what it can.

In harnesses like Claude Code that can choose which model to use for each subagent, Superpowers instructs: cheap model for mechanical tasks, standard for integration, capable for architecture and review. Subagents now have a status protocol: DONE, DONE_WITH_CONCERNS, BLOCKED, NEEDS_CONTEXT.

## Software engineering as a principle

The value of interfaces starts here:

- **Unit decomposition**: each unit must have one clear purpose, well-defined interfaces, and be independently testable.
- **"Can someone understand what a unit does without reading its implementation? Can you change the implementation without breaking consumers?"**
- **Large files as a design smell**: it is not just a style issue, it is a warning that decomposition failed.
- **File Structure as a mandatory step**: before decomposing into tasks, you first decide what files exist and what responsibility each one owns.

This is interface-driven design pushed from specification through implementation and review.

## Other interesting design decisions

**Skills are not documentation.** They are **workflows**: sequences of steps the agent follows, with checkpoints that produce evidence, ending in a defined exit criterion. If you put a 2,000-word essay into the agent's context, it reads it and skips the actual execution. If you put a workflow there, the agent has something to do.

**Instruction priority hierarchy.** Superpowers establishes an explicit priority:

1. Your direct instructions (CLAUDE.md, AGENTS.md) — highest priority
2. Superpowers skills — override default system behavior
3. Default system prompt — lowest priority

If your CLAUDE.md says "don't use TDD" and a Superpowers skill says "always use TDD," the user's instructions win.

**Progressive disclosure.** The 20 skills are not loaded into context at session start. A meta-skill acts as a router that decides which skills apply based on the task. Each skill describes when it should activate. The agent checks whether it applies. If not, it moves on.

**Anti-rationalization tables.** Each skill includes a table of common excuses an agent might use to skip the workflow, paired with a rebuttal. This is especially effective because LLMs are excellent at producing plausible justifications for doing what they feel like.

**The SUBAGENT-STOP gate.** Subagents dispatched for specific tasks skip the meta-skill and do not activate full skill workflows. This prevents a subagent that only needs to implement a change from starting a brainstorming session.

## How it differs from the others

**Every** focuses on the learning loop: compound engineering accumulates knowledge in CLAUDE.md so each cycle is more efficient.

**Addy Osmani** focuses on discipline: agent-skills forces the agent through the phases a senior engineer would never skip, with anti-rationalization tables as the main weapon.

**Superpowers** is more ambitious: it is a **complete operating system** for coding agents. It does not just define workflows — it manages git worktrees, decides which model to use for each subagent, reviews specifications with adversarial loops, and has a communication protocol between subagents.

If Every is compound engineering and Addy is harness engineering, Superpowers is **methodology engineering**: building the system that forces the agent to follow a complete software development methodology.

Addy focuses on senior engineer discipline. Superpowers focuses on **process discipline**: the workflow is in charge, not the agent. The difference is subtle but important.

## My take

Superpowers is the most complete project we have covered in this series. Jesse Vincent has been iterating on the same idea since October 2025: how to make a coding agent behave like an experienced engineer, not a junior who writes the first solution that comes to mind.

The difference from other approaches is that Superpowers does not trust the agent. It does not trust that the agent "will know what to do." It gives the agent a workflow, forces it to follow it, checks that it has followed it, and redirects when it deviates.

That sounds restrictive, and it is. But the experience of hundreds of thousands of users suggests that is exactly what agents need: structure, not freedom.

For me, the most valuable thing about Superpowers is not the skills themselves, but the **philosophy**: if you want an agent to produce quality work, you cannot delegate the methodology to the agent. You have to encode it in skills that activate automatically, with checkpoints that produce evidence, and with adversarial loops that verify nothing was skipped.

The next article in the series will explore yet another approach. But I believe Superpowers marks a before and after in how we think about agent-driven engineering.

## Resources

- [Superpowers on GitHub](https://github.com/obra/superpowers) — The repository (180K+ stars)
- [Superpowers 5 — the announcement](https://blog.fsck.com/2026/03/09/superpowers-5/) — Jesse Vincent's article
- [Superpowers: How I'm using coding agents in October 2025](https://blog.fsck.com/2025/10/09/superpowers/) — The original launch article
- [Prime Radiant](https://primeradiant.com) — Jesse Vincent's company
- [Compound Engineering — Every](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents) — Previous article in the series
- [Agent Skills by Addy Osmani](https://addyosmani.com/blog/agent-skills/) — Previous article in the series
