Title: Joyas ocultas en pi-powerline-footer
Date: 2026-03-22
Category: DevOps
Tags: pi, terminal, productivity
Slug: powerline-footer-hidden-gems
Summary: Dos características del plugin pi-powerline-footer que van más allá del típico footer con información del modelo.
featured_image: /images/pi-powerline-footer.png
Lang: es

![Captura de pantalla del plugin pi-powerline-footer](/images/pi-powerline-footer.png)

Llevo usando [pi-powerline-footer](https://github.com/nicobailon/pi-powerline-footer) un tiempo, principalmente por su funcionalidad principal: ese footer con información útil del modelo, contexto, tokens y coste. Pero hace poco descubrí dos features que han cambiado cómo trabajo con pi en el día a día.

## Editor Stash: tu portapapeles temporal integrado

Con `Alt+S` puedes guardar el contenido actual del editor, limpiarlo, escribir algo rápido (por ejemplo, una pregunta corta a otro agente), y cuando termine, tu texto original vuelve automáticamente.

Es perfecto cuando estás en medio de una tarea compleja y necesitas hacer una consulta rápida sin perder el contexto. O cuando quieres guardar un bloque de código que vas a reutilizar después.

Además, tienes atajos para copiar (`ctrl+alt+c`) y cortar (`ctrl+alt+x`) el contenido completo del editor, y un historial de stashs accesible con `ctrl+alt+h` que persiste entre sesiones.

## Model Profiles: navegación rápida entre configuraciones de modelo

Esta es la feature que más uso ahora mismo. Con varios providers activos —principalmente [OpenRouter](https://openrouter.ai/) (con sus muchísimos modelos), [Google Gemini](https://ai.google.dev/) y [OpenCode](https://opencode.ai/)— cambiar entre modelos era un lío.

Los Model Profiles guardan combinaciones de modelo + nivel de thinking. Los defino en `~/.pi/agent/settings.json`:

```json
{
  "modelProfiles": [
    { "model": "google/gemini-3-pro", "thinking": "high", "label": "Gemini Deep" },
    { "model": "anthropic/claude-opus-4-5", "thinking": "xhigh", "label": "Opus Ultra" },
    { "model": "openai/codex-5.3", "thinking": "low", "label": "Codex Fast" }
  ]
}
```

Con `alt+shift+tab` ciclo entre perfiles y con `ctrl+alt+m` abro un selector visual. El cambio es instantáneo —no más menúes interminables buscando el modelo exacto.

Es especialmente útil con OpenRouter, donde la lista de modelos es enorme. En lugar de navegar por todos, tengo mis 3-4 configuraciones preferidas y alterno entre ellas según la tarea.

## El footer es solo el principio

La documentación del plugin está llena de pequeñas utilidades: [Working Vibes](https://github.com/nicobailon/pi-powerline-footer?tab=readme-ov-file#working-vibes) para mensajes de carga temáticos, atajos de teclado configurables, integración con git... Pero estas dos features que he descrito son las que más impacto tienen en mi flujo de trabajo diario.

Si aún no lo has probado: `pi install npm:pi-powerline-footer` y luego `/reload`.
