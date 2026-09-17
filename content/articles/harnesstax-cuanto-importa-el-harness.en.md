---
title: HarnessTax: The Harness Matters Less Than You Think
slug: harnesstax-cuanto-importa-el-harness
lang: en
date: 2026-09-17
category: ia
tags: pi, opencode, coding-agent, ai, harness, claude-code, codex, benchmarks, ai-agents
featured_image: /images/harnesstax.png
Summary: The HarnessTax study from UC Berkeley and Arena evaluates 21 model-harness pairings and reaches three surprising conclusions. They back up with data why I use pi and OpenCode daily.
---

When you pick a coding agent, you're not just choosing a model: you're also choosing its *harness*, the software that manages tools, context, and task execution. What if switching harnesses improves results or cuts the bill? That's the question [HarnessTax](https://harnesstax.github.io/) asks. The study from UC Berkeley and Arena evaluates 21 model–harness pairs (Claude Code, Codex CLI, and **pi**, across 7 models) on SWE-bench Lite and Terminal-Bench 2.0: 30 random tasks per benchmark, 3 attempts per task.

![HarnessTax: How Much Does the Harness Matter for Coding Agents?](/images/harnesstax.png)

Its three main conclusions are quite surprising:

## 1. The harness barely affects success rate, but it does affect cost

The same model achieves nearly identical success rates across different harnesses, but cost can vary up to **5x**. The clearest case: Claude Fable 5 solves 97.8% of attempts in Claude Code and 96.7% in pi... but Claude Code costs twice as much ($1.33 vs $0.67). On average, Claude Code comes out **2x more expensive than pi** on SWE-bench Lite and 1.5x on Terminal-Bench 2.0. They call that price difference for practically the same quality a *harness tax*.

## 2. A simple harness can be competitive

Pi reaches the **Pareto frontier on both benchmarks** with just four tools: `read`, `write`, `edit`, and `bash`. The key is at startup: Claude Code's mean initial context is **over 10x pi's**, with longer instructions and fatter tool schemas. That overhead is paid on every model call. Less scaffolding, same result.

## 3. Models can perform better outside their provider's harness

This is the most groundbreaking one. Even though OpenAI says GPT-5-Codex is optimized for Codex, in **9 of the 12 comparisons between Anthropic and OpenAI models, the best success rate is achieved with a harness other than the provider's own**. For example, GPT-5.6 Sol gets an 83.3% success rate in pi versus 78.9% in Codex... at half the price. A model's capabilities are portable; the provider-harness coupling guarantees nothing.

## What this means for me

For anyone using coding agents daily, the takeaway is clear: **compare harnesses before accepting the default one**, or you'll be paying the harness tax without noticing.

And for me personally, the study is a data-backed validation of what I already suspected. I've been using [pi](https://pablocaro.es/tag/pi.html) as my main agent for months —[I explained what it is and why it convinced me](https://pablocaro.es/en/que-es-pi-coding-agent)— and [OpenCode](https://pablocaro.es/tag/opencode.html) as a complement. The study confirms exactly why: a minimalist harness, with just the right tools and minimal initial context, delivers the same result as the heavyweight all-in-one agents at a fraction of the cost. The pi trilogy on this blog ages better than I expected.

*Original source*: [HarnessTax: How Much Does the Harness Matter for Coding Agents?](https://harnesstax.github.io/) (UC Berkeley / Arena, September 2026). There's also an [extended version on Arena's blog](https://arena.ai/blog/coding-agents-harness-tax).
