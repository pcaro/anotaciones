---
title: `direnv`: Manage your development environments intelligently
date: 2025-12-25 14:30
tags: direnv, shell, environment, productivity, development, linux, tools
lang: en
category: Tools
slug: direnv-gestion-entornos
summary: Discover `direnv`, a shell extension that automatically loads and unloads environment variables when changing directories, keeping your configuration clean and organized.
---

In the daily life of a developer, it is common to work with multiple projects, each with its own environment variables, paths (`PATH`), tool versions, or credentials. Manually managing these variables can lead to messy configurations in your `.profile` or `.bashrc`, or errors due to using the wrong environment. This is where **`direnv`** shines, offering an elegant and automatic solution.

## What is `direnv`?

`direnv` is an extension for your shell (Bash, Zsh, Fish, etc.) that automatically detects when you change directories. When you enter a directory containing an `.envrc` file, `direnv` loads it; when you leave it, it unloads it. This means your shell environment dynamically adapts to your current project without you having to do anything manually.

## How does it work?

`direnv` integrates with your shell through a hook in the `cd` command. Every time you change directories, `direnv` checks if there is an `.envrc` file in the current directory or any of its ancestors. If it finds one (and you have granted permission to load it), it executes the commands defined in that file to modify your environment. Upon leaving the directory, it reverts those changes, cleaning up your environment.

## Common Use Cases

*   **`PATH` Management**: Adding project-specific binaries to your `PATH` temporarily.
*   **Python Virtual Environments**: Automatically activating a `virtualenv` or `uv venv` when entering a Python project.
*   **Credentials and API Keys**: Loading environment variables with database credentials, API keys, or tokens securely (without leaving them in the shell history).
*   **Project-Specific Environment Variables**: `RAILS_ENV`, `NODE_ENV`, etc.
*   **Tool Version Switching**: Integrating with tools like `nvm` or `pyenv` to automatically switch Node.js or Python versions.

## Basic Installation (Bash example)

1.  **Install `direnv`**: You can install it from your package manager (`sudo apt install direnv`, `brew install direnv`, etc.).
2.  **Activate the hook in your shell**: Add the following line to your `~/.bashrc` (or `~/.zshrc`):

    ```bash
    eval "$(direnv hook bash)"
    ```

3.  **Create an `.envrc` file**: In the root of your project, create an `.envrc` file with the variables and commands you want.

    ```bash
    # .envrc in the root of your Python project
    layout python  # Automatically activates a virtual environment
    export MY_API_KEY="super_secret_project_key"
    ```

4.  **Allow loading**: The first time you enter the directory with a new `.envrc`, `direnv` will ask for confirmation:

    ```bash
    direnv: error .envrc is blocked. Run `direnv allow` to approve its contents
    ```
    Run `direnv allow`.

## The `direnv` Standard Library

`direnv` comes with a powerful standard library that includes predefined functions for common tasks, such as `layout python` (to manage virtualenvs), `use nix`, `use node`, etc., greatly simplifying the configuration of your `.envrc` files.

## Key Benefits

*   **Clean environments**: Your `.profile` stays tidy.
*   **Consistency**: Each project has exactly the environment it needs.
*   **Productivity**: No more manual `source venv/bin/activate` or remembering to set variables.

`direnv` is a small but powerful tool that transforms the way you manage your development environments, making your life in the terminal much more efficient and error-free.

*Original article*: [`direnv` homepage](https://direnv.net/)
