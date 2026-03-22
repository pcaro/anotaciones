Title: Crit: El bucle de revisión para Agentes
Date: 2026-03-22 14:49
Category: Programación
Tags: ai, agents, review, opencode, productivity
Slug: crit-review-loop-agents
Lang: es
featured_image: /images/crit-demo.png
Summary: Crit es una herramienta diseñada para cerrar el bucle de revisión de código generado por agentes de IA, proporcionando una interfaz web intuitiva y eficiente.
Status: published

Revisar lo que un agente de IA escribe directamente en la terminal es, a menudo, una pesadilla. No puedes señalar una línea concreta, dar feedback estructurado y, cuando el agente actualiza el archivo, te toca volver a leerlo todo para ver qué ha cambiado realmente. 

Ahí es donde entra **Crit**.

![Crit review UI](/images/crit-demo.png)

Crit abre los archivos generados o modificados por tu agente en el navegador con una interfaz al estilo GitHub. Puedes dejar comentarios en líneas específicas, sugerencias de cambio y, lo mejor de todo, ver los diffs entre las distintas rondas de iteración. 

Lo que más me ha gustado es su enfoque **multi-agente** y su **usabilidad**. No importa si usas Claude Code, Cursor, Aider o, como en mi caso, **OpenCode**. Crit se integra de maravilla.

### Instalación y configuración

La instalación es tan sencilla como:

```bash
gah install tomasz-tomczyk/crit
```

Una vez instalado, integrarlo con OpenCode es cuestión de un comando:

```bash
crit install opencode
```

Esto instala los comandos y las *skills* necesarias para que los agentes puedan usar Crit. Al ejecutar `/crit` en OpenCode, se inicia el bucle de revisión: el agente propone un plan o cambios, Crit abre la interfaz web para que tú des el visto bueno o corrijas, y el agente recibe tu feedback estructurado en un archivo `.crit.json` para actuar en consecuencia.

> **Nota para mi yo del futuro:** Si usas [pi-agent](https://shittycodingagent.ai/) en vez de OpenCode, puedes copiar el comando de OpenCode como prompt y copiar el skill de crit tal cual — funciona perfectamente. De hecho, esta misma anotación ha sido revisada usando pi-agent con Crit.

### Por qué usarlo

- **Interfaz Web, no TUI**: Renderizado de Markdown y diffs visuales persistentes.
- **Diffs entre rondas**: Ves exactamente qué ha cambiado desde tu último comentario.
- **Agnóstico al agente**: Funciona con cualquier herramienta, permitiendo un flujo de trabajo consistente.
- **Sugerencias directas**: Puedes insertar sugerencias que el agente puede aplicar tal cual.

Por ejemplo, el propio cambio que subsanó el problema de la coma de esta misma anotación:

![Ejemplo de revisión con Crit](/images/crit-review-example.png)

Es, sin duda, la pieza que faltaba para que el trabajo con agentes sea realmente colaborativo y no una sucesión de "copy-pasted" y revisiones manuales tediosas.

