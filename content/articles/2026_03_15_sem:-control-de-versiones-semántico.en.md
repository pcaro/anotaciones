Title: sem: Semantic Version Control
Date: 2026-03-15 14:11
Category: Programming
Tags: cli, versioning, rust, tools
Slug: sem-semantic-version-control
Lang: en
featured_image: /images/sem-cli.png
Summary: Discovering sem, a CLI tool that understands your code's semantics and tells you what entities changed, not just what lines.
Status: published

I stumbled upon [sem](https://github.com/Ataraxy-Labs/sem) a few weeks ago and I think it's a brilliant idea. It's a CLI that goes beyond traditional line-by-line diffs and understands the actual structure of your code.

## The difference between lines and entities

When you do a traditional `git diff`, you see something like:

```diff
- const oldAuth = function(user) { ... }
+ const newAuth = async function(user) { ... }
```

But with `sem diff` you see:

```
⊕ function validateToken          [added]
∆ function authenticateUser       [modified]
⊖ function legacyAuth             [deleted]
```

No lines added or deleted — **entities** that changed: functions, classes, methods. Much more useful for understanding what actually happened in the PR.

## Available commands

- **`sem diff`**: Shows what entities changed
- **`sem impact <entity>`**: Analyzes what would break if you change that entity (incoming dependencies)
- **`sem blame`**: Entity-level blame — who changed each function/class
- **`sem graph`**: Shows the dependency graph between entities

## Practical example

```bash
# See what entities changed in working directory
sem diff

# See only staged changes
sem diff --staged

# See changes from a specific commit
sem diff --commit abc1234

# See impact of changing a function
sem impact validateToken

# JSON output for CI pipelines
sem diff --format json
```

## Installation

```bash
# macOS
brew install sem-cli

# Linux (my case)
brew install sem-cli
# or download binary from GitHub Releases
```

Or build from source if you have Rust installed:

```bash
git clone https://github.com/Ataraxy-Labs/sem
cd sem/crates
cargo install --path sem-cli
```

## Why this is useful

For me, mainly two cases:

1. **Faster code reviews** — You understand the real impact of a change in seconds
2. **Safe refactors** — Before renaming a critical function, `sem impact` tells you what might break

Supports 20 languages (including Python, Rust, Go, TypeScript, Java, C++, etc.) using tree-sitter to parse the code.

A tool that goes straight into my daily toolkit.
