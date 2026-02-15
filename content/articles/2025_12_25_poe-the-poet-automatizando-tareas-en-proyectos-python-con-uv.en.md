---
title: Poe the Poet: Automating Tasks in Python Projects with uv
date: 2025-12-25 11:00
tags: python, uv, poethepoet, automation, pyproject.toml
lang: en
category: Programming
slug: poe-the-poet-automatizando-tareas-en-proyectos-python-con-uv
summary: Discover how Poe the Poet allows you to define and execute custom commands directly from your pyproject.toml, optimizing your workflow in uv environments.
---

Managing Python projects often involves executing various custom tasks, from building documentation to running tests or helper scripts. While `uv` has greatly simplified dependency management, how to integrate and execute these commands directly from `pyproject.toml` has been a point of debate. This is where **Poe the Poet** emerges as an elegant and effective solution.

## What is Poe the Poet?

Poe the Poet is a tool that allows you to define custom "scripts" or "tasks" directly in your `pyproject.toml` file. These tasks can be any command you want to run in the context of your Python environment, making workflow automation much cleaner and centralized. It solves the problem of having to resort to `Makefile` or other external scripts for project-specific tasks.

## How to Use Poe the Poet with uv

Integrating Poe the Poet into a project using `uv` is straightforward:

1.  **Add `poethepoet` to your dev dependencies:**
    First, ensure that `poethepoet` is included in your development dependencies group (e.g., `dev`) in `pyproject.toml`.

```toml
[project]
# ... other project configurations ...

[tool.uv]
dev-dependencies = [
    "black",
    "ruff",
    "poethepoet>=0.38.0", # Add Poe the Poet here
]
```

2.  **Define custom tasks:**
    Then, you can add a `[tool.poe.tasks]` section in your `pyproject.toml` to define your custom commands.

```toml
[tool.poe.tasks]
docs = "sphinx-build -M html docs docs/_build"
livehtml = "sphinx-autobuild -b html docs docs/_build"
cog = "cog -r docs/*.md"
```

## Running Tasks with `uv run`

Once Poe the Poet is configured and your tasks are defined, you can easily execute them using `uv run`:

```bash
# To build the documentation
uv run poe docs

# For the live preview server
uv run poe livehtml

# To run the 'cog' command
uv run poe cog
```

## Benefits

*   **Centralization:** All your custom tasks live in `pyproject.toml`, alongside your dependencies.
*   **Integration with `uv`:** Tasks run in the virtual environment managed by `uv`, ensuring all necessary tools are available.
*   **Simplification:** Avoids the need for `Makefile` or complex bash scripts for common tasks.
*   **Consistency:** Promotes a more consistent and shareable workflow among collaborators.

Poe the Poet offers a robust and elegant way to extend the capabilities of `uv` for task automation in Python projects, enhancing the development experience.

*Original article*: [Poe the Poet - Simon Willison's Weblog](https://simonwillison.net/2025/Dec/16/poe-the-poet/#atom-everything)
