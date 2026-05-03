---
title: DNS blocking of AliExpress links with NextDNS
date: 2026-05-03 10:01
tags: dns, nextdns, aliexpress, blocking, networking, linux
lang: en
category: Networking
slug: bloqueo-dns-aliexpress-nextdns
summary: Using an overly aggressive DNS blocklist in NextDNS broke AliExpress affiliate links. Diagnosed with dig and fixed by switching to HaGeZi Multi PRO.
featured_image: /images/dns-blocking-nextdns.jpg
---

![DNS blocking illustration](/images/dns-blocking-nextdns.jpg)

I'd been having a weird issue for a few days: AliExpress links from product video descriptions wouldn't load. Firefox kept showing "Server not found". I knew it looked like a DNS block because enabling PIA's VPN (Private Internet Access) made the problem go away.

## The diagnosis

The `dig` command confirmed it immediately:

```bash
# Querying the router (using NextDNS)
$ dig s.click.aliexpress.com @192.168.1.1

;; ANSWER SECTION:
s.click.aliexpress.com. 300	IN	A	0.0.0.0
```

```bash
# Querying Google DNS
$ dig s.click.aliexpress.com @8.8.8.8

;; ANSWER SECTION:
s.click.aliexpress.com. 300	IN	A	23.40.114.185
```

The router was returning `0.0.0.0` for `s.click.aliexpress.com`. That's not an NXDOMAIN —non-existent domain—, it's a deliberate block: the domain resolves to a null IP and the browser can't connect.

With the VPN active, DNS queries went through PIA's servers, which don't apply blocklists, so the links worked fine.

## The cause

The router had **NextDNS** configured with its default blocklist. It blocked malware and phishing just fine, but it was also catching legitimate domains like affiliate redirects. Too aggressive for daily use.

## The fix

The simplest fix would have been to whitelist `s.click.aliexpress.com` in NextDNS and call it a day. But I took the chance to review which list I was using and switched to **HaGeZi - Multi PRO**, which solved the problem anyway.

According to the [official HaGeZi guide](https://github.com/hagezi/dns-blocklists/wiki/FAQ#whatshouldiuse):

| List     | Blocking level      | False positives             |
| -------- | ------------------- | --------------------------- |
| Light    | Relaxed             | None                        |
| Normal   | Relaxed/Balanced    | Almost none                 |
| **Pro**  | **Balanced**        | **Very rare** ← recommended |
| Pro++    | Balanced/Aggressive | Some                        |
| Ultimate | Aggressive          | Common                      |

Multi PRO (~420k domains, ~200k compressed) is the HaGeZi author's **personal recommendation** for effective blocking without issues. It blocks ads, trackers, telemetry, phishing, malware, scams, cryptojacking, and "crap", with very few false positives.

## The key detail: referral domains

HaGeZi's FAQ has an entire section explaining that **referral domains** —affiliate/tracking links like `s.click.aliexpress.com`— are **allowed in all lists**, except for a few that also function as pure trackers and are only blocked in Pro++ and Ultimate.

These domains only activate after a manual user click and aren't used to display ads. Blocking them breaks search result links, deal links, confirmation emails, etc.

## Summary

An overly aggressive DNS blocklist blocks domains that aren't ads or malware, just e-commerce redirect mechanisms. The sweet spot is **Multi PRO**: good privacy protection without breaking everyday functionality.

If I ever need more aggressiveness, the trade-off will be having to manually unblock false positives. For now, Multi PRO works perfectly.

_More info_: [HaGeZi DNS Blocklists](https://github.com/hagezi/dns-blocklists)
