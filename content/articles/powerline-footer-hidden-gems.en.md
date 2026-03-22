Title: Hidden gems in pi-powerline-footer
Date: 2026-03-22
Category: DevOps
Tags: pi, terminal, productivity
Slug: powerline-footer-hidden-gems
Summary: Two features of the pi-powerline-footer plugin that go beyond the typical footer with model information.
featured_image: /images/pi-powerline-footer.png
Lang: en

![Screenshot of the pi-powerline-footer plugin](/images/pi-powerline-footer.png)

I've been using [pi-powerline-footer](https://github.com/nicobailon/pi-powerline-footer) for a while, mainly for its main feature: that footer showing useful model info, context, tokens, and cost. But recently I discovered two features that have changed how I work with pi day-to-day.

## Editor Stash: your integrated temporary clipboard

With `Alt+S` you can save the current editor content, clear it, write something quick (for example, a short question to another agent), and when it's done, your original text comes back automatically.

It's perfect when you're in the middle of a complex task and need to make a quick query without losing context. Or when you want to save a code block you'll reuse later.

Plus, you have shortcuts to copy (`ctrl+alt+c`) and cut (`ctrl+alt+x`) the full editor content, and a stash history accessible with `ctrl+alt+h` that persists between sessions.

## Model Profiles: quick navigation between model configurations

This is the feature I use the most right now. With several active providers —mainly [OpenRouter](https://openrouter.ai/) (with its many models), [Google Gemini](https://ai.google.dev/), and [OpenCode](https://opencode.ai/)— switching between models was a mess.

Model Profiles save model + thinking level combinations. I define them in `~/.pi/agent/settings.json`:

```json
{
  "modelProfiles": [
    { "model": "google/gemini-3-pro", "thinking": "high", "label": "Gemini Deep" },
    { "model": "anthropic/claude-opus-4-5", "thinking": "xhigh", "label": "Opus Ultra" },
    { "model": "openai/codex-5.3", "thinking": "low", "label": "Codex Fast" }
  ]
}
```

With `alt+shift+tab` I cycle through profiles and with `ctrl+alt+m` I open a visual selector. The change is instant — no more endless menus searching for the exact model.

It's especially useful with OpenRouter, where the model list is huge. Instead of navigating through all of them, I have my 3-4 preferred configurations and switch between them based on the task.

## The footer is just the beginning

The plugin documentation is full of small utilities: [Working Vibes](https://github.com/nicobailon/pi-powerline-footer?tab=readme-ov-file#working-vibes) for themed loading messages, configurable keyboard shortcuts, git integration... But these two features I've described are the ones that have the most impact on my daily workflow.

If you haven't tried it yet: `pi install npm:pi-powerline-footer` and then `/reload`.
