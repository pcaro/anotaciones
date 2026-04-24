Title: Trying Aurora: my first look at the future of the Linux desktop
Date: 2026-04-24 09:51
Category: Linux
Tags: aurora, linux, kde, desktop, devcontainers, homebrew
Slug: probando-aurora-mi-primer-vistazo-al-futuro-del-escritorio-linux
Lang: en
featured_image: /images/aurora-desktop-2026-04-24.png
Summary: Aurora: Image-based, atomic updates, devcontainers, homebrew, and the whole DX experience I'm testing in a VM.

I've always been a KDE user. With SUSE or Debian distros. For the past few years, my main desktop has been KDE Neon.

But lately, I've been following the [Aurora](https://getaurora.dev/en/) project and decided to give it a try in a virtual machine. And I have to say it: it looks very promising.

## What is Aurora?

Aurora is a Fedora-based Linux distribution that's rethinking how a modern desktop should work. It's not just "another distro with KDE" — it's a complete paradigm shift.

The first thing that stands out is that it uses an **image-based model**. Instead of updating individual packages with `dnf` or `apt`, the entire operating system updates as an atomic image. This means:

- **Background updates** that apply on reboot
- **Instant rollback** if something goes wrong (you can boot into the previous version from grub)
- **Immutable system** that's much harder to break

For someone coming from a traditional system, with many years behind them, this is a huge change.

## KDE, but different

Aurora uses KDE Plasma, but it's not the simple original KDE that used to be found in Fedora (never the best distro for this GUI).
It's carefully customized to offer an "out of the box" experience that just works. No need to configure anything, no tweaks or weird adjustments needed.

And yet, it keeps the essence of KDE: it's flexible, it's powerful, and it feels familiar from day one.

## Aurora DX: the real attraction

But where Aurora really shines is in the **Developer Experience (DX)**. I've been tinkering with this for days, and every time I discover something new, it seems like a good decision.
That said, I have to keep in mind that I have a lot of Linux behind me and it's hard to change old habits.

### Devcontainers by default

The preinstalled IDE is Visual Studio Code with the **DevContainers** extension already configured. All development happens inside containers, not on the host. This means:

- Your operating system doesn't get cluttered with project dependencies
- Each project can have its own isolated environment
- You can discard and recreate environments in seconds

### Homebrew integrated

Aurora includes **Homebrew** preinstalled and configured to not touch the base system. Want a new CLI tool? `brew install`. Done. No conflicts with system packages, no sudo needed, no breaking anything. You know I like to keep some small tools very up to date and use gah to install.

They even have `ujust bbrew` that gives you an interactive menu to install entire categories of tools: fonts, k8s-tools, ai, cncf...

### ujust: commands that simplify life

`ujust` is like a super-powered alias. Commands like:

```bash
ujust devmode        # Enable developer mode
ujust dx-group       # Add you to the necessary groups
ujust jetbrains-toolbox  # Install JetBrains Toolbox
ujust cncf           # Browse and install CNCF tools
```

Each command guides you step by step. It's like having an assistant that knows exactly what you need.

### Tailscale and cloud-native tools

Tailscale comes preconfigured for VPN. Cockpit for system management. Profiling tools like `sysprof`, `bcc`, `bpftrace`. Everything you'd need for cloud-native development is there, ready to use.

### Terminal with container support

The default terminal is **Ptyxis**, which has native integration with Distrobox. You can have interactive "pet" containers and switch between them and the host with a shortcut. It's very convenient.

## The big differences

In Aurora, the system takes care of itself:

1. **You can't easily break it** — the base system is immutable
2. **Updates are atomic** — they either work completely, or they don't apply
3. **Everything is in containers** — your tools, your environments, your dependencies
4. **If something fails, there's rollback** — boot the previous version and you're done

It's like the difference between tending a garden and staying in a hotel. In a hotel, everything just works.

## Will I leave KDE Neon?

I don't know yet. I've been on KDE Neon for years and have my workflow set up. But Aurora is making me rethink things.

What's pulling me in:

- **The DX** is simply superior for modern development
- **Automatic updates** without having to keep track
- **The philosophy** of "everything in containers" makes a lot of sense

What scares me:

- **The immutability** — feels restrictive at first
- **The mindset shift** — letting go of total control
- **What if I need something specific? (which will surely happen)** — though with homebrew and containers, probably not much

---

**Links:**

- [Aurora Website](https://getaurora.dev/en/)
- [Aurora DX Documentation](https://docs.getaurora.dev/dx/aurora-dx-intro/)
- [Universal Blue (the project behind)](https://universal-blue.org)
