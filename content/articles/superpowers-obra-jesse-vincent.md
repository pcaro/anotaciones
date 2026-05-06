---
title: Superpowers — Jesse Vincent impone metodología a los agentes de codificación
slug: superpowers-obra-jesse-vincent
lang: es
date: 2026-05-06
category: ia
tags: agentes, ia, superpowers, jesse-vincent, claude-code, prime-radiant
series: Ingeniería de Programación con Agentes
series_index: 4
featured_image: /images/superpowers-obra-cover.png
---

Cuarta entrega de la serie sobre ingeniería de programación con agentes. Hoy toca un proyecto que ha cambiado las reglas del juego: **Superpowers**, de Jesse Vincent.

Con 180.000 estrellas en GitHub y 16.000 forks, Superpowers es el marco de habilidades para agentes más popular del momento. Pero lo que lo hace especial no es el número de estrellas, sino su obsesión: imponer una metodología de ingeniería completa a los agentes de código, desde el primer prompt hasta el último commit.

![Superpowers — Jesse Vincent](/images/superpowers-obra-cover.png)

## Quién es Jesse Vincent

Jesse Vincent es una figura conocida en el mundo del software de código abierto. Es el creador de **Perl 6** (hoy Raku), cofundó **Best Practical** y construyó **RT** (Request Tracker), el sistema de ticketing usado por organizaciones como la Free Software Foundation y el kernel de Linux. Hoy está en **Prime Radiant**, una empresa que construye herramientas para ingeniería con agentes.

Su blog es un referente en la comunidad de coding agents desde octubre de 2025, cuando publicó el primer artículo sobre Superpowers. Desde entonces, cada release ha sido un evento.

## La idea central

Superpowers no es un plugin más. Es una **metodología de desarrollo completa** para agentes de codificación, construida sobre habilidades composables que se activan automáticamente según el contexto.

El flujo básico es:

1. **Brainstorming** — El agente NO empieza a programar. Pregunta, explora alternativas y refina la idea antes de tocar una línea.
2. **Using-git-worktrees** — Crea un workspace aislado en una rama nueva.
3. **Writing-plans** — Descompone el trabajo en tareas de 2-5 minutos, cada una con paths exactos, código completo y pasos de verificación.
4. **Subagent-driven-development o executing-plans** — Despacha agentes para implementar o ejecuta en lotes con checkpoints humanos.
5. **Test-driven-development** — RED-GREEN-REFACTOR obligatorio. Tests primero, siempre.
6. **Requesting-code-review** — Review contra el plan, con severidades Critical/Nit/Optional.
7. **Finishing-a-development-branch** — Tests, merge o PR, cleanup.

El mantra que resume todo: **si el agente empieza a codificar sin hacer preguntas, Superpowers ha fallado**.

## Visual Brainstorming

La novedad más llamativa de la versión 5 es el **Visual Brainstorming Companion**: un servidor web local que el agente levanta para mostrarte mockups, diagramas y comparaciones visuales en el navegador mientras conversáis.

El origen es curioso. Jesse se encontró pidiendo a Claude una y otra vez: _"Oye, ¿por qué no escribes eso como HTML para que pueda ver lo que quieres decir?"_ Hasta que recordó el mantra más importante de la programación con agentes: **"¿Por qué lo estoy haciendo yo?"**

El agente ahora pregunta si quieres probar el compañero visual, y si aceptas, te abre un navegador con contenido interactivo. Detrás, un servidor WebSocket sirve chunks de HTML que el agente escribe a disco, con JavaScript para capturar clics y feedback.

Jesse lo probó para idear un logo para Prime Radiant con Claude. Dice que imaginar cómo habría sido en ASCII art da escalofríos.

## Spec Review: el bucle adversarial

Otro avance de la v5 es el **spec review loop**. Jesse detectó que los agentes dejaban secciones "TBD" o "Fill this in later" en los documentos de planificación — y que eso acababa tan mal como cabría esperar.

La solución: después de planificar, Superpowers lanza un subagente que lee la documentación de diseño buscando lagunas y rarezas. No es un sustituto de leerla uno mismo, pero mejora drásticamente la calidad de los planes.

Es el mismo patrón que hemos visto en otras herramientas de la serie: **un loop adversarial de revisión**. El planificador produce, el revisor critica, el planificador corrige. Se repite hasta que no quedan objeciones.

## Subagent Driven Development

Hasta la v4, Superpowers ofrecía al usuario la opción entre subagentes o ejecución secuencial con checkpoints humanos. Esa ambigüedad venía de una época en que los subagentes eran nuevos y Jesse no se fiaba de ellos.

A partir de la v5, si tu agente soporta subagentes, **Subagent Driven Development es obligatorio**. Si no los soporta, Superpowers te advierte que otro harness lo haría mejor, y luego hace lo que puede.

En harnesses como Claude Code que pueden elegir qué modelo usar para cada subagente, Superpowers instruye: modelo barato para tareas mecánicas, estándar para integración, capaz para arquitectura y revisión. Y los subagentes ahora tienen un protocolo de estado: DONE, DONE_WITH_CONCERNS, BLOCKED, NEEDS_CONTEXT.

## Ingeniería de software como principio

El valor de las interfaces comienza aquí:

- **Descomposición en unidades**: cada unidad debe tener un propósito claro, interfaces bien definidas y ser testeable de forma independiente.
- **"¿Puede alguien entender lo que hace una unidad sin leer su implementación? ¿Puedes cambiar la implementación sin romper a los consumidores?"**.
- **Archivos grandes como smell de diseño**: no es solo un problema de estilo, es una advertencia de que la descomposición falló.
- **File Structure como paso obligatorio**: antes de descomponer en tareas, primero decides qué archivos existen y qué responsabilidad tiene cada uno.
  Esto es diseño guiado por interfaces llevado desde la especificación hasta la implementación y la revisión.

