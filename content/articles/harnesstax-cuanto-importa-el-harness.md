---
title: HarnessTax: el harness importa menos de lo que crees
slug: harnesstax-cuanto-importa-el-harness
lang: es
date: 2026-09-17
category: ia
tags: pi, opencode, coding-agent, ia, harness, claude-code, codex, benchmarks, agentes-ia
featured_image: /images/harnesstax.png
Summary: El estudio HarnessTax de UC Berkeley y Arena evalúa 21 combinaciones modelo-harness y llega a tres conclusiones sorprendentes. Validan con datos por qué uso pi y OpenCode a diario.
---

Si eliges un coding agent no estás eligiendo solo un modelo: estás eligiendo también su *harness*, el software que gestiona herramientas, contexto y ejecución de tareas. ¿Y si cambiar de harness mejora los resultados o abarata la factura? Esa es la pregunta que se hace [HarnessTax](https://harnesstax.github.io/), un estudio de UC Berkeley y Arena que evalúa 21 pares modelo–harness (Claude Code, Codex CLI y **pi**, con 7 modelos) sobre SWE-bench Lite y Terminal-Bench 2.0: 30 tareas aleatorias por benchmark, 3 intentos por tarea.

![HarnessTax: How Much Does the Harness Matter for Coding Agents?](/images/harnesstax.png)

Sus tres conclusiones principales son bastante sorprendentes:

## 1. El harness apenas afecta la tasa de éxito, pero sí el coste

El mismo modelo logra tasas de éxito casi idénticas en harnesses distintos, pero el coste puede variar hasta **5x**. El caso más claro: Claude Fable 5 resuelve el 97.8% de intentos en Claude Code y el 96.7% en pi... pero Claude Code cuesta el doble ($1.33 frente a $0.67). En media, Claude Code sale **2x más caro que pi** en SWE-bench Lite y 1.5x en Terminal-Bench 2.0. A esa diferencia de precio por calidad prácticamente igual la llaman, con muy buen nombre, *harness tax*.

## 2. Un harness simple puede ser competitivo

Pi llega a la **frontera de Pareto en ambos benchmarks** aportando solo cuatro herramientas: `read`, `write`, `edit` y `bash`. La clave está en el arranque: el contexto inicial de Claude Code es de media **más de 10 veces el de pi**, con instrucciones más largas y esquemas de herramientas más gordos. Ese sobrecoste se paga en cada llamada al modelo. Menos andamiaje, mismo resultado.

## 3. Los modelos rinden mejor fuera del harness de su proveedor

Este es el más rompedor. Aunque OpenAI diga que GPT-5-Codex está optimizado para Codex, en **9 de las 12 comparaciones entre modelos de Anthropic y OpenAI, la mejor tasa de éxito se consigue con un harness alternativo** al de su proveedor. Por ejemplo, GPT-5.6 Sol consigue un 83.3% de éxito en pi frente al 78.9% en Codex... a mitad de precio. Las capacidades de un modelo son portables; el acoplamiento proveedor-harness no garantiza nada.

## Lo que esto significa para mí

Para cualquiera que use coding agents a diario, la moraleja es clara: **compara harnesses antes de aceptar el que viene por defecto**, o estarás pagando la harness tax sin darte cuenta.

Y para mí en particular, el estudio es una validación con datos de lo que ya intuía. Llevo meses usando [pi](https://pablocaro.es/tag/pi.html) como agente principal —[ya expliqué qué es y por qué me convenció](https://pablocaro.es/que-es-pi-coding-agent)— y [OpenCode](https://pablocaro.es/tag/opencode.html) como complemento. El estudio confirma exactamente por qué: un harness minimalista, con las herramientas justas y el contexto inicial al mínimo, da el mismo resultado que los todoterrenos pesados a una fracción del coste. La trilogía de pi en este blog envejece mejor de lo que esperaba.

*Fuente original*: [HarnessTax: How Much Does the Harness Matter for Coding Agents?](https://harnesstax.github.io/) (UC Berkeley / Arena, septiembre 2026). También hay una [versión extendida en el blog de Arena](https://arena.ai/blog/coding-agents-harness-tax).
