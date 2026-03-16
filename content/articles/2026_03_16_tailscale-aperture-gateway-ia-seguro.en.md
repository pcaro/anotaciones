Title: Tailscale Aperture: AI Gateway Without Distributing API Keys
Date: 2026-03-16 10:00
Category: Tools
Tags: tailscale, security, ai, api, gateway
Slug: tailscale-aperture-gateway-ia-seguro
Lang: en
featured_image: /images/tailscale-aperture.png
Summary: Tailscale's Aperture centralizes LLM access by eliminating the need to distribute API keys to developers, using Tailscale identity for authentication.

One thing that kept me up at night when I started using LLMs at work was: **where do I store the API keys?** In private repos, in `.env` files I forgot to gitignore, in phone notes... A mess.

Tailscale recently announced [Aperture](https://tailscale.com/docs/features/aperture), an AI gateway that runs inside your tailnet and completely eliminates that problem.

## The Problem with Distributed API Keys

When developers need access to OpenAI, Anthropic, or any other LLM provider, the common practice has been:

1. Create an API key
2. Share it via Slack, email, or pasted in a private repo
3. Pray it doesn't leak
4. When someone leaves, manually rotate all keys

This doesn't scale. An organization with 50 developers can have hundreds of keys floating around in documents, CI/CD scripts, and developer machines that are no longer at the company.

## Aperture: Centralization with Real Identity

Tailscale's solution is elegant: **use tailnet identity for authentication, not distributed keys**.

How it works:

1. **Configure Aperture in your tailnet** with your provider API keys (OpenAI, Anthropic, Google, OpenRouter, etc.)
2. **Developers connect to Aperture** using their Tailscale identity
3. **Aperture injects the credentials** for the corresponding provider and forwards the request
4. **Complete telemetry**: tokens used, costs, sessions, all in a dashboard

Developers never see the real API keys. Aperture keeps them centralized and injects them server-side.

## Integration with Existing Tools

The good news is it works with the tools you already use:

- **Claude Code**: Set `ANTHROPIC_BASE_URL=http://ai` and you're done
- **Codex**: Base URL to Aperture
- **Gemini CLI, Roo Code, Cline**: Similar, change the base URL
- **Custom apps**: Works with any client using OpenAI-compatible APIs

From the client's perspective, Aperture looks like the provider itself. It detects the model in the request body and routes to the correct provider.

## pi-ts-aperture: Plugin for Pi

There's an official Pi plugin to automatically route through Aperture:

```bash
pi install npm:@aliou/pi-ts-aperture
/aperture:setup
```

The wizard asks for:
1. Your Aperture URL (e.g., `ai.your-tailnet.ts.net`)
2. Which providers to route

It saves configuration to `~/.pi/agent/extensions/aperture.json` and modifies providers to use Aperture as proxy.

## Visibility and Control

Aperture'sdashboard gives you:

- **Tokens by model and user**: How much does each person spend?
- **Grouped sessions**: A Claude Code session can have50 requests; you see them as a coherent unit
- **Tool use**: Which tools are being invoked and how frequently
- **Adoption**: Who's using what, and who tried once and didn't come back
- **Export to S3**: To integrate with your usual SIEM

For platform or security teams that need auditing, this is gold.

## Requirements

- A Tailscale tailnet (fundamental, all authentication depends on Tailscale identity)
- API keys for the providers you want to use
- The device running Pi must be on the tailnet

## In Summary

If your organization is adopting AI tools and you don't want to deal with API keys circulating everywhere, Aperture is a clean solution. It centralizes credentials, gives real visibility into usage, and uses the identity infrastructure you already have with Tailscale.

It's still in alpha, but available for free during the testing period. Worth trying if you already use Tailscale.