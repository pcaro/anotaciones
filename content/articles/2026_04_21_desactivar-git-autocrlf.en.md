Title: Disable git autocrlf
Date: 2026-04-21 12:00
Category: Git
Tags: Git, Windows, WSL, Line Endings
Slug: disable-git-autocrlf
Lang: en
featured_image: /images/git-disable-autocrlf.png
Summary: If you use Windows (or WSL), Git has been silently converting your line endings. One command fixes it.

If you're on Windows, Git has been silently messing with your line endings since the day you installed it. The culprit is `core.autocrlf`, enabled by default.

```bash
git config --global core.autocrlf false
```

## What `core.autocrlf` does

Windows has historically used `CRLF` (`\r\n`) as its line ending character, while Linux and macOS use plain `LF` (`\n`). With `autocrlf true` (the default on Windows):

- On **checkout**: Git converts `LF` line endings in the repository to `CRLF` in your working directory
- On **commit**: Git converts `CRLF` back to `LF` before storing the file

In theory, your local files always have Windows-style line endings and the repository stays clean with Unix-style endings. In practice, it's a constant source of problems.

## Why it's a bad default

**WSL makes it worse.** Your Linux environment expects `LF` line endings. Windows Git has helpfully checked out everything with `CRLF`. The result: every script and config file has a stray `\r` at the end of every line, causing silent failures. And if you haven't seen this warning, you've probably started ignoring it:

```
warning: LF will be replaced by CRLF in some-file.sh.
The file will have its original line endings in your working directory
```

**Modern editors handle LF just fine.** The original argument was that Notepad couldn't handle `LF`-only files — which was true in 2003. Notepad has supported `LF` line endings since Windows 10 (2018). VS Code, Sublime, Vim, IntelliJ, Notepad++ — they've all handled it fine for even longer.

**The conversion is lossy in practice.** Binary files can get corrupted if Git misidentifies them as text. If some people on a team have `autocrlf true` and others have it `false`, you'll end up with commits that are just line ending changes.

## The fix: disable it and use `.gitattributes`

```bash
git config --global core.autocrlf false
```

From then on, Git leaves your line endings exactly as they are — no silent conversions. For teams, a `.gitattributes` file in the repository is a much better approach, since it applies the same rules for everyone regardless of their local config.

Use `LF` everywhere, configure your editor to save with `LF` by default. Don't think about it again (until you change machines).

*Original source*: [Git - Disable autocrlf (Ryan Harrison)](https://ryanharrison.co.uk/2026/04/21/git-disable-autocrlf.html)