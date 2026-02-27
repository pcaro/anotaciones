Title: Record and Share your Terminal Sessions with asciinema
Date: 2026-02-27 12:00
Tags: asciinema, terminal, linux, productivity
Lang: en
Category: Tools
Slug: asciinema-terminal-recorder
Summary: Discover asciinema, the perfect tool to record your terminal sessions in a lightweight, reproducible, and easy-to-share way.

Often we need to share what's happening in our terminal, whether for a tutorial, demonstrating a bug, or simply documenting a process. While traditional video recording tools exist, **asciinema** offers a much more powerful and lightweight alternative.

## What is asciinema?

[asciinema](https://github.com/asciinema/asciinema) doesn't record video in the traditional sense (pixels). Instead, it captures the terminal's text stream along with exact timings. This has several advantages:

- **Tiny files**: Instead of megabytes of video, you get very small text files.
- **Selectable text**: When playing back a session on the web, you can copy and paste the code directly.
- **Perfect quality**: No loss of resolution or compression artifacts.

## Installation and Help

I already have `asciinema` installed on my system. Here you can see the summary of available commands:## Interactive example

Below you can see a small demonstration of `asciinema` in action, running the command `cowsay Muuuuu`:

<link rel="stylesheet" type="text/css" href="/theme/asciinema-player/asciinema-player.css" />
<div id="demo-player"></div>
<script src="/theme/asciinema-player/asciinema-player.js"></script>
<script>
    window.addEventListener('load', function() {
        AsciinemaPlayer.create('/images/demo.cast', document.getElementById('demo-player'), {
            cols: 80,
            rows: 10,
            autoPlay: true,
            loop: true
        });
    });
</script>

## Basic commands

To start recording, simply run:

```bash
asciinema rec demo.cast
```

This will begin recording everything that happens in your current terminal session. When you're finished, simply press `Ctrl-D` or type `exit`. The result will be saved in the `demo.cast` file.

To play it back locally:

```bash
asciinema play demo.cast
```

And if you want to share it with the world, you can upload it to their free hosting service:

```bash
asciinema upload demo.cast
```

## Why use it?

It's ideal for developers writing technical blogs (like this one), as it allows you to embed the recordings directly into the browser with a lightweight JavaScript-based player. Goodbye, blurry 20MB GIFs!

![asciinema help]({static}/images/asciinema_help.png)
