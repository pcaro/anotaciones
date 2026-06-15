---
title: Pluggy — Un framework de plugins para usar en tus proyectos
slug: pluggy-plugins-python
lang: es
date: 2026-06-15
category: python
tags: pluggy, plugins, python, pytest, simon-willison, testing
featured_image: /images/pluggy-pluggy-logo.png
Summary: Pluggy es el framework de plugins que usa pytest, Datasette, y otros proyectos Python. Apareció en un artículo reciente de Eli Bendersky donde analiza si merece la pena, y la respuesta es: depende.
---

Los dos usos que más conozco de Pluggy son **pytest** y **Datasette**. pytest tiene posiblemente el ecosistema de plugins más rico de todo el ecosistema Python, y todo ese sistema — los `conftest.py`, los markers, los fixtures, los reporters — funciona sobre Pluggy. Datasette es el otro ejemplo que sigo de cerca: Simon Willison lo usa para que cualquiera pueda extender Datasette con nuevos hooks sin tocar el core. De hecho, Pluggy nació extrayendo el sistema de plugins de pytest para que otros proyectos como Datasette pudieran reutilizarlo.

Hace poco cayó en mis manos un artículo de **Eli Bendersky** — de esos que escribe cada cierto tiempo y que merecen la pena — donde analiza Pluggy como caso de estudio de sistemas de plugins. Eli tiene toda una [serie sobre fundamentos de plugins](https://eli.thegreenplace.net/tag/plugins) y aquí aplica su framework conceptual a Pluggy.

![Eli Bendersky plugins](/images/pluggy-pluggy-logo.png)

## ¿Es Pluggy una shallow API?

Eli es bastante claro en su veredicto, y estoy de acuerdo:

> Plugin frameworks are very easy to create, and the functionality they provide is relatively small compared to their large surface area. In other words, this is a *shallow API*.

O sea: los frameworks de plugins son fáciles de crear, y la funcionalidad que aportan es pequeña en comparación con su superficie de API. Una API *shallow* — poca profundidad para mucho interfaz. Tiene razón. Hacer un sistema de plugins cutre en Python son cuatro líneas con `__init_subclass__` o `entry_points`. Pero la cuestión es qué necesitas exactamente.

## Lo que realmente aporta Pluggy

Donde Pluggy marca la diferencia es cuando necesitas algunas de estas funcionalidades:

- **Registro automático via entry points** — si lo necesitas
- **Validación de firmas** de los hooks
- **Recolección consistente de resultados** entre múltiples hooks en un mismo plugin y entre varios plugins
- **Ordenación de plugins** con `firstresult`, `tryfirst`, `trylast`, etc.
- **Hook "wrappers"** para casos de uso avanzados

Las dos que más me interesan son la validación de firmas y la ordenación de plugins. La validación de firmas te evita el clásico bug de que tu plugin tenga una función con parámetros incorrectos y el sistema lo ignore silenciosamente. Y la ordenación es clave cuando tienes varios plugins compitiendo por el mismo hook; poder decir "este va primero" o "este va al final" sin tener que implementar un priority system tú mismo ahorra mucho.

Eli concluye con la pregunta correcta:

> Are these worthwhile for your project? It really depends on the project, and it's always worth keeping the tradeoff between dependencies and project effort in mind.

Pluggy es una dependencia ligera, pero sigue siendo una dependencia. Si tu sistema de plugins tiene tres hooks y dos plugins, probablemente no la necesites. Si tienes un ecosistema de plugins abierto como Datasette o pytest, tiene todo el sentido.

## Cómo se usa Pluggy en tests

Simon Willison tiene dos TILs prácticos sobre Pluggy que merecen ser guardados aquí como referencia.

### Registrar plugins temporales en tests

En [Registering temporary pluggy plugins inside tests](https://til.simonwillison.net/pytest/registering-plugins-in-tests), Simon muestra cómo registrar un plugin de Datasette para la duración de un test concreto usando `pm.register()` y `pm.unregister()`:

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

El patrón `try/finally` es la clave para no dejar el plugin registrado después del test. También se puede hacer con un fixture de pytest:

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

Esto es muy potente para tests de integración donde necesitas mockear comportamientos de plugins sin tener que crear un plugin real.

### Registrar múltiples hooks en un mismo fichero

En [Registering the same Pluggy hook multiple times in a single file](https://til.simonwillison.net/pluggy/multiple-hooks-same-file), Simon explica cómo registrar dos implementaciones del mismo hook en un solo módulo usando `specname`:

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

La función no se llama `menu_links` sino `menu_links_1` y `menu_links_2`, y el parámetro `specname` le dice a Pluggy qué hook implementa cada una. Esto requiere **Pluggy 1.0.0+** (que tiene ya unos años, así que probablemente lo tengas si usas algo moderno). Combinado con `tryfirst`/`trylast`, es una forma limpia de aportar múltiples contribuciones al mismo hook desde un único plugin.

*Fuente original*: [Plugins case study: Pluggy](https://eli.thegreenplace.net/2026/plugins-case-study-pluggy/) — Eli Bendersky
