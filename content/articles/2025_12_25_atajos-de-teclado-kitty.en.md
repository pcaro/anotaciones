---
title: Essential Keyboard Shortcuts in Kitty: Mastering Your Terminal
date: 2025-12-25 12:15
tags: kitty, terminal, shortcuts, keyboard, productivity
lang: en
category: Systems
slug: atajos-de-teclado-kitty
summary: A quick guide to the most useful Kitty keyboard shortcuts to optimize your command-line workflow.
---

**Kitty** is a terminal that shines for its performance and high customizability, but where it truly excels is in its keyboard-driven interface. Mastering its shortcuts will allow you to navigate, manage, and manipulate your terminal sessions with amazing efficiency.

## Discover Your Shortcuts: `show_shortcuts`

The fastest way to know all the keyboard shortcuts configured in your Kitty instance is by using its own functionality:

```bash
kitty +kitten show_shortcuts
```

This will open an interactive window where you can see all shortcuts, both the default ones and those customized in your `kitty.conf`.

## Essential Shortcuts for Every Day

Here are some of the most useful shortcuts that will help you optimize your workflow the most:

### Window and Split Management (Panes)

*   `ctrl+shift+enter`: Opens a new Kitty window.
*   `ctrl+shift+w`: Closes the current Kitty window.
*   `ctrl+shift+o`: Splits the current window vertically (new pane to the right).
*   `ctrl+shift+e`: Splits the current window horizontally (new pane below).
*   `ctrl+shift+f`: Toggles between split panes (focus).
*   `ctrl+shift+[` / `ctrl+shift+]`: Navigates between panes (left/right).
*   `ctrl+shift+alt+[` / `ctrl+shift+alt+]`: Moves the active pane (left/right).

### Tab Management

*   `ctrl+shift+t`: Opens a new tab.
*   `ctrl+shift+q`: Closes the current tab.
*   `ctrl+shift+.`: Moves to the next tab.
*   `ctrl+shift+,`: Moves to the previous tab.
*   `ctrl+shift+alt+.`: Moves the current tab to the right.
*   `ctrl+shift+alt+,`: Moves the current tab to the left.

### Copy and Paste

Kitty has its own copy/paste implementation, which can be more reliable than the system one when working in remote environments or with multiplexers:

*   `ctrl+shift+c`: Copies the selected text to the system clipboard.
*   `ctrl+shift+v`: Pastes text from the system clipboard.

### Font and Appearance Control

*   `ctrl+shift+=` (or `+`): Increases the font size.
*   `ctrl+shift+-`: Decreases the font size.
*   `ctrl+shift+backspace`: Resets the font size to the default value.
*   `ctrl+shift+k`: Enters "scrollback" mode (to search or select historical text).

## Customizing Your Shortcuts in `kitty.conf`

You can add or modify keyboard shortcuts in your configuration file `~/.config/kitty/kitty.conf` using the `map` directive. For example, to map `F1` for a custom script:

```
map f1 launch --type=overlay bash -c "my_custom_script.sh"
```

Mastering these shortcuts will transform your interaction with the terminal, making it more fluid and intuitive. Experiment and customize Kitty to perfectly adapt to your work style!
