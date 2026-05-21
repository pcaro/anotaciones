---
title: ¿Qué es pi? — El agente de código minimalista que se ha vuelto viral
slug: que-es-pi-coding-agent
lang: es
date: 2026-05-21
category: ia
tags: pi, coding-agent, agentes-ia, claude-code, codex, opencode, gemini-cli
series: Pi: el agente de código
series_index: 1
featured_image: /images/comparativa-agentes-pi.png
Summary: Pi es un agente de código minimalista para la terminal. En este artículo explico qué es, cómo se diferencia de Claude Code, Codex, OpenCode y Gemini CLI, y por qué se ha vuelto viral.
---

Llevo ya varios meses usando [pi](https://pi.dev/) como mi agente de código principal. Es una de esas herramientas que, una vez que la usas, no entiendes cómo funcionabas antes. En este artículo —primero de una serie de tres— voy a contar qué es pi, en qué se diferencia de otros coding agents y por qué creo que se ha vuelto extremadamente popular en GitHub. No os perdáis [pi.dev](https://pi.dev/), la web del proyecto — tiene unas animaciones muy didácticas que explican visualmente los conceptos.

![Comparativa de agentes de código](/images/comparativa-agentes-pi.png)

## La filosofía: menos es más

Pi se define como *"a minimal terminal coding harness"* — un arnés de codificación minimalista para la terminal. Y cuando dicen minimalista, lo dicen en serio.

El núcleo básico de pi tiene exactamente **cinco capacidades nativas**: leer archivos, ejecutar Bash, editar archivos, escribir archivos y gestionar sesiones. Eso es todo. No trae subagentes, ni modo de planificación, ni pop-ups de permisos, ni MCP incorporado, ni un editor de código.

Suena a poco, pero es la clave de todo. Vivimos en la era del *harness engineering* — la disciplina de construir entornos robustos alrededor de los agentes de IA — y pi es un punto de partida excelente para montar tu propio harness sin pagar el peaje de un ecosistema cerrado.

La filosofía de pi es que el usuario debe adaptar la herramienta a sus flujos de trabajo, y no al revés. En lugar de venir con 50 funciones que la mayoría no usa, pi te da las primitivas mínimas y un sistema de extensiones TypeScript para que construyas exactamente lo que necesites.

Si quieres subagentes, instalas una extensión. Si quieres MCP, te montas un adaptador. Si quieres un plan mode, te escribes un prompt template. Y si no quieres nada de eso, pues no lo tienes ocupando espacio ni ralentizando el arranque.

## Comparativa con otros coding agents

| Característica | **Pi** | **Claude Code** | **Codex** | **OpenCode** | **Gemini CLI** |
|---|---|---|---|---|---|
| **Filosofía** | Núcleo mínimo + extensiones | Todo incluido | Todo incluido | Núcleo mínimo | Todo incluido |
| **Modelos** | Cualquier proveedor (API key o suscripción) | Solo Claude | Solo OpenAI | Múltiples (OpenAI API) | Solo Gemini |
| **Subagentes** | Via extensiones | Nativos | Nativos | Nativos | Nativos |
| **MCP** | Via extensiones | Nativo | - | Nativo | Nativo |
| **Plan mode** | Via skills/templates | Nativo | Nativo | - | - |
| **Extensiones** | TypeScript SDK | Plugins JSON | - | - | - |
| **Precio** | Gratuito (tus claves) | Suscripción de pago | Suscripción de pago | Gratuito (tus claves) | Gratuito (cuota gratuita) |
| **Plataforma** | Terminal (cualquier emulador) | Terminal | Terminal | Terminal | Terminal |
| **Sesiones en árbol** | Nativo (JSONL tree) | Lineal | Lineal | Lineal | Lineal |
| **Skills** | Markdown + frontmatter | Markdown + frontmatter | - | - | - |

### Claude Code — El todoterreno de Anthropic

Claude Code es la apuesta oficial de Anthropic. Viene con todo: subagentes, memoria persistente, sistema de permisos, MCP nativo, y una experiencia muy pulida. Es el más maduro de los que no requieren IDE.

El problema es que solo funciona con Claude. Si quieres usar DeepSeek, Gemini u OpenAI, no puedes. Y el ecosistema de plugins es limitado comparado con lo que ofrece pi.

### Codex — La integración con ChatGPT

Codex es el agente de OpenAI. Se puede usar desde la terminal (`codex`) o integrado con ChatGPT. Viene con subagentes y una experiencia similar a Claude Code.

Pero al igual que Claude Code, estás atado a un solo proveedor. Y las extensiones son prácticamente inexistentes: lo que viene, es lo que tienes.

### Gemini CLI — El cli de la comunidad

Gemini CLI nace del desarrollo comunitario de google-gemini y se integra con su ecosistema (Gemini API, Google Cloud). Google ha ido dejando de lado el CLI en favor de Antigravity, su cliente privativo para empresas. Viene con skills y subagentes, pero la personalización es limitada y las extensiones de terceros son prácticamente inexistentes.

### OpenCode — El alma gemela

[OpenCode](https://github.com/opencode-go/opencode-go) es el que más uso después de pi, y en muchos sentidos es su complemento natural. Su filosofía es parecida: núcleo mínimo, terminal, multi-modelo. No tiene el ecosistema de extensiones de pi, pero trae subagentes y MCP nativos. Está escrito en Go, arranca igual de rápido, y su integración con el ecosistema OpenAI es excelente.

## ¿Qué hace único a pi?

Después de probarlos todos, lo que hace único a pi es una combinación de factores que ningún otro agente reúne:

**Extensibilidad**: Con el SDK de TypeScript puedes añadir herramientas, comandos, interceptar eventos, crear UI personalizada, y compartirlo todo como pi packages. Nadie más ofrece este nivel de personalización.

**Sesiones en árbol**: Las conversaciones se guardan como un árbol de decisión. Usas `/tree` para saltar a cualquier punto anterior y crear una rama alternativa sin perder el progreso previo. Esto solo lo tiene pi.

**Skills y prompt templates**: Pequeños archivos markdown que se inyectan en el contexto del agente. Son la forma más simple de enseñar a tu agente nuevas capacidades. [Ya hablé de cómo instalarlos](https://pablocaro.es/instalando-skills-de-github) y de las [skills de Matt Pocock](https://pablocaro.es/matt-pocock-skills) que se han vuelto virales.

**Ecosistema de paquetes**: En [pi.dev/packages](https://pi.dev/packages) hay extensiones para casi todo: adaptadores MCP, buscadores web, modos de optimización de contexto, temas, y mucho más. Y si no encuentras lo que buscas, te escribes una extensión en TypeScript en cinco minutos.

**No es un IDE**: Pi es un agente que vive en tu terminal, no un editor. Esto significa que funciona igual en tu máquina local, en un servidor por SSH, dentro de tmux, o en WSL. Usas tu editor favorito y pi se encarga del resto. Profundizaré en este concepto en la [siguiente entrega](https://pablocaro.es/pi-de-principiante-a-avanzado) de la serie.

## Por qué me gusta pi

A estas alturas seguramente se nota, pero por cerrar: me gusta pi porque vivo en la terminal. Porque quiero probar muchos modelos sin atarme a un proveedor. Porque personalizo todo con mis propias extensiones.

No es para todos, obviamente. Si prefieres pagar una suscripción y olvidarte, Claude Code o Codex son más directos. Pero si eres un ingeniero que vive en la terminal, pi es probablemente el mejor agente de código que existe hoy.

En los próximos artículos de esta serie:
- **[Pi de novato a usuario avanzado](https://pablocaro.es/pi-de-principiante-a-avanzado)** — Instalación, TUI, sesiones, skills, extensiones y todo lo que necesitas saber para dominarlo.
- **[Las extensiones de pi que uso](https://pablocaro.es/extensiones-pi-que-uso)** — Mi setup real con paquetes, skills y extensiones personalizadas.

*Fuente original*: [pi.dev](https://pi.dev/)
