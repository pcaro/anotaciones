Title: From net-tools to iproute2: command equivalents
Date: 2026-03-06 11:30
Tags: linux, networking, iproute2, net-tools, terminal
Category: Linux
Slug: net-tools-to-iproute
Summary: A guide to equivalents between classic net-tools commands (ifconfig, route, arp) and modern iproute2 commands (ip).
Lang: en

Over 30 years with Linux, and it's hard to change what you're already used to. In my case, I've always used **ifconfig**, **arp**, **route**, and **netstat** to configure and diagnose the network. But these commands belong to the **net-tools** package, which has been replaced by **iproute2** years ago.

## net-tools vs iproute2

There are traditionally two ways of configuring the network in Linux:

- **The old way**: with commands like `ifconfig`, `arp`, `route` and `netstat`, which are part of the *net-tools* package
- **The new way**: mostly (but not entirely!) wrapped in a single `ip` command, which is part of the *iproute2* package

It seems like the latter was made "important" in Debian in 2008, which means every release since Debian 5 "lenny" (!) has featured the `ip` command.

I have been slowly training my brain to use the new commands but I sometimes forget some. So, here's a couple of equivalences from the old net-tools package to the new iproute2:

| net-tools | iproute2 | Shorter form | What it does |
|-----------|----------|--------------|--------------|
| `ifconfig` | `ip address` | `ip a` | Show/configure IP addresses |
| `ifconfig -s` | `ip link` | `ip l` | Show link stats (up/down, packet counts) |
| `route` | `ip route` | `ip r` | Show or modify routing table |
| `arp` | `ip neigh` | `ip n` | Show ARP/neighbors table |
| `netstat` | `ss` | `ss` | Show socket statistics |

## Visual comparison

Here's the difference between using `ip a` and `ip -br -c a`:

### `ip a` (full output)

![ip a output](/images/net-tools-ip-a.png)

### `ip -br -c a` (brief and colored output)

![ip -br -c a output](/images/net-tools-ip-br.png)

## My favorite alias

I often alias `ip` to provide much prettier output:

```bash
alias ip='ip -br -c'
```

This provides a much nicer and readable output, as you can see in the second image.

Do you still use the old commands or have you already switched to iproute2?
