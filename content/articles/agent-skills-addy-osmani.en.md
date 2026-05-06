---
title: Agent Skills by Addy Osmani — Enforcing Senior Engineering Discipline on Agents
slug: agent-skills-addy-osmani
lang: en
date: 2026-05-06
category: ia
tags: agents, ai, agent-skills, addy-osmani, google, claude-code
series: Ingeniería de Programación con Agentes
series_index: 3
featured_image: /images/agent-skills-addy-cover.png
---

In the previous two parts of this series we have seen an overview of agent-driven engineering and then Every's compound engineering methodology. Now for another similar approach: **Agent Skills**, Addy Osmani's project at Google that has nearly 30,000 stars on GitHub and tackles the problem from a completely different angle.

![Agent Skills by Addy Osmani](/images/agent-skills-addy-cover.png)

## The problem nobody wants to see

Addy poses something uncomfortable: the default behavior of any coding agent is to take the shortest path to "done." Ask for a feature and it writes the feature. It does not ask whether you have a spec, write a test before the implementation, consider whether the change crosses a trust boundary, or check what the PR will look like to a reviewer. It produces code, declares victory, and moves on.

This is exactly the same failure mode every senior engineer has spent their career learning to avoid. Senior work is not what shows up in the diff: it is surfacing assumptions, writing the spec, breaking work into reviewable chunks, choosing the boring design, leaving evidence that the result is correct, sizing the change so a human can actually review it.

Agents skip those steps for the same reason any junior would: they are invisible. The reward signal points at "task complete," not "task complete and the design doc exists." So we have to bolt the senior-engineer scaffolding back on.

## What a skill actually is

Addy defines a skill with precision: a markdown file with frontmatter that gets injected into the agent's context when the situation calls for it. Something between a system-prompt fragment and a runbook.

A skill is **not** reference documentation. It is not "everything you should know about testing." It is a **workflow**: a sequence of steps the agent follows, with checkpoints that produce evidence, ending in a defined exit criterion.

That distinction changes everything. If you put a 2,000-word essay on testing best practices into the agent's context, the agent reads it, generates plausible-looking text, and skips the actual testing. If you put a **workflow** there (write the failing test first, run it, watch it fail, write the minimum code to pass, watch it pass, refactor), the agent has something to do, and you have something to verify.

> Process described with clarity. Workflows over reference. Steps with exit criteria over essays without them.

## The 20 skills and 7 commands

The repository organizes 20 skills around 6 software lifecycle phases, with 7 slash commands on top:

| Phase  | Command   | What it does                 |
| ------ | --------- | ---------------------------- |
| Define | `/spec`   | Decide what you are building |
| Plan   | `/plan`   | Break the work down          |
| Build  | `/build`  | Implement in vertical slices |
| Verify | `/test`   | Prove it works               |
| Review | `/review` | Catch what slipped through   |
| Ship   | `/ship`   | Get to production safely     |

There is also `/code-simplify` that cuts across the whole cycle.

A complex feature might activate 11 skills in sequence. A small bug fix might use 3. A meta-skill (`using-agent-skills`) acts as a router that decides which ones apply. The workflow scales to the actual scope, not the assumed scope.

## Five principles that hold everything up

### 1. Simple and direct process

Workflows are actionable for agents; essays are not. The same is true for human teams. If your team handbook is 200 pages, no one reads it under time pressure. If it is a small set of workflows with checkpoints, people actually run them.

### 2. Anti-rationalization tables

This is the most distinctive design decision in the project. Each skill includes a table of common excuses an agent (or a tired engineer) might use to skip the workflow, paired with a written rebuttal.

- _"This task is too simple to need a spec."_ → Acceptance criteria still apply. Five lines is fine. Zero lines is not.
- _"I'll write tests later."_ → Later is the load-bearing word. There is no later. Write the failing test first.
- _"Tests pass, ship it."_ → Passing tests are evidence, not proof. Did you check the runtime? Did you verify user-visible behaviour? Did a human read the diff?

The reason this works is that LLMs are excellent at rationalization. They will produce a plausible-sounding paragraph explaining why _this particular_ task does not need a spec, or why _this particular_ change is fine to merge without review. **Anti-rationalization tables are pre-written rebuttals to lies the agent hasn't yet told.**

The pattern is just as good for human teams. Most engineering decay is not anyone choosing to do bad work. It is people accepting plausible-sounding justifications for skipping the parts they don't feel like doing.

### 3. Verification is NOT negotiable

Every skill terminates in concrete evidence. Tests pass. Build output is clean. The runtime trace shows the expected behaviour. A reviewer signs off. _"Seems right"_ is never sufficient.

The agent is a generator. You need a separate signal that the work is done. Skills bake that signal into every workflow.

### 4. Progressive disclosure

Do not load all twenty skills into context at session start. Activate them based on the phase.

Every token loaded into context degrades performance somewhere, so you load what is relevant and leave the rest on disk. **Progressive disclosure is how you get a twenty-skill library into a 5K-token slot without poisoning the well.**

