---
title: Detecting secrets in git with gitleaks
slug: gitleaks-deteccion-secrets-git
lang: en
date: 2026-05-28
category: tools
tags: git, security, gitleaks, tools, cli
featured_image: /images/gitleaks-deteccion-secrets-git.png
Summary: gitleaks scans git repositories for secrets, API keys, and leaked credentials. Install it in seconds with gah — it might save you from a very bad day.
---

![gitleaks detecting secrets in a git repo](/images/gitleaks-deteccion-secrets-git.png)

`gitleaks` scans git repositories —including the full commit history— for secrets: API keys, passwords, AWS tokens, database credentials, and over 150 predefined patterns.

## Installing with gah

The fastest way on Linux is with [`gah`](https://github.com/user/gah), a GitHub release asset downloader:

```bash
$ gah install gitleaks/gitleaks
Fetching release info for: gitleaks/gitleaks [latest]
Found release: v8.30.1
Downloading: gitleaks_8.30.1_linux_x64.tar.gz
############################################### 100.0%
Verifying digest sha256 551f6fc8... ...
Digest verification succeeded!
Extracting: gitleaks_8.30.1_linux_x64.tar.gz
Installing: gitleaks
Done!
```

Single binary, zero dependencies, ready in seconds.

## Basic usage

To scan a local repo with full commit history:

```bash
$ gitleaks git --verbose -v /path/to/repo
```

It walks every commit and shows what secrets it found, in which file and at which line.

Some useful flags:

- `--no-banner`: hides the ASCII banner at startup.
- `--exit-code 0`: don't exit with error when leaks are found (handy for CI).
- `--config .gitleaks.toml`: use a custom config with your own detection rules.
- `--gitleaks-ignore-path .`: respects the `.gitleaksignore` file for false positives.
- `--redact`: masks secrets in output (useful for public logs).

You can also scan standalone directories with `gitleaks dir` or pipe content through `gitleaks stdin`.

## When to use it

- **Before making a repo public**: scan the full history to make sure no keys slipped through.
- **In CI/CD**: add it as a GitHub Actions step so the build fails if someone commits a secret.
- **Security audits**: great for reviewing old repos that have been touched by many people.

## Pre-commit hook

The most effective way to use it is as a [pre-commit hook](https://github.com/BadLiveware/pi/blob/main/.githooks/pre-commit) that automatically blocks any commit containing secrets:

```bash
#!/usr/bin/env bash
set -euo pipefail

if [[ "${SKIP_GITLEAKS:-}" == "1" || "${SKIP_GITLEAKS:-}" == "true" ]]; then
  echo "Skipping gitleaks pre-commit scan because SKIP_GITLEAKS=${SKIP_GITLEAKS}." >&2
  exit 0
fi

if ! command -v gitleaks >/dev/null 2>&1; then
  cat >&2 <<'EOF'
gitleaks is required by this repository's pre-commit hook but was not found.
Install gitleaks, or set SKIP_GITLEAKS=1 for an intentional one-off bypass.
EOF
  exit 1
fi

echo "Running gitleaks on staged changes..." >&2
gitleaks protect --staged --source . --redact --no-banner
```

Save this as `.githooks/pre-commit`, make it executable (`chmod +x`), and configure git to use that directory:

```bash
git config core.hooksPath .githooks
```

From then on, every `git commit` will scan staged changes for secrets. Need to bypass it once? `SKIP_GITLEAKS=1 git commit`.

It's one of those tools you don't need until you *really* need it. And when that day comes, you'll be glad it's just a `gah install` away.
