---
title: Pluggy — A plugin framework to use in your projects
slug: pluggy-plugins-python
lang: en
date: 2026-06-15
category: Programación
tags: plugins, python, pytest, testing, herramientas
featured_image: /images/pluggy-pluggy-logo.png
Summary: Pluggy is the plugin framework behind pytest, Datasette, and other Python projects. Eli Bendersky recently analyzed whether it's worth using, and the answer is: it depends.
---

The two use cases I know best for Pluggy are **pytest** and **Datasette**. pytest has arguably the richest plugin ecosystem in all of Python, and the entire system — `conftest.py`, markers, fixtures, reporters — runs on Pluggy. Datasette is the other one I follow closely: Simon Willison uses it so anyone can extend Datasette with new hooks without touching the core. In fact, Pluggy was born by extracting pytest's plugin system so other projects like Datasette could reuse it.

I recently came across an article by **Eli Bendersky** — one of those he writes every so often that are always worth reading — where he analyzes Pluggy as a plugin systems case study. Eli has a whole [series on plugin fundamentals](https://eli.thegreenplace.net/tag/plugins), and here he applies his conceptual framework to Pluggy.

![Eli Bendersky plugins](/images/pluggy-pluggy-logo.png)

## Is Pluggy a shallow API?

Eli is quite clear in his verdict, and I agree:

> Plugin frameworks are very easy to create, and the functionality they provide is relatively small compared to their large surface area. In other words, this is a *shallow API*.

A *shallow* API — little depth for a lot of interface. He's right. A crappy plugin system in Python is four lines with `__init_subclass__` or `entry_points`. But the question is what exactly you need.

## What Pluggy actually brings to the table

Where Pluggy makes a difference is when you need some of these features:

- **Automatic entry point registration** — if you need it
- **Signature validation** for hooks
- **Consistent result collection** across multiple hooks in a single plugin and across many plugins
- **Plugin ordering** with `firstresult`, `tryfirst`, `trylast`, etc.
- **Hook "wrappers"** for advanced use cases

The two I care about most are signature validation and plugin ordering. Signature validation saves you from the classic bug where your plugin has a function with wrong parameters and the system silently ignores it. And ordering is key when you have multiple plugins competing for the same hook; being able to say "this one goes first" or "this one goes last" without implementing a priority system yourself saves a lot of effort.

Eli ends with the right question:

> Are these worthwhile for your project? It really depends on the project, and it's always worth keeping the tradeoff between dependencies and project effort in mind.

Pluggy is a lightweight dependency, but it's still a dependency. If your plugin system has three hooks and two plugins, you probably don't need it. If you have an open plugin ecosystem like Datasette or pytest, it makes perfect sense.

## How to use Pluggy in tests

Simon Willison has two practical TILs on Pluggy worth saving here as a reference.

### Registering temporary plugins in tests

In [Registering temporary pluggy plugins inside tests](https://til.simonwillison.net/pytest/registering-plugins-in-tests), Simon shows how to register a Datasette plugin for the duration of a single test using `pm.register()` and `pm.unregister()`:

```python
from datasette import hookimpl
from datasette.plugins import pm
import pytest

def test_using_test_plugin():
    class TestPlugin:
        __name__ = "TestPlugin"

        @hookimpl
        def permission_allowed(self, datasette, actor, action):
            if action.startswith("insert-api:"):
                return permissions.get(action.replace("insert-api:", ""))

    pm.register(TestPlugin(), name="undo")
    try:
        # Rest of test goes here
    finally:
        pm.unregister(name="undo")
```

The `try/finally` pattern is key to not leaving the plugin registered after the test. You can also use a pytest fixture:

```python
@pytest.fixture
def unsafe():
    class UnsafeInsertAll:
        __name__ = "UnsafeInsertAll"

        @hookimpl
        def permission_allowed(self, action):
            if action == "insert:all":
                return True

    pm.register(UnsafeInsertAll(), name="undo")
    yield
    pm.unregister(name="undo")
```

This is very powerful for integration tests where you need to mock plugin behaviors without creating an actual plugin.

### Registering multiple hooks in a single file

In [Registering the same Pluggy hook multiple times in a single file](https://til.simonwillison.net/pluggy/multiple-hooks-same-file), Simon explains how to register two implementations of the same hook in one module using `specname`:

```python
from datasette import hookimpl

@hookimpl(specname="menu_links", tryfirst=True)
def menu_links_1(datasette):
    return [
        {"href": datasette.urls.path("/"), "label": "Home"},
    ]

@hookimpl(specname="menu_links", trylast=True)
def menu_links_2():
    return [
        {
            "href": "http://www.example.com/",
            "label": "Link at the end",
        },
    ]
```

The function isn't called `menu_links` but `menu_links_1` and `menu_links_2`, and `specname` tells Pluggy which hook each one implements. This requires **Pluggy 1.0.0+** (which has been around for a while, so you likely have it if you're using anything modern). Combined with `tryfirst`/`trylast`, it's a clean way to contribute multiple things to the same hook from a single plugin.

*Original source*: [Plugins case study: Pluggy](https://eli.thegreenplace.net/2026/plugins-case-study-pluggy/) — Eli Bendersky
