---
title: Spec Kit de GitHub — Especificaciones como fuente de verdad
slug: spec-kit-github
lang: es
date: 2026-05-10
category: ia
tags: agentes, ia, spec-kit, github, spec-driven-development
series: Ingeniería de Programación con Agentes
series_index: 6
featured_image: /images/spec-kit-github-cover.png
---

Sexta entrega de la serie sobre ingeniería de programación con agentes. Hoy toca el proyecto que GitHub ha convertido en el estándar de facto del desarrollo guiado por especificaciones: **Spec Kit**.

Hasta ahora hemos visto metodologías para dirigir agentes: compound engineering (Every), skills de disciplina (Addy Osmani), un sistema operativo completo para agentes (Superpowers de Jesse Vincent), y skills mínimas y pragmáticas (Matt Pocock). Todas comparten una premisa: defines cómo quieres que el agente trabaje y él ejecuta.

Spec Kit da la vuelta a esa premisa. No le dice al agente **cómo** trabajar. Le dice **qué** construir, y deja que el agente descubra cómo. La diferencia es sutil pero lo cambia todo.

![Spec Kit de GitHub — Especificaciones como fuente de verdad](/images/spec-kit-github-cover.png)

## El problema que resuelve

Todos los frameworks que hemos visto en la serie asumen que sabes lo que quieres construir y que el problema es que el agente no lo construye bien. Tiene razón: sin disciplina, los agentes toman atajos, generan código genérico y producen resultados inconsistentes.

Pero hay otro problema, más profundo: **¿y si no sabes exactamente lo que quieres?** ¿Y si tus requisitos son vagos, contradictorios o incompletos?

Si veinte desarrolladores le piden a un agente "haz un CRUD de usuarios", obtendrán veinte resultados diferentes, y probablemente ninguno sea lo que realmente necesitaban. Porque "CRUD de usuarios" no es una especificación. Es una idea. Y las ideas no se implementan: se refinan.

Spec Kit aborda este problema desde la raíz. No es un framework para programar con agentes. Es un **framework para especificar con agentes**. El código sale solo.

## La inversión de poder

Spec Kit llama a su idea central **The Power Inversion** (la inversión de poder). La idea no es nueva: es ingeniería del software de toda la vida. Cuando yo estudiaba ingeniería informática, esto se llamaba DDR (Documento de Definición de Requisitos). Tenías requisitos de usuario ("Como usuario quiero..."), requisitos funcionales y requisitos de sistema. De ahí derivabas una especificación técnica, y luego el código. En Carto era nuestra filosofía principal: PRD, documento de especificación técnica, código.

Lo que cambia con Spec Kit es que la especificación ya no es un documento que guía la implementación para que un humano la ejecute. Es un documento **ejecutable** por un agente de IA. El PRD no es contexto para que un desarrollador escriba código. Es la entrada que genera directamente la implementación.

La diferencia es que los agentes son muy buenos ayudándote a especificar. Pueden hacer preguntas, identificar ambigüedades, explorar el código existente en busca de contexto, y refinar los requisitos contigo antes de escribir una línea. Esa capacidad de iterar sobre la especificación en segundos en lugar de días es lo que hace que el flujo sea práctico.

Los números lo avalan: 95.000 estrellas en GitHub, 8.200 forks, 30+ agentes de IA soportados, y un ecosistema de extensiones comunitarias que ha crecido de 26 a 83 en solo un mes.

## El flujo de trabajo

Spec Kit define seis comandos principales que cubren todo el ciclo de vida de una feature:

| Comando                 | Qué hace                                              |
| ----------------------- | ----------------------------------------------------- |
| `/speckit.constitution` | Define los principios rectores del proyecto           |
| `/speckit.specify`      | Describe **qué** construir (requisitos, user stories) |
| `/speckit.clarify`      | Preguntas estructuradas para resolver ambigüedades    |
| `/speckit.plan`         | Traduce la especificación a un plan técnico           |
| `/speckit.tasks`        | Descompone el plan en tareas accionables              |
| `/speckit.implement`    | Ejecuta las tareas y genera el código                 |

Además hay comandos opcionales: `/speckit.analyze` para validación cruzada entre artefactos, y `/speckit.checklist` para generar checklists de calidad personalizados.