### 5. Scope discipline

The meta-skill encodes a non-negotiable I would staple to every agent if I could: _"touch only what you're asked to touch."_ Do not refactor adjacent systems. Do not remove code you do not fully understand. Do not brush against a TODO and decide to rewrite the file.

This sounds obvious until you watch an agent decide that fixing one bug requires modernizing three unrelated files. **Scope discipline is the single biggest determinant of whether an agent's PR is mergeable or has to be unwound.**

## The Google DNA

Addy works at Google, and the skills are saturated with practices from _Software Engineering at Google_ and Google's public engineering culture. This is intentional. Most of what makes Google-scale software work is documented and public, and it is _exactly_ the part agents are most likely to skip.

- **Hyrum's Law** in `api-and-interface-design`. Every observable behaviour of your API will eventually be depended on by someone.
- **The test pyramid (~80/15/5) and the Beyoncé Rule** in `test-driven-development`. _"If you liked it, you should have put a test on it."_
- **DAMP over DRY in tests.** Google's testing philosophy is explicit that test code should read like a specification even at the cost of some duplication.
- **~100-line PR sizing, with Critical / Nit / Optional / FYI severity labels** in `code-review-and-quality`. Straight from Google's code review norms. Big PRs don't get reviewed; they get rubber-stamped.
- **Chesterton's Fence** in `code-simplification`. Don't remove a thing until you understand why it was put there.
- **Trunk-based development and atomic commits** in `git-workflow-and-versioning`.
- **Shift Left and feature flags** in `ci-cd-and-automation`. Catch problems as early as possible, decouple deploy from release.
- **Code-as-liability** in `deprecation-and-migration`. Every line you keep is one you have to maintain forever.

None of these are new ideas. **The point is that none of them are in the agent by default.** A frontier model has read the phrase "Hyrum's Law" in its training data, but it does not apply Hyrum's Law when it is designing your API at 3am while you sleep. Skills are how you make sure it does.

## What you can use even if you don't follow the full strategy

**Anti-rationalization as a team practice.** Write down the lies your team tells itself. _"We'll fix the tests after launch."_ _"This change is too small for a design doc."_ _"It's fine, we have monitoring."_ Pair each with the rebuttal. Put it in your AGENTS.md or your engineering wiki. It will save you arguments and it will catch the next tired Friday-afternoon shortcut.

**Clear process on paper for anything you write internally.** If you find yourself writing a 2,000-word doc titled "how we approach X," you've written reference material. Convert it to a workflow with checkpoints. The doc shrinks to 400 words and people actually run it.

**Verification as a hard exit criterion.** Make "produce evidence" the exit step of every task. For agents, for engineers, for yourself. Evidence is whatever proves the work is done: a green test run, a screenshot, a log, a review approval. Without it, the task is not done. _"Seems right"_ never closes the loop.

**Progressive disclosure for any rulebook.** Do not write a 50-page handbook. Write a small router that points to the right small chapter for the situation. This is true for AGENTS.md, for runbooks, for incident playbooks, for anything anyone will read under time pressure.

**Five non-negotiables, lifted from the meta-skill, that I would put in any AGENTS.md tomorrow:**

1. Surface assumptions before building. Wrong assumptions held silently are the most common failure mode.
2. Stop and ask when requirements conflict. Don't guess.
3. Push back when warranted. The agent (or engineer) is not a yes-machine.
4. Prefer the boring, obvious solution. Cleverness is expensive.
5. Touch only what you're asked to touch.

That is a worthwhile engineering culture in five lines, and you don't need to install anything to adopt it.

## My take

What Addy proposes is different from Every's approach, but complementary. Every focuses on the learning loop: each iteration makes the next cycle easier. Addy focuses on discipline: every task must go through the phases that a senior engineer would never skip.

Every is compound engineering. Addy is **harness engineering** — building the harness that forces the agent to behave like a senior. Addy's repository is not a framework, it is a library of portable workflows. The same SKILL.md file works in Claude Code, Cursor, Gemini CLI, Codex, and any other environment that accepts system-prompt content.

The implication is clear: it is not enough to have a powerful agent. You need a system that prevents it from taking shortcuts. The anti-rationalization tables are the most brilliant idea in the project because they attack directly the most dangerous weakness of LLMs: their ability to produce plausible justifications for doing poor work.

In my own workflow, I am adopting two things immediately: the anti-rationalization tables for the tasks where I most often fail (skipping tests on "small" changes, assuming "I'll review it later"), and the five non-negotiables as a mental checklist before any session with an agent.

## Resources

- [Agent Skills on GitHub](https://github.com/addyosmani/agent-skills) — The repository with all 20 skills (29K+ stars)
- [Agent Skills — the article](https://addyosmani.com/blog/agent-skills/) — Addy's post explaining the design
- [Agent Harness Engineering](https://addyosmani.com/blog/agent-harness-engineering/) — The article on agent harnesses in general
- [Long-running Agents](https://addyosmani.com/blog/long-running-agents/) — Why skills matter more in long sessions
