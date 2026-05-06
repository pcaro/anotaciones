---
title: Compound Engineering — La visión de Every sobre ingeniería con agentes
slug: compound-engineering-every
lang: es
date: 2026-05-06
category: ia
tags: agentes, ia, compound-engineering, every, claude-code
series: Ingeniería de Programación con Agentes
series_index: 2
featured_image: /images/compound-engineering-every-cover.png
---

En la primera parte de esta serie hablé de cómo los agentes de IA han cambiado mi forma de construir software. Pero eso era solo el calentamiento. Lo que viene ahora es la visión de una empresa que ha llevado esta idea al extremo: **Every**, la startup de Dan Shipper y Kieran Klaassen, que ha construido no solo productos con agentes, sino una **metodología completa** para hacerlo.

La llaman **compound engineering**.

![Compound Engineering — How Every Codes With Agents](/images/compound-engineering-every-cover.png)

## El problema con la ingeniería tradicional

En la ingeniería de software clásica, cada nueva feature complica la siguiente. Más código significa más casos límite, más interdependencias, más sorpresas que nadie anticipó. Es una curva de complejidad que solo sube.

Every se dio cuenta de que con agentes escribiendo el código, esa premisa ya no tenía sento. Si un agente puede generar código en segundos, el cuello de botella deja de ser "escribir código" y pasa a ser "saber qué código escribir". Y si el agente puede aprender de cada iteración, la complejidad deja de ser un peso muerto y se convierte en combustible.

> En compound engineering, cada feature hace más fácil la siguiente. No porque el código desaparezca, sino porque el sistema aprende de él.

## El bucle de compound engineering

Every define cuatro pasos que se repiten en ciclo. El truco está en que el output de cada ciclo alimenta el siguiente:

### 1. Plan

Aquí es donde pasa el 40% del tiempo de un compound engineer. No escribir código, no revisar PRs. **Planificar**.

El agente investiga el codebase actual, lee la historia de commits, busca mejores prácticas en internet, y sintetiza todo en un plan de implementación detallado. Cuando empieza a escribir, ya está calentado. Ya conoce las convenciones del proyecto, los patrones que funcionaron antes, y los que fracasaron.

Este paso es crítico porque un agente sin contexto genera código genérico. Un agente con contexto genera código que encaja en tu arquitectura como si lo hubiera escrito un miembro del equipo.

### 2. Work

El agente escribe código y tests según el plan. Esto es lo que la mayoría de la gente imagina cuando piensa en "programar con IA": el agente genera funciones, clases, tests. Pero en compound engineering, este paso representa apenas el 10% del esfuerzo humano. El código se escribe solo. El valor está en todo lo que rodea a ese código.

### 3. Review

El ingeniero revisa el output. No solo busca bugs, sino que extrae **lecciones**. ¿Por qué el agente eligió esta abstracción? ¿Hubo un patrón que no reconoció? ¿Un edge case que olvidó?

En Every usan múltiples agentes revisoras especializadas: una para seguridad, otra para rendimiento, otra para simplicidad, otra para mantenibilidad. Cada una mira el código desde un ángulo diferente. El ingeniero humano orquesta estas revisiones y decide qué feedback incorporar.

### 4. Compound

Este es el paso que cambia todo. Las lecciones extraídas en la review no se quedan en la cabeza del ingeniero. Se documentan. Se codifican. Se convierten en parte del sistema.

Every usa archivos como `CLAUDE.md` y `AGENTS.md` donde se registra todo: patrones de código aprobados, decisiones arquitectónicas, bugs recurrentes y sus soluciones, estilos de nomenclatura, preferencias de diseño. La próxima vez que un agente trabaje en el proyecto, lee estos archivos antes de empezar. Cada ciclo hace que el agente sea más listo.

## Un ejemplo real: el detector de frustración

Kieran Klaassen describe en Every cómo construyeron un "detector de frustración" para su producto Cora, un asistente de email con IA. El objetivo: detectar cuando un usuario se está frustrando con la app y generar automáticamente un reporte de mejora.

El flujo fue así:

