Title: DeepDiff: La navaja suiza para comparar datos en Python
Slug: deepdiff-comparar-datos-python
Date: 2026-02-20
Tags: python, data, cli, tools, diff
Category: Python
Lang: es

Cuando trabajamos con datos estructurados en Python, a menudo necesitamos comparar dos diccionarios, JSONs u objetos complejos para encontrar qué ha cambiado. Si bien la comparación directa (`==`) es útil, a veces necesitamos entender *exactamente qué* es diferente: qué claves se han añadido, cuáles se han eliminado, o dónde han cambiado los valores, incluso en estructuras profundamente anidadas.

Aquí es donde entra **[DeepDiff](https://github.com/seperman/deepdiff)**.

DeepDiff es una biblioteca de Python increíblemente potente que ofrece mucho más que una simple comparación. Es una herramienta esencial para pruebas, validación de datos y depuración de APIs.

## Características principales

DeepDiff no es solo una herramienta, es un conjunto de utilidades:

*   **DeepDiff**: Compara diccionarios, iterables, cadenas y otros objetos recursivamente. Puede ignorar el orden en listas, ignorar tipos específicos, o excluir rutas de la comparación.
*   **DeepSearch**: Busca objetos dentro de otros objetos, como un `grep` para estructuras de datos en memoria.
*   **DeepHash**: Calcula hashes de objetos basándose en su contenido. Muy útil para deduplicación de datos complejos donde el orden de las claves no importa.
*   **Delta**: Genera "deltas" (diferencias) que se pueden aplicar a otros objetos, similar a un `git patch` pero para objetos Python.

## Instalación

La forma moderna y recomendada de instalar herramientas en Python es usando `uv`.

### Como herramienta de línea de comandos (CLI)

Si solo quieres usar el comando `deep` en tu terminal para comparar archivos JSON o YAML:

```bash
uv tool install "deepdiff[cli]"
```

Esto instalará el comando `deep` en tu sistema de forma aislada. Asegúrate de incluir `[cli]` para instalar las dependencias necesarias.

### Como biblioteca en tu proyecto

Si vas a usarlo dentro de tus scripts de Python:

```bash
uv add "deepdiff"
```

O si necesitas la CLI también dentro de tu entorno virtual:

```bash
uv add "deepdiff[cli]"
```

## Ejemplos de uso

### En Python

Imagina que tienes dos respuestas de API ligeramente diferentes y quieres saber qué cambió:

```python
from deepdiff import DeepDiff

t1 = {
    "id": 1,
    "name": "Producto A",
    "tags": ["nuevo", "oferta"],
    "details": {"price": 100, "stock": 50}
}

t2 = {
    "id": 1,
    "name": "Producto A",
    "tags": ["oferta", "nuevo"],  # Orden diferente
    "details": {"price": 120, "stock": 50}
}

# Por defecto, el orden importa en listas
diff = DeepDiff(t1, t2)
# Resultado muestra cambios en la lista 'tags' y en 'details.price'

# Si ignoramos el orden en iterables
diff_ignore_order = DeepDiff(t1, t2, ignore_order=True)
print(diff_ignore_order)
```

Salida:
```python
{
    'values_changed': {
        "root['details']['price']": {
            'new_value': 120,
            'old_value': 100
        }
    }
}
```

Como ves, detectó el cambio de precio pero ignoró el cambio de orden en los tags.

### En la terminal (CLI)

El comando `deep` es muy útil para comparar archivos rápidamente:

```bash
# Comparar dos archivos JSON
deep diff production.json development.json
```

También puedes usarlo para extraer información o buscar dentro de archivos JSON/YAML grandes sin tener que escribir un script.

## Conclusión

DeepDiff es una de esas librerías que, una vez que conoces, no puedes dejar de usar. Su flexibilidad para ignorar ciertos campos (como timestamps o IDs autogenerados) la hace perfecta para tests de integración y validación de datos.

Puedes ver la documentación completa en [zepworks.com/deepdiff](https://zepworks.com/deepdiff/current/).
