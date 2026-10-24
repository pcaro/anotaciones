Title: pi-claude-bridge: your Claude Pro/Max subscription inside pi
Date: 2026-10-24
Category: Tools
Tags: pi, claude, claude-code, coding-agent, subscriptions, cli
Slug: pi-claude-bridge
Lang: en
Summary: pi-claude-bridge wires pi to the Claude Code Agent SDK so you can use Opus, Sonnet and Haiku from your Pro or Max subscription as regular pi models, with no API key and every tool call flowing through pi's TUI.
Featured_image: /images/pi-claude-bridge.png

At work my model budget is the Claude subscription. Before this I had two options: open Claude Code in another tab, or put a separate API key into pi and pay twice. [pi-claude-bridge](https://github.com/elidickinson/pi-claude-bridge) solves exactly that: Claude models show up in pi's `/model` and the conversation spends your subscription quota instead of billed tokens.

![pi-claude-bridge repository](/images/pi-claude-bridge.png)

## What it actually is

It's a pi extension built on the [Claude Code Agent SDK](https://github.com/anthropics/claude-agent-sdk-typescript). It started as a fork of Prateek Sunal's `claude-agent-sdk-pi` and does two things:

1. **Provider** — Registers a `claude-bridge` provider with the Claude models from pi-ai's catalog. Every tool call flows through pi's TUI, so you see what you'd see with any other model.
2. **`AskClaude` tool** — Lets you delegate a question to Claude Code while running another provider. It's marked deprecated.

```bash
pi install npm:pi-claude-bridge
```

Requires pi 1.2.0 or newer for all models to be available.

## Using it as a provider

```bash
/model claude-bridge/claude-opus-5
```

That's it. Behind the scenes pi translates its tools into Claude Code's format, so the workflow doesn't change: same tools, same session, same subagents. A few things do change and are worth knowing:

- **Bash gets a 120-second timeout**, Claude Code's default. pi's bash has no timeout of its own, so it inherits the bridge's.
- **Skills are forwarded** into Claude Code's system prompt.
- **Mid-turn steering** reaches Claude at the next tool boundary, not immediately.
- **The model list is pi-ai's**. When pi-ai adds a Claude model it appears in `/model` after you update the package, without waiting for a bridge release. Dated snapshot ids (`claude-opus-4-5-20251101`) are hidden.

## 1M context

A million-token context isn't available the same way on every plan, and the bridge needs to know yours. It's configured in `~/.pi/agent/claude-bridge.json`:

```json
{
  "provider": {
    "plan": "max",
    "longContextExtraUsage": false
  }
}
```

With `plan: "pro"` (the default) you get 1M on Fable 5/5.1, Opus 5.5/5/4.8/4.7 and Sonnet 5.5/5. Opus 4.6 only reaches 1M on a Max plan or with Extra Usage, and Sonnet 4.6 only with Extra Usage. If your plan advertises 1M but Claude Code won't serve it, `forceTwoHundredK` pins specific models to 200K:

```json
{
  "provider": {
    "plan": "max",
    "forceTwoHundredK": ["claude-opus-4-6"]
  }
}
```

## The rest of the config

```json
{
  "provider": {
    "strictMcpConfig": true,
    "autoMemoryEnabled": false,
    "pathToClaudeCodeExecutable": "/home/you/.nix-profile/bin/claude"
  },
  "askClaude": {
    "enabled": false,
    "defaultMode": "read",
    "allowFullMode": true
  }
}
```

`strictMcpConfig` is on by default and blocks MCP servers from `~/.claude.json` and `.mcp.json`. That makes sense: if you already have MCP in pi, loading Claude Code's on top duplicates tools and burns context. Cloud MCP (Gmail, Drive via claude.ai OAuth) is always blocked.

`pathToClaudeCodeExecutable` is for when the SDK's bundled binaries can't run on your system. Nix is the classic case: point it at the `claude` from your profile.

## What to know before using it

This is not just another provider, and it has traps the repo documents. The important ones:

**Rebuilding a session re-sends the whole conversation.** The bridge rewrites Claude Code's session from pi's history whenever the two diverge: after an abort, a `/compact`, tree navigation, an API error, or on returning to a session. The next request usually misses the prompt cache for everything past the system prompt. In abort-heavy sessions you feel it in the bill.

**Files Claude Code edits don't survive a rebuild.** The edit itself does, it stays in the history as a tool call and result. What's lost is the file snapshot after the edit. `@file` expansions are preserved.

**System prompt changes mid-session may not reach the model.** Claude Code records the first request's prompt (project context, skills, extension instructions) and reuses it on resume. That keeps the cached prefix stable, but if you edit `AGENTS.md` mid-session it may not take effect until a rebuild or compaction.

**Exported `ANTHROPIC_*` variables hijack the child process.** An `ANTHROPIC_BASE_URL`, `ANTHROPIC_API_KEY` or `ANTHROPIC_AUTH_TOKEN` in your environment redirects Claude Code to that gateway and every turn fails with its auth error. If you have one of those in your `.zshrc`, drop it from the pi process.

**`modelOverrides` from `models.json` doesn't work here.** They only apply to pi-side settings like the compaction threshold. To change `contextWindow` you edit `src/models.ts` or use `forceTwoHundredK`.

## Details that surprised me for the better

**Claude Code hooks keep working.** `~/.claude/settings.json` fires inside bridge turns. That can be useful or a mess: a hook injecting Claude-specific guidance duplicates what your pi extensions already do. The escape hatch is the one the README suggests:

```sh
[ -n "$PI_CODING_AGENT" ] && exit 0
```

pi sets `PI_CODING_AGENT=true` on child processes, so the hook opts itself out when it runs inside pi.

**Compaction is still pi's job.** The bridge routes those calls to isolated Claude Code queries, leaving the live session untouched until pi finishes rewriting the history.

**Plan usage can be read from other extensions.** Claude Code emits a `rate_limit_event` when a usage window changes, and the bridge passes it through the `after_provider_response` event as `anthropic-ratelimit-unified-*` headers, with the same names the Anthropic API uses. An extension that already reads those headers for the native `anthropic` provider can accept `claude-bridge` unchanged.

**Coexistence with subagents.** With `@gotgenes/pi-subagents` you need this in `~/.pi/agent/subagents.json`:

```json
{"promptInheritance": {"claude-bridge": "portable"}}
```

## On billing

Anthropic announced and then un-announced a change to how Agent SDK usage gets billed. As of today this extension spends your subscription quota just like Claude Code. That's why I use it at work and not at home: where I have Claude paid for, the bridge pays off; where I don't, it makes no sense.

## How I use it

On the work machine I have Claude paid for and pi is my harness. `claude-bridge` lets me stay in pi without giving up the models I already pay for, and without a loose API key lying around. The TUI is pi's, the tools are pi's, the skills are pi's, and underneath the thing talking to Anthropic is Claude Code with my session.

The real downside is abort-heavy sessions, where the bridge pays the price of rebuilding history. I accept it: my normal flow has few aborts, and in exchange I don't have to choose between the agent I like and the model I've paid for.

At home the setup is the opposite: an OpenCode Go subscription and [pi-provider-opencode-console](https://pablocaro.es/en/pi-provider-opencode-console) for a live model catalog.

## Resources

- [pi-claude-bridge on GitHub](https://github.com/elidickinson/pi-claude-bridge) — Code, config and known issues
- [On npm](https://www.npmjs.com/package/pi-claude-bridge) — `pi install npm:pi-claude-bridge`
- [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-typescript) — The foundation it builds on
- [claude-agent-sdk-pi](https://github.com/prateekmedia/claude-agent-sdk-pi) — The project it came from
- [The OpenCode bridge](https://pablocaro.es/en/pi-provider-opencode-console) — The other provider extension I use
