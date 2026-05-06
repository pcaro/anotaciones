---
title: Matt Pocock — Skills sencillas que funcionan
slug: matt-pocock-skills
lang: es
date: 2026-05-06
category: ia
tags: agentes, ia, skills, matt-pocock, claude-code
series: Ingeniería de Programación con Agentes
series_index: 5
featured_image: /images/matt-pocock-skills-cover.png
---

Quinta entrega de la serie sobre ingeniería de programación con agentes. Hoy toca el proyecto que está arrasando estos días: las **skills de Matt Pocock**.

He cubierto Superpowers (Jesse Vincent), Agent Skills (Addy Osmani) y Compound Engineering (Every). Cada uno aporta una pieza importante del puzzle. Pero las skills de Matt Pocock han explotado en popularidad en cuestión de días, y creo que sé por qué: aplican una filosofía KISS llevada al extremo. Skills cortas, directas, sin pretensiones. Y una de ellas, `/grill-me`, se ha convertido en un fenómeno por sí sola.

![Matt Pocock Skills](/images/matt-pocock-skills-cover.png)

## La filosofía: skills que un ingeniero real usaría

Matt es conocido por Total TypeScript y su trabajo en TypeScript. Cuando empezó a publicar skills para Claude Code, no escribió un framework. Escribió archivos markdown de tres líneas que hacían una cosa y la hacían bien.

El lema del repositorio lo resume: _"Skills for Real Engineers"_ (skills para ingenieros de verdad). No hay capas de abstracción, ni plugins complejos, ni ciclos de vida sofisticados. Son ficheros markdown con frontmatter que se inyectan en el contexto del agente. Punto.

El repositorio se organiza en cubos: `engineering/` (skills del día a día), `productivity/` (herramientas generales), `misc/` (cosas que raramente usa), `personal/` (atadas a su setup) e `in-progress/`. De las ~20 skills totales, solo unas 6 son las que realmente recomienda para el día a día. Esa contención es la clave: no más de media docena de skills, y muy muy cortas.

El contraste con Superpowers (v5 con 20+ skills, loops adversariales, sistema de fases completo) no podría ser mayor. Matt demuestra que menos puede ser más si eliges bien qué automatizar.

## `/grill-me`: el skill que lo cambia todo

Tres frases. Eso es todo el skill:

> _"Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. Ask the questions one at a time. If a question can be answered by exploring the codebase, explore the codebase instead."_

Tres frases que han generado 62.000 estrellas en GitHub y se han compartido en todas partes. ¿Por qué?

Porque resuelven el problema número uno de trabajar con agentes: **la alineación**. El agente no sabe lo que quieres, y tú no sabes lo que el agente ha entendido. El `grill-me` fuerza una conversación estructurada donde el agente te pregunta hasta que no quedan ramas del árbol de decisión sin explorar.

Matt cuenta que en una sesión típica, Claude le hizo 16 preguntas para una feature relativamente simple. En features complejas, ha tenido sesiones de 30-40-50 preguntas que duran casi media hora. Pero al final de esa media hora, el diseño está completamente resuelto. No hay sorpresas cuando el agente empieza a escribir código.

El concepto de "árbol de decisión" viene de _The Design of Design_ de Frederick P. Brooks. La idea es que cuando diseñas algo, caminas por ramas: "¿búsqueda avanzada o búsqueda simple? Si avanzada, ¿qué filtros? ¿qué ordenación?" Hasta que has recorrido todas las ramas y el diseño está completamente especificado.

## El flujo completo: grill → PRD → issues → TDD

Matt encadena varias skills en un pipeline que cubre todo el ciclo de vida de una feature, desde la idea hasta el código pasando por tests:

1. **`/grill-me`**: el agente te entrevista hasta que el diseño está claro. Cada pregunta resuelve una decisión. Si puede responderla explorando el código, lo hace.

2. **`/to-prd`**: una vez alineados, convierte la conversación en un PRD (Product Requirements Document) con user stories, decisiones de implementación y criterios de aceptación. Se publica como issue en GitHub, Linear o el tracker que uses.

3. **`/to-issues`**: rompe el PRD en issues independientes usando _vertical slices_ (tracer bullets). Cada issue atraviesa todas las capas (schema, API, tests) y es demoable por sí mismo. Distingue entre HITL (human-in-the-loop, requiere decisión humana) y AFK (automatizable de principio a fin).

