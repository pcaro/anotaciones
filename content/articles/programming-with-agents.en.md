---
title: Programming with Agents
slug: programming-with-agents
lang: en
date: 2026-05-06
category: ia
tags: agents, ai, productivity
series: Ingeniería de Programación con Agentes
series_index: 1
status: published
featured_image: /images/programming-with-agents-cover.jpg
---

After more than 20 years of writing code, the rise of AI agents has changed how I work more than any new framework or language ever could. It is not about the AI writing code for me, but about letting me stay focused on what actually matters: design, architecture, and the technical decisions an agent cannot make. This will be a series of notes that collects several weeks of testing with different methodologies and tools. I will split it into several parts, each exploring a different approach.

![Programming with Agents](/images/programming-with-agents-cover.jpg)

## New workflow

I work with agents as pair programming companions that never get tired. I give them context, pose problems, and review their work with the same criteria I would apply to a human colleague's pull request. The difference is that I can iterate in seconds instead of hours.

I do not use AI to generate code I do not understand. Every line that enters a project of mine has to go through my head first. Agents excel at:

- Writing repetitive tests or scaffolding
- Exploring new APIs or libraries
- Refactoring code following patterns I define
- Cleaning up and linting

## What does not work

Agents shine on well-defined tasks and fail spectacularly when asked to do unsupervised architectural design. I have seen proposals for unnecessary abstractions, phantom dependencies, and solutions to problems that did not exist. The golden rule: if you cannot explain the problem to a junior human, you will not be able to explain it to an agent either.

## The future

Software engineering is not going away, but it is going to mutate. It is mutating already. And very, very quickly.

In this series we will see several engineering processes applied to the use of agents: Compound Engineering (Every), Agent Skills (Addy Osmani), Superpowers (Jesse Vincent), and Skills for Real Engineers (Matt Pocock). Each with its own philosophy, trade-offs, and use cases.
