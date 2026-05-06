---
title: Agent Skills de Addy Osmani — Imponiendo disciplina de ingeniería senior a los agentes
slug: agent-skills-addy-osmani
lang: es
date: 2026-05-06
category: ia
tags: agentes, ia, agent-skills, addy-osmani, google, claude-code
series: Ingeniería de Programación con Agentes
series_index: 3
featured_image: /images/agent-skills-addy-cover.png
---

En las dos partes anteriores de esta serie hemos visto una visión general de la ingeniería con agentes y luego la metodología de compound engineering de Every. Ahora toca otra aproximación similar: **Agent Skills**, el proyecto de Addy Osmani en Google que lleva casi 30.000 estrellas en GitHub y que aborda el problema desde un ángulo completamente diferente.

![Agent Skills de Addy Osmani](/images/agent-skills-addy-cover.png)

## El problema que nadie quiere ver

Addy plantea algo incómodo: el comportamiento por defecto de cualquier agente de código es tomar el camino más corto hacia "hecho". Le pides una feature y te escribe la feature. No pregunta si tienes una especificación. No escribe un test antes de la implementación. No considera si el cambio cruza un límite de confianza. No verifica cómo se verá el PR para un revisor. Produce código, declara victoria y sigue adelante.

Esto es exactamente el mismo fallo que todo ingeniero senior ha pasado su carrera aprendiendo a evitar. El trabajo senior no es el que aparece en el diff: es sacar a la luz suposiciones, escribir la especificación, fragmentar el trabajo en chunks revisables, elegir el diseño aburrido, dejar evidencia de que el resultado es correcto, dimensionar el cambio para que un humano pueda revisarlo.

Los agentes saltan esos pasos por la misma razón que cualquier junior lo haría: son invisibles. La señal de recompensa apunta a "tarea completada", no a "tarea completada y el documento de diseño existe". Así que hay que atornillar el andamiaje de ingeniero senior de nuevo.

## Qué es una skill

Addy define una skill con precisión: es un archivo markdown con frontmatter que se inyecta en el contexto del agente cuando la situación lo requiere. Algo entre un fragmento de system prompt y un runbook.

Una skill **no es** documentación de referencia. No es "todo lo que deberías saber sobre testing". Es un **workflow**: una secuencia de pasos que el agente sigue, con checkpoints que producen evidencia, terminando en un criterio de salida definido.

Esa distinción lo cambia todo. Si metes un ensayo de 2000 palabras sobre mejores prácticas de testing en el contexto del agente, el agente lo lee, genera texto plausible, y salta el testing de verdad. Si metes un **workflow** (escribe el test que falla primero, ejecútalo, míralo fallar, escribe el mínimo código para pasar, míralo pasar, refactoriza), el agente tiene algo que hacer, y tú tienes algo que verificar.

> Proceso descrito con claridad. Workflows sobre referencia. Pasos con criterios de salida sobre ensayos sin ellos.

## Las 20 skills y los 7 comandos

El repositorio organiza 20 skills alrededor de 6 fases del ciclo de vida del software, con 7 comandos slash encima:

| Fase   | Comando   | Qué hace                           |
| ------ | --------- | ---------------------------------- |
| Define | `/spec`   | Decide qué estás construyendo      |
| Plan   | `/plan`   | Fragmenta el trabajo               |
| Build  | `/build`  | Implementa en slices verticales    |
| Verify | `/test`   | Demuestra que funciona             |
| Review | `/review` | Atrapa lo que se escapó            |
| Ship   | `/ship`   | Lleva a producción de forma segura |

También hay `/code-simplify` que atraviesa todo el ciclo.

Una feature compleja podría activar 11 skills en secuencia. Un bug pequeño podría usar 3. Un meta-skill (`using-agent-skills`) actúa como router que decide cuáles aplican. El workflow escala al scope real, no al scope asumido.

## Cinco principios que sostienen todo

### 1. Proceso simple y directo

Workflows son accionables para agentes; ensayos no. Lo mismo ocurre en equipos humanos. Si tu manual del equipo tiene 200 páginas, nadie lo lee bajo presión. Si es un conjunto pequeño de workflows con checkpoints, la gente realmente los ejecuta.