1. **Crearon una conversación de ejemplo** donde un usuario expresa frustración (preguntas repetidas, lenguaje cada vez más conciso).
2. **Le pidieron a Claude que escribiera un test** que verifique si el sistema detecta esa frustración.
3. **El test falló** — como debe ser en TDD.
4. **Le pidieron a Claude que escribiera la lógica de detección**.
5. **Funcionó parcialmente**. Entonces le pidieron que **iterara el prompt** hasta que el test pasara.
6. **Para evitar la no-determinación de la IA**, hicieron que Claude ejecutara el test 10 veces.
7. **Analizó los 6 fallos**, leyó el chain-of-thought de cada uno, y descubrió un patrón: el sistema no detectaba lenguaje atenuado como "Hmm, not quite", que en contexto de repetición sí señala frustración.
8. **Actualizó el prompt** para buscar específicamente ese lenguaje. En la siguiente iteración, identificaba frustración 9 de 10 veces.
9. **Codificaron todo el flujo** en `CLAUDE.md`. La próxima vez que necesiten detectar una emoción o comportamiento de usuario, no empiezan de cero. Dicen: "usa el workflow del detector de frustración".

Ese es compound engineering en acción. No es solo resolver el problema de hoy. Es enseñar al sistema a resolver toda una categoría de problemas.

## El plugin de compound engineering

Every ha open-sourcéado su sistema como un plugin que funciona con Claude Code, Codex CLI, Cursor y otros. Tiene más de 50 agentes especializados y 38 skills accesibles como slash commands.

Algunos de los skills más interesantes:

- `/ce-strategy` — Crea o mantiene el `STRATEGY.md` del producto: problema, approach, persona, métricas clave.
- `/ce-plan` — Genera planes estructurados para cualquier tarea multi-paso, con verificación de confianza automática.
- `/ce-brainstorm` — Q&A interactivo para pensar un feature antes de planificarlo.
- `/ce-work` — Ejecuta items de trabajo de forma sistemática.
- `/ce-debug` — Encuentra root causes y fixea bugs con hipótesis testeables.
- `/ce-code-review` — Review estructurada con múltiples agentes revisores en paralelo.
- `/ce-compound` — Documenta problemas resueltos para que el equipo (y los agentes) aprendan.
- `/ce-compound-refresh` — Revisa learnings obsoletos y decide si actualizar, reemplazar o archivar.
- `/ce-product-pulse` — Genera reportes de uso, performance, errores y followups.
- `/ce-sessions` — Busca en el historial de sesiones de Claude Code, Codex y Cursor.

Y las agentes revisoras son especialistas: hay una para contratos de API, otra para migraciones de datos, otra para carreras en frontend, otra para seguridad, otra para rendimiento. Cada una aplica su lente específico.

## Por qué esto importa

Every corre cinco productos software, cada uno construido y mantenido principalmente por una sola persona. Productos que usan miles de personas todos los días. No son demos. Son negocios reales.

Su métrica: un solo desarrollador con compound engineering hace el trabajo de cinco desarrolladores tradicionales. No porque escriba más código, sino porque cada línea que escribe construye sobre todo lo aprendido antes.

La implicación es profunda. Si la ingeniería tradicional asume que escribir código es difícil y los ingenieros son escasos, compound engineering asume que el código es barato y el conocimiento es el activo valioso. La pregunta ya no es "¿cómo escribo esto?", sino "¿cómo enseño al sistema a escribir esto, y todo lo que se le parezca, para siempre?".

## Mi lectura

Lo que propone Every no es una herramienta, es un cambio de paradigma. La ingeniería de software siempre ha tenido un componente de acumulación: bibliotecas, frameworks, patrones. Pero eso era acumulación de código. Compound engineering es acumulación de **conocimiento sobre cómo construir**.

El `CLAUDE.md` no es documentación para humanos. Es memoria para agentes. Y eso cambia la naturaleza del trabajo del ingeniero: deja de ser quien escribe código para ser quien diseña sistemas que escriben código, y que además aprenden de cada línea que generan.

No es futurismo. Every ya lo está haciendo. El plugin está en GitHub, con 16k+ estrellas. La pregunta no es si esto va a llegar a tu equipo, sino cuándo.

## Recursos

- [Compound Engineering Plugin](https://github.com/EveryInc/compound-engineering-plugin) — El plugin open source de Every
- [Compound Engineering: How Every Codes With Agents](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents) — El artículo original de Dan Shipper y Kieran Klaassen
- [My AI Had Already Fixed the Code Before I Saw It](https://every.to/source-code/my-ai-had-already-fixed-the-code-before-i-saw-it) — Kieran describe el sistema de compounding en acción
