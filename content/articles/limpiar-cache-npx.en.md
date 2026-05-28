---
title: Cleaning up npx's hidden cache
slug: limpiar-cache-npx
lang: en
date: 2026-05-28
category: tools
tags: npm, npx, terminal, tools
featured_image: /images/limpiar-cache-npx.png
Summary: npx leaves a hidden package cache in ~/.npm/_npx/. Here's how to list what you've accumulated and clean it up.
---

You run `npx howcode` to try out a tool, it doesn't convince you, and you move on. Do this a few times and, without realizing it, you've got hundreds of megabytes sitting in a cache you didn't even know existed.

![Cleaning up npx's hidden cache](/images/limpiar-cache-npx.png)

## The problem

Every time you run `npx <package>`, npm downloads the package and stores it in `~/.npm/_npx/`. This isn't like `npm install` — there's no `package.json` or `node_modules` you can inspect. It's an opaque cache that keeps growing without you noticing.

After playing around with a few tools, here's what I had:

```bash
$ npm cache npx ls
06d0829110b3b3f: skill
135b94ef511a5b29: pi-kanban
1bf0be162bc0d832: @mvanhorn/printing-press
483d2954a4c5190c: madge
69c381f8ad94b576: vitest
7439c0f00f94bc1a: snipgrapher
9126f0a380537b3d: howcode   # 237 MB for this one alone
```

## The trap

Your first instinct is `npm cache npx rm vitest howcode` and call it a day. Not so fast:

```bash
$ npm cache npx rm vitest snipgrapher howcode
npm error code EUSAGE
npm error Invalid npx key vitest
```

`npm cache npx rm` only accepts the hex hash, not the package name. You need to copy the key from the first column:

```bash
$ npm cache npx rm 9126f0a380537b3d 7439c0f00f94bc1a 69c381f8ad94b576
Removing npx key at /home/pcaro/.npm/_npx/9126f0a380537b3d
Removing npx key at /home/pcaro/.npm/_npx/7439c0f00f94bc1a
Removing npx key at /home/pcaro/.npm/_npx/69c381f8ad94b576
```

If you want to nuke everything at once, `npm cache clean` wipes the entire npm cache (including npx's). More drastic, but faster.
