---
title: What is Pi? — The Minimal Coding Agent That Went Viral
slug: que-es-pi-coding-agent
lang: en
date: 2026-05-21
category: ia
tags: pi, coding-agent, agents, claude-code, codex, opencode, gemini-cli
series: Pi: el agente de código
series_index: 1
featured_image: /images/comparativa-agentes-pi.png
Summary: Pi is a minimal terminal coding agent. This article explains what it is, how it differs from Claude Code, Codex, OpenCode, and Gemini CLI, and why it went viral.
---

I've been using [pi](https://pi.dev/) as my primary coding agent for several months now. It's one of those tools that, once you use it, you can't imagine how you worked before. In this article —the first of a three-part series— I'll explain what pi is, how it differs from other coding agents, and why it has become extremely popular on GitHub. Don't miss [pi.dev](https://pi.dev/) — the site has great animations that explain the concepts visually.

![Coding agent comparison](/images/comparativa-agentes-pi.png)

## The philosophy: less is more

Pi defines itself as *"a minimal terminal coding harness"*. And when they say minimal, they mean it.

The core of pi has exactly **five native capabilities**: read files, run Bash, edit files, write files, and manage sessions. That's it. No subagents, no plan mode, no permission popups, no built-in MCP, no code editor.

It sounds like little, but that's the whole point. We live in the age of *harness engineering* — the discipline of building robust environments around AI agents — and pi is an excellent starting point for building your own harness without paying the toll of a closed ecosystem.

Pi's philosophy is that you should adapt the tool to your workflows, not the other way around. Instead of shipping with 50 features most people don't use, pi gives you the minimal primitives and a TypeScript extension system to build exactly what you need.

Want subagents? Install an extension. Want MCP? Set up an adapter. Want plan mode? Write a prompt template. And if you don't want any of that, it doesn't take up space or slow down startup.

## Comparison with other coding agents

| Feature | **Pi** | **Claude Code** | **Codex** | **OpenCode** | **Gemini CLI** |
|---|---|---|---|---|---|
| **Philosophy** | Minimal core + extensions | Everything included | Everything included | Minimal core | Everything included |
| **Models** | Any provider (API key or subscription) | Claude only | OpenAI only | Multiple (OpenAI API) | Gemini only |
| **Subagents** | Via extensions | Built-in | Built-in | Built-in | Built-in |
| **MCP** | Via extensions | Built-in | - | Built-in | Built-in |
| **Plan mode** | Via skills/templates | Built-in | Built-in | - | - |
| **Extensions** | TypeScript SDK | JSON plugins | - | - | - |
| **Price** | Free (your keys) | Paid subscription | Paid subscription | Free (your keys) | Free (generous free tier) |
| **Platform** | Terminal (any emulator) | Terminal | Terminal | Terminal | Terminal |
| **Tree sessions** | Native (JSONL tree) | Linear | Linear | Linear | Linear |
| **Skills** | Markdown + frontmatter | Markdown + frontmatter | - | - | - |

### Claude Code — Anthropic's all-in-one

Claude Code is Anthropic's official coding agent. It comes with everything: subagents, persistent memory, permission system, native MCP, and a very polished experience. It's the most mature non-IDE agent.

The catch: it only works with Claude. If you want to use DeepSeek, Gemini, or OpenAI, you can't. And the plugin ecosystem is limited compared to pi.

### Codex — ChatGPT integration

Codex is OpenAI's agent. You can use it from the terminal (`codex`) or integrated with ChatGPT. It comes with subagents and a similar experience to Claude Code.

But same as Claude Code, you're locked to one provider. And extensions are practically nonexistent: what you see is what you get.

### Gemini CLI — The community CLI

Gemini CLI comes from the google-gemini community project and integrates with Google's ecosystem (Gemini API, Google Cloud). Google has been gradually moving away from the CLI in favor of Antigravity, its proprietary enterprise client. It comes with skills and subagents, but customization is limited and third-party extensions are practically nonexistent.

### OpenCode — The kindred spirit

[OpenCode](https://github.com/opencode-go/opencode-go) is the one I use most after pi, and in many ways it's its natural complement. Its philosophy is similar: minimal core, terminal-native, multi-model. It doesn't have pi's extension ecosystem, but it comes with built-in subagents and MCP. Written in Go, starts just as fast, and its OpenAI ecosystem integration is excellent.

## What makes pi unique

After trying them all, what makes pi unique is a combination of factors that no other agent brings together:

**Extensibility**: With the TypeScript SDK you can add tools, commands, intercept events, create custom UI, and share it all as pi packages. No one else offers this level of customization.

**Tree sessions**: Conversations are saved as a decision tree. Use `/tree` to jump to any previous point and create an alternative branch without losing progress. Only pi has this.

**Skills and prompt templates**: Small markdown files that inject into the agent's context. The simplest way to teach your agent new capabilities. [I already covered how to install them](https://pablocaro.es/en/installing-github-skills) and [Matt Pocock's viral skills](https://pablocaro.es/en/matt-pocock-skills).

**Package ecosystem**: [pi.dev/packages](https://pi.dev/packages) has extensions for almost everything: MCP adapters, web search, context optimization modes, themes, and more. And if you can't find what you need, you write a TypeScript extension in five minutes.

**It's not an IDE**: Pi is an agent that lives in your terminal, not an editor. This means it works the same on your local machine, on a server over SSH, inside tmux, or on WSL. You use your favorite editor and pi handles the rest. I'll dive deeper into this concept in the [next part](https://pablocaro.es/en/pi-de-principiante-a-avanzado) of the series.

## Why I like pi

By now it's probably obvious, but to wrap up: I like pi because I live in the terminal. Because I want to try many models without being locked to one provider. Because I customize everything with my own extensions.

It's not for everyone, obviously. If you prefer to pay a subscription and forget about it, Claude Code or Codex are more straightforward. But if you're an engineer who lives in the terminal, pi is probably the best coding agent out there today.

In the next articles of this series:
- **[Pi from Beginner to Advanced](https://pablocaro.es/en/pi-de-principiante-a-avanzado)** — Installation, TUI, sessions, skills, extensions, and everything you need to master it.
- **[The Pi Extensions I Use](https://pablocaro.es/en/extensiones-pi-que-uso)** — My real setup with packages, skills, and custom extensions.

*Source*: [pi.dev](https://pi.dev/)
