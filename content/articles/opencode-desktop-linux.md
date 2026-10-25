---
Title: De OpenCode en la terminal a OpenCode Desktop (en Linux)
Date: 2026-10-25
Category: Herramientas
Tags: opencode, coding-agent, linux, claude, pi, agentes-ia
Slug: opencode-desktop-linux
Lang: es
Summary: Llevo meses usando OpenCode en la terminal. Ahora estoy probando la app de escritorio en mi Linux personal, con la misma suscripción de OpenCode Go y sin tocar la configuración.
Featured_image: /images/opencode-desktop-linux.png
---

Llevo mucho tiempo usando [OpenCode](https://opencode.ai/) dentro de la terminal. Después de pi, es el segundo agente que más utilizo, y hasta ahora no había sentido la necesidad de salir de la TUI. Estas últimas semanas estoy probando la **app de escritorio** en mi ordenador personal con Linux. En el trabajo, además, he cambiado a **Claude Desktop** en Mac.

Mi stack ahora mismo son tres agentes: [pi](https://pablocaro.es/que-es-pi-coding-agent), OpenCode (con los tokens de [OpenCode Go](https://pablocaro.es/pi-provider-opencode-console)) y Claude.

![Página de descarga de OpenCode con las opciones de escritorio para Linux](/images/opencode-desktop-linux.png)

## Tres agentes, tres interfaces

| Agente | Interfaz | Modelos | Para qué lo uso |
|---|---|---|---|
| **pi** | Terminal | OpenCode Go vía [provider](https://pablocaro.es/pi-provider-opencode-console) | Trabajo personal, sesiones largas, extensiones propias |
| **OpenCode** | Terminal + escritorio | OpenCode Go ($10/mes) | Proyectos del blog, scripts y revisión de cambios |
| **Claude** | Claude Desktop (Mac, trabajo) | Suscripción de Claude | Cosas del trabajo y tareas donde quiero Opus o Sonnet |

Los tres conviven sin pisarse porque cada uno tiene su configuración y sus credenciales. La novedad es que OpenCode ya no lo abro solo con `opencode`: cada vez más veces arranco la app.

## Lo que cambia al abrir la app

OpenCode no es un binario con una ventana pegada encima. Desde hace tiempo funciona como cliente/servidor: hay un servidor de fondo que guarda las sesiones, la configuración y los proveedores, y la TUI, la web y la app de escritorio son clientes que hablan con él.

Eso es lo importante para mi caso: **la app no es un producto distinto**. Es el mismo OpenCode con otra cara. Al abrirla encuentro las mismas sesiones, el mismo `AGENTS.md`, los mismos providers y la misma suscripción de OpenCode Go, sin volver a loguearme ni duplicar configuración.

La descarga está en [opencode.ai/download](https://opencode.ai/download), con builds para macOS (Apple Silicon e Intel), Windows (x64 y ARM64) y Linux en `.deb` y `.rpm`. En macOS también se puede instalar con Homebrew:

```bash
brew install --cask opencode-desktop
```

En Linux, con el paquete descargado:

```bash
sudo dpkg -i opencode-desktop_*.deb
```

O con `rpm` si estás en Fedora o similar. El proyecto sigue publicando builds con frecuencia, así que conviene mirar la página de descarga antes de instalarse una versión vieja de un mirror.

## Lo que me gusta

Si tengo que quedarme con dos cosas, me quedo con el **navegador integrado** y con los **diffs integrados**. Son los dos motivos por los que la app me ha enganchado.

- **Diffs integrados.** Ver el cambio completo y dejar una nota en una línea concreta es mucho más cómodo que leer `git diff` en la terminal. Es lo que más uso.
- **Navegador integrado.** Puedo abrir la web del proyecto, la documentación o el servidor de desarrollo en un panel dentro de la app, sin saltar al navegador y perder el hilo de la sesión.
- **Pestañas y sesiones por proyecto.** Puedo tener una sesión de este blog, otra de un script de Python y otra de un repositorio del trabajo en la misma ventana, sin abrir cinco terminales.
- **Terminal integrada.** Para lanzar el servidor de desarrollo o un test sin cambiar de ventana.
- **Formularios de MCP.** Cuando un servidor MCP pide un dato a mitad de una herramienta, la app muestra el formulario en vez de dejar la llamada esperando.
- **Notificaciones.** Puedo dejar una sesión trabajando y enterarme cuando termina.

## Lo que sigo haciendo en la TUI

No he abandonado la terminal, y creo que no lo voy a hacer.

- Arrancar y trabajar con el teclado sigue siendo más rápido. La TUI no tiene latencia de ventana ni clics de más.
- Para **scripts y CI**, `opencode run` es la única vía sensata. La app no sustituye eso.
- En **SSH remoto** la terminal gana por goleada. La app está pensada para tu máquina.
- Los **worktrees** y el trabajo en paralelo con varias ramas siguen siendo más cómodos desde la CLI.

Mi uso real se ha quedado así: TUI para escribir código y desktop para revisar, comparar y llevar varias sesiones a la vez.

## Conclusión

OpenCode Desktop no me ha hecho cambiar de herramienta, sino de ventana. Sigo usando la TUI para el trabajo fino y la app para revisar y coordinar sesiones, que es justo donde una interfaz gráfica aporta algo. Y como comparte servidor, configuración y proveedores con la versión de terminal, probarla no tiene ningún coste: si no me convence, cierro la ventana y sigo donde estaba.

En el trabajo uso **Claude Desktop en Mac**, no en Linux, y también me gusta: la pestaña Code trae Claude Code con sesiones en paralelo, worktrees y diffs comentados, y se siente más pulido. Pero está atado a los modelos de Claude y a un plan de pago (Pro, Max, Team o Enterprise), mientras que OpenCode me deja el mismo tipo de trabajo con el catálogo de modelos que yo elija. A día de hoy eso sigue pesando más.

*Fuente original*: [OpenCode — Download](https://opencode.ai/download).