### 2. Tablas anti-racionalización

Esta es la decisión de diseño más distintiva del proyecto. Cada skill incluye una tabla de excusas comunes que un agente (o un ingeniero cansado) podría usar para saltarse el workflow, emparejadas con una réplica.

- _"Esta tarea es demasiado simple para necesitar una especificación."_ → Los criterios de aceptación siguen aplicando. Cinco líneas están bien. Cero líneas no.
- _"Escribiré los tests después."_ → "Después" es la palabra que sostiene todo. No hay después. Escribe el test que falla primero.
- _"Los tests pasan, mándalo."_ → Tests que pasan son evidencia, no prueba. ¿Comprobaste el runtime? ¿Verificaste el comportamiento visible al usuario? ¿Un humano leyó el diff?

La razón por la que esto funciona es que los LLMs son excelentes en la racionalización. Producirán un párrafo plausible explicando por qué _esta tarea en particular_ no necesita una spec, o por qué _este cambio en particular_ está bien para mergear sin revisión. **Las tablas anti-racionalización son réplicas pre-escritas a mentiras que el agente aún no ha contado.**

El patrón es igual de bueno para equipos humanos. La mayoría de la decadencia en ingeniería no es que alguien elija hacer mal trabajo. Es que la gente acepta justificaciones plausibles para saltarse las partes que no le apetecen hacer.

### 3. La verificación NO es negociable

Cada skill termina en evidencia concreta. Tests pasan. La salida del build está limpia. El trace del runtime muestra el comportamiento esperado. Un revisor da el visto bueno. "Parece correcto" nunca es suficiente.

El agente es un generador. Necesitas una señal separada de que el trabajo está hecho. Las skills hornean esa señal en cada workflow.

### 4. Divulgación progresiva

No cargues las 20 skills en el contexto al inicio de la sesión. Actívalas según la fase.

Cada token cargado en el contexto degrada el rendimiento en algún lugar, así que cargas lo relevante y dejas el resto en disco. La divulgación progresiva es cómo metes una librería de 20 skills en un slot de 5K tokens sin envenenar el pozo.

### 5. Disciplina de scope

El meta-skill codifica algo que graparía a cada agente si pudiera: _"toca solo lo que te piden tocar"_. No refactorices sistemas adyacentes. No elimines código que no entiendes completamente. No topes con un TODO y decidas reescribir el archivo.

Esto suena obvio hasta que ves a un agente decidir que arreglar un bug requiere modernizar tres archivos no relacionados. La disciplina de scope es el determinante más importante de si el PR de un agente es mergeable o hay que deshacerlo.

## El ADN de Google

Addy trabaja en Google, y las skills están saturadas de prácticas de _Software Engineering at Google_ y la cultura de ingeniería pública de Google. Esto es intencional. La mayoría de lo que hace que el software a escala de Google funcione está documentado y es público, y es _exactamente_ la parte que los agentes son más propensos a saltar.

- **Ley de Hyrum** en `api-and-interface-design`. Cualquier comportamiento observable de tu API eventualmente será dependido por alguien.
- **La pirámide de tests (~80/15/5) y la Regla de Beyoncé** en `test-driven-development`. _"Si te gustó, deberías haberle puesto un test"._
- **DAMP sobre DRY en tests.** La filosofía de testing de Google es explícita: el código de test debe leerse como una especificación, incluso a costa de algo de duplicación.
- **PRs de ~100 líneas, con etiquetas de severidad Critical / Nit / Optional / FYI** en `code-review-and-quality`. Directamente de las normas de code review de Google. PRs grandes no se revisan; se sellan sin mirar.
- **La Valla de Chesterton** en `code-simplification`. No elimines algo hasta que entiendas por qué fue puesto ahí.
- **Desarrollo basado en trunk y commits atómicos** en `git-workflow-and-versioning`.
- **Shift Left y feature flags** en `ci-cd-and-automation`. Atrapa problemas lo antes posible, desacopla deploy de release.
- **Código como pasivo** en `deprecation-and-migration`. Cada línea que mantienes es una que tienes que mantener para siempre.