### 1. Constitución

Antes de escribir una sola línea de especificación, defines los principios del proyecto. No es un documento de equipo. Es un contrato que el agente debe respetar en cada decisión.

Spec Kit incluye una constitución de ejemplo con nueve artículos que cubren desde "library-first" (toda feature empieza como librería independiente) hasta "test-first imperative" (no hay código sin tests que fallen primero).

La constitución no es opcional. Es el sistema inmunológico del proyecto. Sin ella, el agente toma decisiones coherentes pero no necesariamente consistentes. Con ella, cada decisión refuerza la arquitectura.

### 2. Especificación

Aquí está la clave de todo: en `/speckit.specify` solo hablas del **qué** y el **por qué**. Nada de stack tecnológico. Nada de APIs. Nada de cómo.

El template de especificación fuerza esta separación explícitamente:

```text
- ✅ Focus on WHAT users need and WHY
- ❌ Avoid HOW to implement (no tech stack, APIs, code structure)
```

Esto es más difícil de lo que parece. Como ingenieros, nuestro instinto es saltar al "cómo" en cuanto entendemos el problema. Spec Kit te obliga a mantenerte en el "qué" el tiempo suficiente para que la especificación sea completa.

Además, el template incluye marcadores `[NEEDS CLARIFICATION]` que el agente debe usar cuando algo no está claro. Esto evita el problema más común con los LLMs: que adivinen en lugar de preguntar.

### 3. Clarificación

Este paso es el que más valoro personalmente. Antes de pasar al plan técnico, `/speckit.clarify` inicia un diálogo estructurado donde el agente identifica ambigüedades y te pregunta una por una.

No es un cuestionario genérico. El agente ha leído la especificación y sabe exactamente qué no entiende. Te pregunta hasta que no quedan ramas del árbol de decisión sin explorar.

Es el mismo patrón que el `/grill-me` de Matt Pocock, pero incrustado en un flujo más amplio y con un formato estructurado que queda registrado en la propia especificación.

### 4. Plan

Ahora sí, llegó el momento del "cómo". Le dices al agente tu stack tecnológico y tus decisiones arquitectónicas. El agente genera un plan de implementación detallado que incluye:

- **Modelo de datos**: esquemas, relaciones, restricciones
- **Contratos de API**: endpoints, eventos, formatos
- **Investigación**: comparativa de librerías, benchmarks, decisiones técnicas con su rationale
- **Quickstart**: escenarios de validación clave

Cada elección técnica enlaza con requisitos concretos de la especificación. Nada queda sin trazar.

### 5. Tareas

El plan se descompone en tareas individuales, cada una con paths exactos, código completo y pasos de verificación. Las tareas independientes se marcan como paralelizables.

El sistema de tareas de Spec Kit es notable porque distingue entre tareas HITL (requieren decisión humana) y AFK (automatizables de principio a fin). Esto permite que el humano intervenga solo donde realmente aporta valor.

### 6. Implementación

El agente ejecuta las tareas en orden, respetando dependencias y siguiendo TDD. Cada tarea produce evidencia: tests que pasan, builds limpios, contratos validados.

Si algo falla, el agente no sigue adelante. Para, informa y espera instrucciones. Es la materialización del principio que recorre toda la serie: **la verificación no es negociable**.

## La fundación constitucional

Spec Kit impone un gran nivel de detalle en su constitución. No son principios vagos. Son nueve artículos con cláusulas concretas que el agente no puede ignorar.

**Artículo I — Library-First**: Toda feature empieza como librería independiente. Esto fuerza modularidad desde el primer commit. No vale "ya lo refactorizaremos".

**Artículo II — CLI Interface**: Toda librería debe exponer una interfaz de línea de comandos. Esto garantiza observabilidad: puedes invocar cualquier funcionalidad desde un script, sin tocar la interfaz gráfica.

**Artículo III — Test-First Imperative**: No negociable. Primero los tests. Tests que fallan. Luego la implementación mínima para que pasen.

**Artículos VII y VIII — Simplicidad y Anti-Abstracción**: Máximo 3 proyectos en la implementación inicial. Usa el framework directamente, no lo envuelvas. Nada de "por si acaso".

