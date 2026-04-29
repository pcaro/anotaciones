---
title: marksman: LSP para Markdown
date: 2026-04-29 22:46
tags: markdown, lsp, fresh, editor, herramientas, linux
lang: es
category: Herramientas
slug: marksman-lsp-markdown
summary: marksman es un servidor de protocolo de lenguaje (LSP) para Markdown que añade autocompletado, navegación entre archivos y detección de errores a cualquier editor compatible.
featured_image: /images/marksman-splash.png
---

Escribo bastante en Markdown — este blog, notas, documentación — y hasta ahora me las apañaba sin más. Pero tras acostumbrarme a los beneficios del LSP en código, empecé a echar en falta algo similar para mis archivos `.md`. Enlaces rotos, referencias a notas inexistentes, falta de autocompletado entre documentos... todo eso se acumula cuando mantienes varios ficheros.

Así que he instalado **marksman**, un servidor LSP dedicado exclusivamente a Markdown.

![Marksman splash](/images/marksman-splash.png)

## ¿Qué es marksman?

marksman es un [servidor de protocolo de lenguaje](https://microsoft.github.io/language-server-protocol/) (LSP) que entiende la estructura de tus documentos Markdown. No solo resalta sintaxis: analiza enlaces internos, referencias entre archivos, títulos, tablas de contenido y mucho más.

Algunas de las funciones que ofrece:

- **Autocompletado** de enlaces internos entre archivos Markdown.
- **Ir a definición** (F12) para saltar a la sección o archivo referenciado.
- **Renombrar símbolos**: cambia un título y actualiza todos los enlaces que apuntan a él.
- **Detección de errores**: alerta sobre enlaces rotos o referencias inexistentes.
- **Información flotante** (hover) para previsualizar contenido de enlaces.
- **Búsqueda de referencias** para ver dónde se usa un título o archivo.

Básicamente, convierte un conjunto de archivos Markdown en algo parecido a un proyecto de código, con todas las ventajas de navegación y refactorización que eso conlleva.

## Instalación

Lo he instalado con [gah](https://github.com/pablocaro/gah) (GitHub Asset Helper), una herramienta que uso habitualmente para bajar binarios de releases de GitHub:

```bash
gah install artempyanykh/marksman
```

Seleccioné la versión `marksman-linux-x64` y en cuestión de segundos ya tenía el binario disponible en el PATH.

También se puede instalar vía Homebrew, Snap, o descargando el binario directamente desde las releases del proyecto.

## Configuración en `fresh`

Lo uso junto a [`fresh`]({filename}/articles/2025_12_25_fresh-editor-terminal.md), mi editor de terminal preferido. `fresh` tiene soporte LSP nativo, así que solo tuve que asegurarme de que `marksman` esté en el PATH. Al abrir un archivo Markdown, `fresh` detecta automáticamente el servidor y ofrece iniciarlo:

![Menú LSP en fresh](/images/marksman-fresh-lsp.png)

Una vez arrancado, el menú LSP de `fresh` muestra todas las opciones disponibles:

![Opciones del menú LSP](/images/marksman-fresh-menu.png)

## ¿Por qué me convence?

No necesito un editor gráfico pesado para escribir Markdown con comodidad. Con `marksman` + `fresh` tengo autocompletado de enlaces, navegación rápida entre notas, y detección de errores sin salir de la terminal. Es especialmente útil en este blog, donde hay decenas de artículos referenciándose entre sí.

Si trabajas habitualmente con Markdown y usas un editor con soporte LSP, `marksman` es una de esas herramientas que, una vez instaladas, te preguntas cómo has podido vivir sin ellas.

*Repositorio oficial*: [marksman en GitHub](https://github.com/artempyanykh/marksman)
