---
title: wrapture — monkey patching and observability in a single mechanism
slug: wrapture
lang: en
date: 2026-09-16
category: Programación
tags: python, monkey-patching, testing, observability, opentelemetry, wrapt
featured_image: /images/wrapture.png
Summary: wrapture is Graham Dumpleton's new monkey patching library (author of wrapt) that combines testing and observability through a single mechanism. Configurable from a TOML file without touching application code.
---

[Simon Willison](https://simonwillison.net/2026/Sep/11/wrapture/) has published a note recommending **wrapture**, the new library by [Graham Dumpleton](https://grahamdumpleton.me/posts/2026/08/introducing-wrapture/) (author of `wrapt` and `autowrapt`). Released on August 31st, it's in beta ahead of 1.0.0 but already very usable. Its motto: *"Wrap anything, capture everything, change nothing"*.

![wrapture documentation](/images/wrapture.png)

## What it is

`wrapture` (`wrapt` + `capture`) is a Python library for attaching bindings to arbitrary call sites, without modifying the code being observed. One mechanism, three uses:

1. **Monkey patching**: a clean lifecycle and behaviour vocabulary over `wrapt.wrap_object()`: stub, fail, transform arguments or results, and remove again, with honest reporting if something else displaced the patch.
2. **Unit testing**: observe and assert how calls actually flowed through the real call graph (nesting, ordering, arguments and return values) and optionally intervene. Unlike a `unittest.mock` `Mock` (which fabricates values and can't see calls an object makes to itself), wrapture watches the real code run and offers strict `stub()` and `mock()` stand-ins.
3. **Ad-hoc tracing**: attach bindings to a running application — even one you cannot modify — and emit a structured, nested trace.

## What catches my eye

**Configuration without touching code**: with a `wrapture.toml` naming the methods and a sink, you just run:

```bash
python -m wrapture manage.py runserver
```

And with `autowrapt` installed, not even the launcher is needed:

```bash
AUTOWRAPT_BOOTSTRAP=wrapture python manage.py runserver
```

**OpenTelemetry export**: the same recorded events can be sent to any OTLP backend as traces, metrics and correlated logs, enabled by one `[otel]` table in the config, with trace identity propagated via W3C `traceparent` headers between services.

**Packaged instrumentation**: the [wrapture-instrumentation](https://github.com/GrahamDumpleton/wrapture-instrumentation) package covers `flask`, `django`, `fastapi`, `starlette`, `aiohttp`, `httpx`, `requests`, `sqlalchemy`, `sqlite3`, `grpc`, `jinja2`, `uvicorn` and more.

## Minimal example

```python
place = wrapture.binding(OrderService, "place")
charge = wrapture.binding(Gateway, "charge")
record = wrapture.binding(Ledger, "record")

with wrapture.timeline(place, charge, record) as tape:
    OrderService().place(500)

print(tape.tree())
```

None of those classes know they are being observed.

Graham publishes [tutorials almost daily](https://wrapture.readthedocs.io/en/latest/blog-posts-and-workshops.html) and there are [interactive workshops](https://github.com/GrahamDumpleton/wrapture-workshops) as JupyterLab notebooks. The idea that a test monkey patch can grow into production observability without rewriting code feels like a Swiss Army knife that will keep paying off for years.

*Source*: [Don't sleep on wrapture — Simon Willison](https://simonwillison.net/2026/Sep/11/wrapture/)