Ninguna de estas ideas es nueva. **El punto es que ninguna de ellas está en el agente por defecto.** Un modelo frontier ha leído la frase "Ley de Hyrum" en su training data, pero no aplica la Ley de Hyrum cuando diseña tu API a las 3 de la mañana mientras duermes. Las skills son cómo te aseguras de que sí lo hace.

## Qué puedes usar aunque decidas no seguir la estrategia completa

**Anti-racionalización como práctica de equipo.** Escribe las mentiras que tu equipo se cuenta a sí mismo. _"Arreglaremos los tests después del lanzamiento."_ _"Este cambio es demasiado pequeño para un doc de diseño."_ _"Está bien, tenemos monitorización."_ Empareja cada una con la réplica. Ponlo en tu AGENTS.md o en tu wiki de ingeniería. Te ahorrará argumentos y atrapará el próximo atajo del viernes por la tarde.

**Proceso claro y sobre papel para cualquier cosa que escribas internamente.** Si te encuentras escribiendo un documento de 2000 palabras titulado "cómo abordamos X", has escrito material de referencia. Conviértelo a un workflow con checkpoints. El documento se reduce a 400 palabras y la gente realmente lo ejecuta.

**Verificación como criterio de salida duro.** Haz que "producir evidencia" sea el paso de salida de cada tarea. Para agentes, para ingenieros, para ti mismo. La evidencia es lo que demuestra que el trabajo está hecho: una ejecución de tests en verde, una captura de pantalla, un log, una aprobación de review. Sin ella, la tarea no está hecha. "Parece correcto" nunca cierra el bucle.

**Divulgación progresiva para cualquier manual.** No escribas un manual de 50 páginas. Escribe un router pequeño que apunte al capítulo pequeño correcto para la situación. Esto es cierto para AGENTS.md, para runbooks, para playbooks de incidentes, para cualquier cosa que alguien lea bajo presión de tiempo.

**Cinco no negociables, extraídos del meta-skill, que pondría en cualquier AGENTS.md mañana:**

1. Saca a la luz las suposiciones antes de construir. Suposiciones equivocadas mantenidas en silencio son el modo de fallo más común.
2. Para y pregunta cuando los requisitos entren en conflicto. No adivines.
3. Empuja hacia atrás cuando sea warranted. El agente (o ingeniero) no es una máquina de decir sí.
4. Prefiere la solución aburrida y obvia. La astucia es cara.
5. Toca solo lo que te piden tocar.

Esa es una cultura de ingeniería válida en cinco líneas, y no necesitas instalar nada para adoptarla.

## Mi lectura

Lo que propone Addy es distinto a lo de Every, pero complementario. Every se centra en el bucle de aprendizaje: cada iteración hace que el siguiente ciclo sea más fácil. Addy se centra en la disciplina: cada tarea debe pasar por las fases que un ingeniero senior nunca saltaría.

Every es compound engineering. Addy es **harness engineering** — construir el arnés que fuerza al agente a comportarse como un senior. El repositorio de Addy no es un framework, es una biblioteca de workflows portables. El mismo archivo SKILL.md funciona en Claude Code, Cursor, Gemini CLI, Codex, y cualquier otro entorno que acepte contenido de system prompt.

La implicación es clara: no basta con tener un agente potente. Necesitas un sistema que le impida tomar atajos. Las tablas anti-racionalización son la idea más brillante del proyecto porque atacan directamente la debilidad más peligrosa de los LLMs: su capacidad para producir justificaciones plausibles para hacer mal trabajo.

En mi propio flujo, voy a adoptar dos cosas inmediatamente: las tablas anti-racionalización para las tareas donde más fallo (saltarme tests en cambios "pequeños", asumir que "ya lo revisaré después"), y la regla de los cinco no negociables como checklist mental antes de cualquier sesión con un agente.

## Recursos

- [Agent Skills en GitHub](https://github.com/addyosmani/agent-skills) — El repositorio con las 20 skills (29K+ estrellas)
- [Agent Skills — el artículo](https://addyosmani.com/blog/agent-skills/) — El post de Addy explicando el diseño
- [Agent Harness Engineering](https://addyosmani.com/blog/agent-harness-engineering/) — El artículo sobre el arnés de agentes en general
- [Long-running Agents](https://addyosmani.com/blog/long-running-agents/) — Por qué los skills importan más en sesiones largas
