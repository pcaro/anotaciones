Title: rbw sync: missing field `access_token`
Date: 2026-04-11 19:30
Category: Linux
Tags: bitwarden, cli, bug, linux
Slug: rbw-sync-access-token
Lang: en
Summary: Known rbw bug when syncing with Bitwarden or Vaultwarden: "failed to parse JSON: missing field access_token". The fix is to clear the local cache.
featured_image: /images/rbw-sync-access-token.png

Today I ran into this error when trying to sync my Bitwarden vault with **rbw**:

```bash
$ rbw sync
rbw sync: failed to sync database from server: failed to parse JSON: missing field access_token at line 1 column 393
```

![Issue #202 in the rbw repo]({static}/images/rbw-sync-access-token.png)

## Diagnosis

This is a known rbw bug that has existed since 2020 ([#32](https://github.com/doy/rbw/issues/32)) and remains open. It happens with both official Bitwarden and Vaultwarden. It's not related to your Vaultwarden version.

**Cause:** rbw stores a session token locally that gets corrupted or expires. When trying to sync, the server returns a JSON response without the `access_token` field that rbw expects. The local rbw cache ends up in an invalid state.

## Solution

```bash
rbw purge
rbw sync
```

`rbw purge` clears the local vault cache. Then `rbw sync` will ask for your master password and re-download everything from scratch.

## Bug context

- Open since December 2020 ([#32](https://github.com/doy/rbw/issues/32)), 19 👍, no fix
- Reopened in August 2024 ([#202](https://github.com/doy/rbw/issues/202)) with the same symptoms
- The maintainer (doy) hasn't been able to reproduce it → still unfixed
- Tends to happen after adding new entries (TOTP, SSH keys) from another client (browser extension, web vault) and then trying to sync from rbw

**TL;DR:** `rbw purge && rbw sync` and you should be good.
