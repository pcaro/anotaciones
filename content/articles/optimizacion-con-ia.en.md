---
title: AI Optimization
slug: optimizacion-con-ia
lang: en
date: 2026-09-22
category: ia
tags: ai, optimization, performance, open-source, libraries
featured_image: /images/optimizacion-con-ia.png
Summary: While only the bad side of AI gets airtime, in mature software it is driving down the cost of optimization. Daniel Lemire documents how six open-source libraries got up to 2.4x faster in a single summer.
---

Only the bad side of AI gets airtime. Unemployment, slop, hallucinations, energy cost. Almost never what it is doing right. In software production the revolution is real and it moves in one very specific direction: it is making every kind of cost cheaper.

There is a lot of talk about how easy prototyping and greenfield software are now. Fair enough. But the interesting case is **stable** software, the kind that is already optimized, where each further improvement used to cost days of work. That is where the change shows up most clearly.

Daniel Lemire documented it this summer. He maintains several open-source libraries that half the internet runs on: `ada` (URL parsing in Node.js), `simdjson` (JSON in Node.js), `simdutf` (Unicode in Node.js), `fast_float` (number parsing in GCC's libc and Chromium), and the Roaring bitmap libraries (inside many database engines).

![ada: URL parsing throughput over time](/images/optimizacion-con-ia.png)

These libraries had flat performance for years. Not because nobody cared, but because the remaining gains required days of careful work and nobody had the days. In 2026, six of them got much faster, most of it in a few weeks of summer.

The numbers:

- **ada**: from 0.54 GB/s to 1.28 GB/s in six weeks (2.4x). About 15 million URLs per second on one core.
- **simdutf**: ASCII validation went from 83 GB/s to 160 GB/s.
- **roaring** (Go): the `FastOr` union got 3.1x faster and the many-value iterator 4.5x–5.9x.
- **CRoaring** (C): 64-bit bitmap cardinality got 4.9x faster.
- **fast_float**: +43% and +70% on two test files.
- **simdjson**: serialization 1.6x–2.1x faster with C++26 reflection.

Lemire is honest: he cannot know how much AI was involved in each case. He does not ask how people arrived at their code; he only asks that it be good. He himself codes with Claude (Opus 5), Grok, and DeepSeek (V4 Pro).

His explanation of why it happened is the whole point: **the techniques have been known for years. What changed is that trying new ideas got cheap.** Each optimization attempt used to cost days; now you can run twenty experiments in the time one used to take, throw away the nineteen that do not work, and keep the good one. That is it.

There is a very human bias at play here, the one-sided bet fallacy: when we see the downsides of something, we ignore the benefits. Cars kill people, but ambulances save them. With AI we are in that phase: we only look at the bad side.

In this case the benefit is concrete and measurable. Millions of people run these libraries, and this summer they got faster. For free. Without changing anything on their end.

New software and prototypes are cool, but the falling cost of optimization in mature software may be the most underrated effect of all this.

*Original source*: [A summer of AI optimization](https://lemire.me/blog/2026/09/22/a-summer-of-ai-optimization/) — Daniel Lemire.
