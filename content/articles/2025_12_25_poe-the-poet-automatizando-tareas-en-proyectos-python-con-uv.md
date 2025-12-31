---
title: Poe the Poet: Automatizando tareas en proyectos Python con uv
date: 2025-12-25 11:00
tags: python, uv, poethepoet, automatizacion, pyproject.toml
lang: es
category: Programación
slug: poe-the-poet-automatizando-tareas-en-proyectos-python-con-uv
summary: Descubre cómo Poe the Poet te permite definir y ejecutar comandos personalizados directamente desde tu pyproject.toml, optimizando tu flujo de trabajo en entornos uv.
---

La gestión de proyectos Python a menudo implica la ejecución de diversas tareas personalizadas, desde la construcción de documentación hasta la ejecución de tests o scripts auxiliares. Si bien `uv` ha simplificado enormemente la gestión de dependencias, la forma de integrar y ejecutar estos comandos directamente desde `pyproject.toml` ha sido un punto de debate. Aquí es donde **Poe the Poet** emerge como una solución elegante y efectiva.

## ¿Qué es Poe the Poet?

Poe the Poet es una herramienta que permite definir "scripts" o "tareas" personalizadas directamente en tu archivo `pyproject.toml`. Estas tareas pueden ser cualquier comando que quieras ejecutar en el contexto de tu entorno Python, haciendo que la automatización del flujo de trabajo sea mucho más limpia y centralizada. Resuelve el problema de tener que recurrir a `Makefile` u otros scripts externos para tareas específicas del proyecto.

## Cómo Usar Poe the Poet con uv

La integración de Poe the Poet en un proyecto que usa `uv` es sencilla:

1.  **Añadir `poethepoet` a tus dependencias de desarrollo:**
    Primero, asegúrate de que `poethepoet` esté incluido en tu grupo de dependencias de desarrollo (por ejemplo, `dev`) en `pyproject.toml`.

```toml
[project]
# ... otras configuraciones del proyecto ...

[tool.uv]
dev-dependencies = [
    "black",
    "ruff",
    "poethepoet>=0.38.0", # Añade Poe the Poet aquí
]
```

2.  **Definir tareas personalizadas:**
    Luego, puedes añadir una sección `[tool.poe.tasks]` en tu `pyproject.toml` para definir tus comandos personalizados.

```toml
[tool.poe.tasks]
docs = "sphinx-build -M html docs docs/_build"
livehtml = "sphinx-autobuild -b html docs docs/_build"
cog = "cog -r docs/*.md"
```

## Ejecutando Tareas con `uv run`

Una vez que Poe the Poet está configurado y tus tareas están definidas, puedes ejecutarlas fácilmente usando `uv run`:

```bash
# Para construir la documentación
uv run poe docs

# Para el servidor de previsualización en vivo
uv run poe livehtml

# Para ejecutar el comando 'cog'
uv run poe cog
```

## Beneficios

*   **Centralización:** Todas tus tareas personalizadas viven en `pyproject.toml`, junto a tus dependencias.
*   **Integración con `uv`:** Las tareas se ejecutan en el entorno virtual gestionado por `uv`, asegurando que todas las herramientas necesarias estén disponibles.
*   **Simplificación:** Evita la necesidad de `Makefile` o scripts bash complejos para tareas comunes.
*   **Consistencia:** Promueve un flujo de trabajo más consistente y fácil de compartir entre colaboradores.

Poe the Poet ofrece una forma robusta y elegante de extender las capacidades de `uv` para la automatización de tareas en proyectos Python, mejorando la experiencia de desarrollo.

*Artículo original*: [Poe the Poet - Simon Willison's Weblog](https://simonwillison.net/2025/Dec/16/poe-the-poet/#atom-everything)
