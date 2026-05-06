---
title: Matt Pocock — Simple Skills That Work
slug: matt-pocock-skills
lang: en
date: 2026-05-06
category: ia
tags: agents, ia, skills, matt-pocock, claude-code
series: Ingeniería de Programación con Agentes
series_index: 5
featured_image: /images/matt-pocock-skills-cover.png
---

Fifth installment of the series on software engineering with agents. Today it is the project that is taking off right now: **Matt Pocock's skills**.

I have covered Superpowers (Jesse Vincent), Agent Skills (Addy Osmani), and Compound Engineering (Every). Each brings an important piece of the puzzle. But Matt Pocock's skills have exploded in popularity in a matter of days, and I think I know why: they apply a KISS philosophy taken to the extreme. Short, direct skills with no pretensions. And one of them, `/grill-me`, has become a phenomenon in its own right.

![Matt Pocock Skills](/images/matt-pocock-skills-cover.png)

## The philosophy: skills a real engineer would use

Matt is known for Total TypeScript and his work on TypeScript. When he started publishing skills for Claude Code, he didn't write a framework. He wrote three-line markdown files that did one thing and did it well.

The repository's tagline says it all: _"Skills for Real Engineers."_ No abstraction layers, no complex plugins, no sophisticated lifecycles. Just markdown files with frontmatter that get injected into the agent's context. Period.

The repository is organized into buckets: `engineering/` (daily skills), `productivity/` (general workflow tools), `misc/` (rarely used), `personal/` (tied to his setup), and `in-progress/`. Out of ~20 total skills, only about 6 are the ones he actually recommends for daily use. That restraint is the key: no more than half a dozen skills, and very very short.

The contrast with Superpowers (v5 with 20+ skills, adversarial loops, a complete phase system) could not be bigger. Matt proves that less can be more if you choose well what to automate.

## `/grill-me`: the skill that changes everything

Three sentences. That is the entire skill:

> _"Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. Ask the questions one at a time. If a question can be answered by exploring the codebase, explore the codebase instead."_

Three sentences that have generated 62,000 GitHub stars and been shared everywhere. Why?

Because they solve problem number one of working with agents: **alignment**. The agent doesn't know what you want, and you don't know what the agent understood. `grill-me` forces a structured conversation where the agent questions you until no branches of the decision tree remain unexplored.

Matt says that in a typical session, Claude asked him 16 questions for a relatively simple feature. For complex features, he has had sessions with 30-40-50 questions lasting almost half an hour. But at the end of that half hour, the design is completely resolved. No surprises when the agent starts writing code.

The concept of the "design tree" comes from _The Design of Design_ by Frederick P. Brooks. The idea is that when you design something, you walk down branches: "advanced search or simple search? If advanced, which filters? Which sorting?" Until you have walked every branch and the design is fully specified.

## The complete flow: grill → PRD → issues → TDD

Matt chains several skills into a pipeline that covers the entire lifecycle of a feature, from idea to code through tests:

1. **`/grill-me`**: the agent interviews you until the design is clear. Each question resolves a decision. If it can answer by exploring the codebase, it does.

2. **`/to-prd`**: once aligned, it turns the conversation into a PRD (Product Requirements Document) with user stories, implementation decisions, and acceptance criteria. Published as an issue on GitHub, Linear, or whatever tracker you use.

3. **`/to-issues`**: breaks the PRD into independent issues using _vertical slices_ (tracer bullets). Each issue cuts through all layers (schema, API, tests) and is demoable on its own. Distinguishes between HITL (human-in-the-loop, requires human decision) and AFK (fully automatable).

4. **`/tdd`**: Test-Driven Development with a red-green-refactor loop. A substantial skill that includes philosophy on mocking, deep modules, and interface design. Write a failing test → minimal implementation → refactor. One iteration at a time, never all horizontal slices together.

5. **`/improve-codebase-architecture`**: for when the code has become a ball of mud. Explores the codebase looking for shallow modules, hidden coupling, and lack of testability.

6. **`/grill-with-docs`**: a variant of grill-me that also updates a `CONTEXT.md` with the shared domain language and writes ADRs for hard-to-reverse decisions. Matt's personal favorite — a combination of interviewing with domain-driven design.

---

It is remarkable how the entire flow maps to what we have seen before:

- **Every's scaffolding** (CLAUDE.md that accumulates knowledge) appears here as `CONTEXT.md` + ADRs.
- **Addy Osmani's discipline** (anti-rationalization tables, workflows with checkpoints) appears in the TDD skill with its per-cycle checklists.
- **Superpowers' structured methodology** (file structure first, unit decomposition, adversarial loops) appears here as vertical slices, tracer bullets, and the HITL/AFK split.

But Matt wraps it all in skills so short they could fit in a tweet. No over-engineering. Just pragmatism.

## My take

Matt Pocock has done something I find harder than building a framework: he has distilled his experience into pieces so small that anyone can adopt them without changing their workflow.

`/grill-me` feels especially familiar because my personal workflow with agents has always included an iterative questioning phase — almost a manual version of what Matt has codified. Seeing it turned into a public skill, with 62,000 people giving it stars, confirms the instinct was right: early alignment is the most undervalued step in working with agents.

The rest of the skills are equally solid. `to-prd` and `to-issues` formalize what any senior engineer does instinctively (think before writing, split work into reviewable chunks) but rarely documents. The TDD skill is the best I have seen for agents: it doesn't just say "do TDD", it explains _why_ horizontal slices produce bad tests and _how_ to do vertical cycles correctly.

What sets Matt apart from the rest is **accessibility**. Superpowers requires integrating a runtime. Agent Skills requires installing a plugin. Matt's skills are markdown files you can copy to your `.claude/` in 30 seconds. And if you don't want to install them, just reading them already gives you the mental framework.

I don't think Matt's skills replace Superpowers or Agent Skills. They are tools for different contexts. Superpowers is for when you want a complete methodology the agent cannot skip. Matt is for when you want small, swappable pieces that you understand and modify.

Both make sense. But Matt has proven something important: sometimes the best skill is the one that fits in three lines.

## Resources

- [mattpocock/skills on GitHub](https://github.com/mattpocock/skills) — The repository (62K+ stars)
- [AI Hero — Skills](https://www.aihero.dev/skills) — The official website with guides for each skill
- [5 Agent Skills I Use Every Day](https://www.aihero.dev/5-agent-skills-i-use-every-day) — Matt's article introducing his kit
- [My Grill Me Skill Has Gone Viral](https://www.aihero.dev/my-grill-me-skill-has-gone-viral) — About the `/grill-me` phenomenon
- [Superpowers — Jesse Vincent](https://pablocaro.es/en/superpowers-obra-jesse-vincent) — Previous article in the series
- [Agent Skills — Addy Osmani](https://pablocaro.es/en/agent-skills-addy-osmani) — Previous article in the series
- [Compound Engineering — Every](https://pablocaro.es/en/compound-engineering-every) — Previous article in the series