## Otras decisiones de diseño interesantes

**Las skills no son documentación.** Son **workflows**: secuencias de pasos que el agente sigue, con checkpoints que producen evidencia, terminando en un criterio de salida definido. Si metes un ensayo de 2000 palabras en el contexto, el agente lo lee y salta la ejecución real. Si metes un workflow, el agente tiene algo que hacer.

**Prioridad de instrucciones.** Superpowers establece una jerarquía explícita:

1. Tus instrucciones directas (CLAUDE.md, AGENTS.md) — prioridad máxima
2. Skills de Superpowers — overriding del comportamiento por defecto
3. System prompt por defecto — prioridad mínima

Si tu CLAUDE.md dice "no uses TDD" y un skill de Superpowers dice "usa TDD siempre", gana tu instrucción.

**Divulgación progresiva.** No se cargan las 20 skills en el contexto al inicio. Un meta-skill actúa como router que decide qué skills aplicar según la tarea. Cada skill describe cuándo debe activarse. El agente comprueba si aplica. Si no, sigue.

**Tablas anti-racionalización.** Cada skill incluye una tabla de excusas comunes que un agente podría usar para saltarse el workflow, emparejadas con una réplica. Esto es especialmente efectivo porque los LLMs son excelentes produciendo justificaciones plausibles para hacer lo que les apetece.

**El SUBAGENT-STOP gate.** Los subagentes despachados para tareas específicas se saltan el meta-skill y no activan flujos completos de skills. Esto evita que un subagente que solo debe implementar un cambio empiece a hacer brainstorming.

## En qué se diferencia de los otros

**Every** se centra en el bucle de aprendizaje: compound engineering acumula conocimiento en CLAUDE.md para que cada ciclo sea más eficiente.

**Addy Osmani** se centra en la disciplina: agent-skills fuerza al agente a pasar por las fases que un ingeniero senior nunca saltaría, con tablas anti-racionalización como arma principal.

**Superpowers** es más ambicioso: es un **sistema operativo completo** para agentes de código. No solo define workflows, sino que gestiona worktrees de git, decide qué modelo usar para cada subagente, revisa especificaciones con loops adversariales, y tiene un protocolo de comunicación entre subagentes.

Si Every es compound engineering y Addy es harness engineering, Superpowers es **methodology engineering**: construir el sistema que obliga al agente a seguir una metodología completa de desarrollo de software.

Addy pone el foco en la disciplina del ingeniero senior. Superpowers pone el foco en la **disciplina del proceso**: el workflow es el que manda, no el agente. La diferencia es sutil pero importante.

## Lo que más me ha gustado

**El mantra "¿Por qué lo estoy haciendo yo?"** aplicado al Visual Brainstorming. Es la pregunta que todo el que programa con agentes debería hacerse constantemente. Si el agente puede hacerlo, que lo haga.

**El spec review loop.** El patrón adversarial para mejorar la calidad de los planes es simple, efectivo, y aplicable a cualquier flujo de trabajo con agentes.

**La prioridad de instrucciones.** Poner CLAUDE.md por encima de las skills de Superpowers es el gesto de diseño más honesto del proyecto. Le dice al usuario: "esto es para ayudarte, no para decirte lo que tienes que hacer".

**La tasa de rechazo del 94% como señal de calidad.** Que el creador sea tan agresivo contra el slop de agentes es una declaración de intenciones. Superpowers no quiere más contribuciones, quiere contribuciones excelentes.

## Mi lectura

Superpowers es el proyecto más completo de los que hemos visto en esta serie. Jesse Vincent lleva desde octubre de 2025 iterando sobre la misma idea: cómo hacer que un agente de código se comporte como un ingeniero con experiencia, no como un junior que escribe la primera solución que se le ocurre.

La diferencia con otras aproximaciones es que Superpowers no confía en el agente. No confía en que "sabrá lo que tiene que hacer". Le da un workflow, le obliga a seguirlo, revisa que lo ha seguido, y si se desvía, le redirige.

Eso suena restrictivo, y lo es. Pero la experiencia de cientos de miles de usuarios sugiere que es exactamente lo que los agentes necesitan: estructura, no libertad.

Para mí, lo más valioso de Superpowers no son las skills, sino la **filosofía**: si quieres que un agente produzca trabajo de calidad, no puedes delegar la metodología al agente. Tienes que codificarla en skills que se activen automáticamente, con checkpoints que produzcan evidencia, y con loops adversariales que verifiquen que no se han saltado nada.

Este framework es el que más he usado de los tres que he revisado en la serie. Desde sus primeras versiones con Claude Code se mostró muy sólido, y cada release ha sido un salto adelante.

El próximo artículo de la serie explorará otro enfoque. Pero creo que Superpowers marca un antes y un después en cómo pensamos sobre la ingeniería con agentes.

## Recursos

- [Superpowers en GitHub](https://github.com/obra/superpowers) — El repositorio (180K+ estrellas)
- [Superpowers 5 — el anuncio](https://blog.fsck.com/2026/03/09/superpowers-5/) — El artículo de Jesse Vincent
- [Superpowers: How I'm using coding agents in October 2025](https://blog.fsck.com/2025/10/09/superpowers/) — El artículo original de lanzamiento
- [Prime Radiant](https://primeradiant.com) — La empresa de Jesse Vincent
- [Compound Engineering — Every](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents) — Artículo anterior de la serie
- [Agent Skills de Addy Osmani](https://addyosmani.com/blog/agent-skills/) — Artículo anterior de la serie
