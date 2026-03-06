Title: Fixing Rodney Chrome Error on Wayland
Date: 2026-03-06 09:00
Tags: rodney, chrome, wayland, linux, debugging
Lang: en
Category: Problems
Slug: rodney-chrome-wayland-error
Summary: How to fix Rodney crash when starting Chrome on Wayland systems by using the system Chrome.

[Rodney](https://github.com/simonw/rodney/) is a CLI tool created by Simon Willison designed specifically for AI agents to control a Chrome instance using the Chrome DevTools Protocol. It's similar to Vercel's `agent-browser`, but uses CDP instead of Playwright.

## The Problem

Running `uvx rodney open https://google.es` without first starting Rodney with `rodney start` fails because:

1. Rodney tries to start Chrome with the Chromium it automatically downloads to `~/.cache/rod/browser/`
2. That Chromium (v128.0.6568.0) has a known bug with the Ozone backend on Wayland systems
3. The crash occurs due to the combination of flags `--single-process` + `--ozone-platform=headless`
4. The error in the logs shows: `gl_factory_ozone.cc(62): "Expected Mock or Stub, actual:0"`

## The Solution

The easiest way to fix this is to configure Rodney to use your system's Chrome instead of the automatically downloaded Chromium. This is done via the `ROD_CHROME_BIN` environment variable:

```bash
# Add to ~/.bashrc or ~/.zshrc
echo 'export ROD_CHROME_BIN=/usr/bin/google-chrome' >> ~/.bashrc
source ~/.bashrc
```

After setting this up, Rodney will work correctly:

```bash
uvx rodney start
uvx rodney open https://google.es
```

## Working example

Once configured, the workflow looks like this:

```bash
~/src/anotaciones [cv|…2] 
09:39 $ uvx rodney start
Chrome started (PID 2981885)
Debug URL: ws://127.0.0.1:34373/devtools/browser/319c905a-83a2-47d9-a6e0-8e6a4f2ff830
~/src/anotaciones [cv|…2] 
09:39 $ uvx rodney open https://google.es
Google
~/src/anotaciones [cv|…2] 
09:39 $ uvx rodney screenshot
screenshot.png
~/src/anotaciones [cv|…3] 
```

![Rodney working example]({static}/images/rodney_example.png)

## Why does this happen?

The Chromium that Rodney downloads automatically has a known bug with the Ozone backend on Linux systems that use Wayland (the alternative to X11). When certain Chrome flag combinations are used, the process fails because the graphics system isn't configured as "Mock" or "Stub" (which is what the development builds expect).

Using the system Chrome avoids this problem because:
- System Chrome is compiled with full Wayland support
- It's generally a more stable and updated version
- It doesn't have the same development flags that cause conflicts

## Link

- [Rodney GitHub Repository](https://github.com/simonw/rodney/)