**Artículo IX — Integration-First Testing**: Tests en entornos reales. Bases de datos reales. Servicios reales. Nada de mocks si puedes evitarlos.

El detalle clave es cómo estos artículos se aplican a través de **gates** en el template del plan de implementación. Antes de que el agente escriba una línea, pasa por una fase de "gates pre-implementación" que verifican cada artículo. Si algo falla, el agente debe justificarlo por escrito en una sección de "Complejidad".

Esto convierte la constitución de un documento pasivo a un **sistema de enforcement activo**. No es que el agente "debería" seguir las reglas. Es que no puede saltárselas sin dejar evidencia.

## Comparación con el resto de la serie

Cada proyecto que hemos visto en la serie ocupa un nicho diferente:

| Proyecto        | Enfoque                 | Fortaleza                                               |
| --------------- | ----------------------- | ------------------------------------------------------- |
| **Every**       | Compound engineering    | Acumulación de conocimiento en CLAUDE.md                |
| **Addy Osmani** | Harness engineering     | Disciplina de ingeniero senior con anti-racionalización |
| **Superpowers** | Methodology engineering | Sistema operativo completo para agentes                 |
| **Matt Pocock** | Skills engineering      | Skills mínimas que cualquiera puede adoptar             |
| **Spec Kit**    | **Spec engineering**    | Las especificaciones son la fuente de verdad            |

Spec Kit es el único que no empieza por el agente. Empieza por la especificación. El agente es el último paso, no el primero.

## Mi lectura

Spec Kit es el proyecto que más se acerca a la ingeniería del software clásica de los que he cubierto en la serie. No por su complejidad técnica (que es poca: es básicamente un CLI de Python que genera archivos markdown), sino porque formaliza algo que siempre debimos hacer: especificar antes de construir.

Invertir la relación entre especificación y código es una idea que suena bien en abstracto pero que tiene implicaciones profundas. Si el código es un artefacto generado, ¿qué significa "mantener" el software? Mantener software significa evolucionar especificaciones. Debuggear significa corregir especificaciones que generan código incorrecto. Refactorizar significa reestructurar especificaciones para claridad.

El perfil del ingeniero de software siempre fue distinto al del programador. Nunca fue alguien que escribe código sin más. Es quien **escribe especificaciones que generan código**. Algo cercano a lo que ahora se denomina Product Owner en Scrum, pero con capacidad técnica para saber qué es implementable y qué no.

No sé si esta visión se cumplirá completamente. Pero Spec Kit tiene algo que ninguno de los otros proyectos tiene: el respaldo institucional de GitHub. Con 95.000 estrellas y creciendo, con una tasa de adopción que duplica a Superpowers en meses, Spec Kit no es un experimento. Es un movimiento.

Y lo más interesante es que GitHub no está construyendo Spec Kit para venderte nada. Es código abierto, es gratuito, y funciona con cualquier agente: Claude Code, Gemini CLI, Cursor, Codex, Copilot, el que uses. Es una apuesta por un estándar abierto de desarrollo con IA, y está funcionando.

La pregunta que debes hacerte no es "qué agente uso" o "qué methodology uso con mis agentes", sino "qué especificación escribo para que mis agentes construyan lo correcto". Spec Kit da una respuesta: escribe la especificación primero. El resto es implementación.

## Recursos

- [GitHub Spec Kit](https://github.com/github/spec-kit) — El repositorio oficial (95K+ estrellas)
- [Spec-Driven Development — la metodología](https://github.com/github/spec-kit/blob/main/spec-driven.md) — El documento que define SDD
- [Spec Kit Community Extensions](https://speckit-community.github.io/extensions/) — Catálogo de extensiones comunitarias
- [Matt Pocock — Skills que funcionan](https://pablocaro.es/matt-pocock-skills) — Artículo anterior de la serie
- [Superpowers — Jesse Vincent](https://pablocaro.es/superpowers-obra-jesse-vincent) — Artículo anterior de la serie
- [Agent Skills — Addy Osmani](https://pablocaro.es/agent-skills-addy-osmani) — Artículo anterior de la serie
- [Compound Engineering — Every](https://pablocaro.es/compound-engineering-every) — Artículo anterior de la serie