4. **`/tdd`**: Test-Driven Development con ciclo red-green-refactor. Una skill sustancial que incluye filosofía sobre mocking, módulos profundos y diseño de interfaces. Escribir un test que falla → implementación mínima → refactor. Una iteración a la vez, nunca todas las vistas horizontales juntas.

5. **`/improve-codebase-architecture`**: para cuando el código se ha convertido en una bola de barro. Explora el codebase buscando módulos poco profundos, acoplamientos ocultos y falta de testabilidad.

6. **`/grill-with-docs`**: variante de grill-me que además actualiza un `CONTEXT.md` con el lenguaje compartido del dominio y escribe ADRs para decisiones difíciles de revertir. Es la skill favorita de Matt — combinación de entrevista con domain-driven design.

---

Es notable cómo el flujo entero encaja con lo que hemos visto antes:

- **El scaffolding de Every** (CLAUDE.md que acumula conocimiento) aparece aquí como `CONTEXT.md` + ADRs.
- **La disciplina de Addy Osmani** (tablas anti-racionalización, workflows con checkpoints) aparece en el TDD skill con sus checklist por ciclo.
- **La metodología estructurada de Superpowers** (file structure primero, descomposición en unidades, loops adversariales) aparece aquí como vertical slices, tracer bullets y la separación HITL/AFK.

Pero Matt lo envuelve todo en skills tan cortas que caben en un tuit. No hay sobreingeniería. Hay pragmatismo.

## Mi lectura

Matt Pocock ha hecho algo que me parece más difícil que construir un framework: ha destilado su experiencia en piezas tan pequeñas que cualquiera puede adoptarlas sin cambiar su flujo de trabajo.

El `/grill-me` me resulta especialmente familiar porque mi flujo personal con agentes siempre ha incluido una fase de preguntas iterativas — casi una versión manual de lo que Matt ha codificado. Verlo convertido en skill pública, con 62.000 personas dándole estrellas, confirma que el instinto era correcto: la alineación temprana es el paso más infravalorado en el trabajo con agentes.

El resto de skills son igual de sólidas. El `to-prd` y `to-issues` formalizan algo que cualquier ingeniero senior hace instintivamente (pensar antes de escribir, dividir el trabajo en trozos revisables) pero que raramente se documenta. El TDD skill es el mejor que he visto para agentes: no solo dice "haz TDD", sino que explica _por qué_ las vistas horizontales producen tests malos y _cómo_ hacer ciclos verticales correctamente.

Lo que diferencia a Matt del resto es la **accesibilidad**. Superpowers requiere integrar un runtime. Agent Skills requiere instalar un plugin. Las skills de Matt son ficheros markdown que puedes copiar a tu `.claude/` en 30 segundos. Y si no quieres instalarlas, leerlas ya te da el framework mental.

No creo que las skills de Matt reemplacen a Superpowers o Agent Skills. Son herramientas para contextos diferentes. Superpowers es para cuando quieres una metodología completa que el agente no pueda saltarse. Matt es para cuando quieres piezas pequeñas, intercambiables, que entiendes y modificas.

Las dos tienen sentido. Pero Matt ha demostrado algo importante: a veces la mejor skill es la que cabe en tres líneas.

## Recursos

- [mattpocock/skills en GitHub](https://github.com/mattpocock/skills) — El repositorio (62K+ estrellas)
- [AI Hero — Skills](https://www.aihero.dev/skills) — La web oficial con guías de cada skill
- [5 Agent Skills I Use Every Day](https://www.aihero.dev/5-agent-skills-i-use-every-day) — El artículo de Matt presentando su kit
- [My Grill Me Skill Has Gone Viral](https://www.aihero.dev/my-grill-me-skill-has-gone-viral) — Sobre el fenómeno `/grill-me`
- [Superpowers — Jesse Vincent](https://pablocaro.es/superpowers-obra-jesse-vincent) — Artículo anterior de la serie
- [Agent Skills — Addy Osmani](https://pablocaro.es/agent-skills-addy-osmani) — Artículo anterior de la serie
- [Compound Engineering — Every](https://pablocaro.es/compound-engineering-every) — Artículo anterior de la serie
