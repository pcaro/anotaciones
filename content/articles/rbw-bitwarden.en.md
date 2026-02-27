Title: rbw: The Bitwarden terminal client you should be using
Date: 2026-02-26 11:45
Category: Tools
Tags: bitwarden, cli, rust, security, pi-agent
Slug: rbw-bitwarden-cli
Lang: en
Summary: How to install and configure rbw, a Rust implementation of the Bitwarden client, and how to integrate it into your workflows with pi-agent.

While Bitwarden has an official command-line client, it can be slow as it is Node.js-based. For those of us looking for something more agile, [rbw](https://github.com/doy/rbw) is the ideal solution. It is an unofficial Rust implementation that stands out for being extremely fast and for managing vault unlocking through an agent, preventing you from having to enter your master password for every command.

## Installation

The easiest way to install it is by downloading the binary directly from its GitHub releases. I use `gah` for this purpose:```bash
gah install doy/rbw
```

This command will download the `rbw` binary and the `rbw-agent` binary.

## Initial Setup

The first thing is to configure your account and the server:

```bash
rbw login
```

It will ask for your email and the server URL (you can leave it blank if you use the official Bitwarden one or enter the URL of your Vaultwarden instance).

To start using it, unlock the vault:

```bash
rbw unlock
```

Unlike the official client, you don't need to export environment variables with session tokens. The `rbw` agent takes care of everything in the background.

## Basic Usage

To get a password quickly:

```bash
rbw get "Item Name"
```

If there are multiple items with the same name, you can use filters or the ID. You can also get custom fields or the username:

```bash
rbw get "OpenRouter" --folder "APIs"
rbw get --username "Twitter"
```

## Integration with pi-agent

One of the greatest advantages of having a fast and secure CLI client is the ability to integrate secrets into your development tools.

[pi-agent](https://github.com/mariozechner/pi-agent) allows executing commands to obtain API keys dynamically. This avoids having to save keys in plain text configuration files. In your `settings.json`, you can configure access to a key as follows:

```json
{ 
    "type": "api_key", 
    "key": "!rbw get 'OpenRouter'" 
}
```

The `!` prefix tells `pi-agent` to execute the command and use its standard output as the key. Thanks to the `rbw` agent, this command will run instantly without asking for your master password every time, as long as the vault is unlocked.

![rbw help]({static}/images/rbw_help.png)
