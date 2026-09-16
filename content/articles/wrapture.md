---
title: wrapture — monkey patching y observabilidad en un solo mecanismo
slug: wrapture
lang: es
date: 2026-09-16
category: Programación
tags: python, monkey-patching, testing, observabilidad, opentelemetry, wrapt
featured_image: /images/wrapture.png
Summary: wrapture es la nueva librería de monkey patching de Graham Dumpleton (autor de wrapt) que combina testing y observabilidad con un único mecanismo. Configurable desde un archivo TOML sin tocar el código de la aplicación.
---

[Simon Willison](https://simonwillison.net/2026/Sep/11/wrapture/) ha publicado una nota recomendando **wrapture**, la nueva librería de [Graham Dumpleton](https://grahamdumpleton.me/posts/2026/08/introducing-wrapture/) (el autor de `wrapt` y `autowrapt`). Se lanzó el 31 de agosto y está en beta antes de 1.0.0, pero ya es muy usable. Su lema: *"Wrap anything, capture everything, change nothing"*.

![Documentación de wrapture](/images/wrapture.png)

## Qué es

`wrapture` (`wrapt` + `capture`) es una librería Python para enlazar bindings a puntos de llamada arbitrarios, sin modificar el código observado. Un solo mecanismo con tres usos:

1. **Monkey patching**: ciclo de vida y vocabulario de comportamiento limpio sobre `wrapt.wrap_object()`: stub, fallo, transformación de argumentos o resultados, y reversión con detección honesta de parches desplazados.
2. **Testing unitario**: observa y asevera cómo fluyeron las llamadas por el grafo real (anidamiento, orden, argumentos y retornos) e interviene opcionalmente. A diferencia de un `Mock` de `unittest.mock` (que fabrica valores y no ve llamadas que un objeto se hace a sí mismo), wrapture observa el código real y ofrece `stub()` y `mock()` estrictos.
3. **Tracing ad-hoc**: adjunta bindings a una aplicación en ejecución —incluso una que no puedes modificar— y emite un trace estructurado y anidado.

## Lo que me llama la atención

**Configuración sin tocar código**: con un archivo `wrapture.toml` que nombra los métodos y un sink, basta con:

```bash
python -m wrapture manage.py runserver
```

Y con `autowrapt` instalado, ni siquiera el lanzador:

```bash
AUTOWRAPT_BOOTSTRAP=wrapture python manage.py runserver
```

**Export a OpenTelemetry**: los mismos eventos registrados se pueden enviar a cualquier backend OTLP como traces, métricas y logs correlacionados con una tabla `[otel]` en la config, con identidad de trace propagada por cabeceras W3C `traceparent` entre servicios.

**Instrumentación empaquetada**: el paquete [wrapture-instrumentation](https://github.com/GrahamDumpleton/wrapture-instrumentation) cubre `flask`, `django`, `fastapi`, `starlette`, `aiohttp`, `httpx`, `requests`, `sqlalchemy`, `sqlite3`, `grpc`, `jinja2`, `uvicorn` y más.

## Ejemplo mínimo

```python
place = wrapture.binding(OrderService, "place")
charge = wrapture.binding(Gateway, "charge")
record = wrapture.binding(Ledger, "record")

with wrapture.timeline(place, charge, record) as tape:
    OrderService().place(500)

print(tape.tree())
```

Ninguna de las clases sabe que está siendo observada.

Graham publica [tutoriales casi a diario](https://wrapture.readthedocs.io/en/latest/blog-posts-and-workshops.html) y hay [workshops interactivos](https://github.com/GrahamDumpleton/wrapture-workshops) en JupyterLab. La idea de que un monkey patch de test pueda crecer hasta convertirse en observabilidad de producción sin reescribir código me parece una navaja suiza que dará juego durante años.

*Fuente original*: [Don't sleep on wrapture — Simon Willison](https://simonwillison.net/2026/Sep/11/wrapture/)