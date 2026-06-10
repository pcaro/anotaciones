Title: AgentsView: local analytics for your coding agents
Date: 2026-06-10
Category: Tools
Tags: agentsview, ai, coding agents, analytics, claude code, pi, codex, open-source
Slug: agentsview-analytics-agentes
Lang: en
Summary: AgentsView is an open-source tool that indexes sessions from 20+ coding agents into a local SQLite database, providing analytics dashboards, cost tracking, and full-text search without sending data off your machine.
Featured_image: /images/agentsview-dashboard.png

If you use multiple coding agents (Claude Code, Codex, Pi, Cursor...) you know the feeling of losing track of what you've spent, which tools you use most, or which project eats up most of your time. Each agent stores sessions in its own format and directory, and until now there was no unified way to see everything together.

[AgentsView](https://github.com/kenn-io/agentsview) fixes this. It's an open-source tool (Go + Svelte 5, MIT) that indexes all your coding agent sessions into a local SQLite database and gives you analytics dashboards, cost tracking, and full-text search. No accounts, no telemetry, no data leaving your machine.

![AgentsView dashboard](/images/agentsview-dashboard.png)

## Installation

```bash
# macOS / Linux
curl -fsSL https://agentsview.io/install.sh | bash

# Or via Homebrew (desktop app)
brew install --cask agentsview
```

Once installed, start the server and open the dashboard at `http://127.0.0.1:8080`:

```bash
agentsview serve
```

On first run it automatically discovers sessions from all agents installed on your machine.

## What you get

- **Cost dashboard**: daily spend by agent and model, priced via LiteLLM. It also accounts for cache tokens (both creation and read).
- **Activity heatmap**: visualize your most productive days and hours.
- **Full-text search (FTS5)**: search across all your past session content. Perfect for recovering that command or solution you used weeks ago.
- **Session viewer**: browse sessions one by one, export to HTML, or publish as a GitHub Gist.
- **Per-project stats**: tokens used, most frequent tools, average session duration.
- **Live updates via SSE**: if you have active sessions, the dashboard updates automatically.

## CLI for costs

Beyond the web dashboard, it has a fast CLI that replaces `ccusage`:

```bash
# Daily cost summary (last 30 days)
agentsview usage daily

# Per-model breakdown
agentsview usage daily --breakdown

# Filter by agent and date range
agentsview usage daily --agent claude --since 2026-05-01

# JSON output for scripting
agentsview usage daily --json
```

Since data is already indexed in SQLite, queries are way faster than re-parsing session files every time.

## Supported agents

AgentsView auto-discovers sessions from 20+ agents: Claude Code, Codex, Pi, Cursor, Copilot CLI, Gemini CLI, OpenCode, OpenHands, Qwen Code, Kimi, Warp, Forge, Zencoder, and many more. The full list is in the [README](https://github.com/kenn-io/agentsview#supported-agents).

## PostgreSQL for teams

If you work in a team, you can sync data to a shared PostgreSQL instance:

```bash
agentsview pg push --watch   # continuous sync
agentsview pg serve           # serve UI from PostgreSQL
```

The PostgreSQL-mode UI is read-only, so anyone on the team can view dashboards without modifying data.

## What it doesn't do

- It doesn't send data to any external server. The only optional outbound traffic is an update check on startup (disabled with `--no-update-check`).
- No account or login required.
- It doesn't replace the agent itself. It's an analytics layer on top of what you already have.

AgentsView fills a real gap in the coding agent ecosystem: unified visibility into how and how much you use these tools. If you use more than one agent, it's worth installing.
