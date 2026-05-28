---
title: Limpiando la caché escondida de npx
slug: limpiar-cache-npx
lang: es
date: 2026-05-28
category: herramientas
tags: npm, npx, terminal, herramientas
featured_image: /images/limpiar-cache-npx.png
Summary: npx deja una caché oculta de paquetes en ~/.npm/_npx/. Aquí explico cómo listar lo que tienes acumulado y cómo borrarlo.
---

Ejecutas `npx howcode` para probar una herramienta, no te convence y sigues con tu vida. Repites esto unas cuantas veces y, sin darte cuenta, tienes cientos de megas acumulados en una caché que ni siquiera sabías que existía.

![Limpiando la caché escondida de npx](/images/limpiar-cache-npx.png)

## El problema

Cada vez que haces `npx <paquete>`, npm descarga el paquete y lo guarda en `~/.npm/_npx/`. No es como `npm install` — aquí no hay un `package.json` ni un `node_modules` que puedas inspeccionar. Es una caché opaca que va creciendo sin que te des cuenta.

En mi caso, después de trastear con varias herramientas, tenía esto:

```bash
$ npm cache npx ls
06d0829110b3b93f: skill
135b94ef511a5b29: pi-kanban
1bf0be162bc0d832: @mvanhorn/printing-press
483d2954a4c5190c: madge
69c381f8ad94b576: vitest
7439c0f00f94bc1a: snipgrapher
9126f0a380537b3d: howcode   # 237 MB solo este
```

## La trampa

El primer impulso es hacer `npm cache npx rm vitest howcode` y ya está. Pero no:

```bash
$ npm cache npx rm vitest snipgrapher howcode
npm error code EUSAGE
npm error Invalid npx key vitest
```

`npm cache npx rm` solo acepta el hash hexadecimal, no el nombre del paquete. Tienes que copiar la clave de la primera columna:

```bash
$ npm cache npx rm 9126f0a380537b3d 7439c0f00f94bc1a 69c381f8ad94b576
Removing npx key at /home/pcaro/.npm/_npx/9126f0a380537b3d
Removing npx key at /home/pcaro/.npm/_npx/7439c0f00f94bc1a
Removing npx key at /home/pcaro/.npm/_npx/69c381f8ad94b576
```

Si quieres borrarlo todo de golpe, `npm cache clean` vacía la caché entera de npm (incluyendo la de npx). Más drástico pero más rápido.
