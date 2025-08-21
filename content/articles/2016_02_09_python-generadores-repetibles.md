Title: Python: Crear generadores repetibles (repeating generators)
Date: 2016-02-09 10:10
Tags: python, generadores, itertools, decoradores, yield
Lang: es
Category: Python
Slug: python-generadores-repetibles
Summary: Técnicas en Python para crear generadores que se pueden iterar múltiples veces, superando la limitación de "una sola vez" de los generadores estándar

Los **generadores en Python son "one-shot"** - solo se pueden iterar una vez. ¿Cómo crear generadores que se puedan reutilizar múltiples veces?

## El problema

```python
def mi_generador():
    yield 1
    yield 2
    yield 3

gen = mi_generador()
print(list(gen))  # [1, 2, 3]
print(list(gen))  # [] - ¡Vacío!
```

## Solución 1: Enfoque con clase (Más robusto)

```python
def multigen(gen_func):
    class _multigen(object):
        def __init__(self, *args, **kwargs):
            self.__args = args
            self.__kwargs = kwargs
        def __iter__(self):
            return gen_func(*self.__args, **self.__kwargs)
    return _multigen

# Uso
@multigen
def mi_generador_repetible(max_num):
    for i in range(max_num):
        yield i

gen = mi_generador_repetible(3)
print(list(gen))  # [0, 1, 2]
print(list(gen))  # [0, 1, 2] - ¡Funciona!
```

## Solución 2: itertools.cycle() para secuencias infinitas

```python
import itertools

# Repetir infinitamente una secuencia
repeating_gen = itertools.cycle([1, 2, 3])

# Tomar solo los primeros 9 elementos
resultado = list(itertools.islice(repeating_gen, 9))
print(resultado)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

## Solución 3: Lambda wrapper (Simple)

```python
def mi_generador():
    yield 1
    yield 2
    yield 3

# Wrapper para crear nueva instancia cada vez
generador_repetible = lambda: mi_generador()

print(list(generador_repetible()))  # [1, 2, 3]
print(list(generador_repetible()))  # [1, 2, 3]
```

## Solución 4: Función factory

```python
def crear_generador(datos):
    def generador():
        for item in datos:
            yield item
    return generador

# Uso
gen_factory = crear_generador([1, 2, 3])
gen1 = gen_factory()
gen2 = gen_factory()

print(list(gen1))  # [1, 2, 3]
print(list(gen2))  # [1, 2, 3]
```

## ¿Cuándo usar cada enfoque?

### Clase decorador (`@multigen`)
- **Generadores complejos** con parámetros
- **Máxima flexibilidad** y reutilización
- **Preserva metadatos** del generador original

### `itertools.cycle()`
- **Repetición infinita** de secuencias pequeñas
- **Patrones cíclicos** conocidos
- **Muy eficiente** en memoria

### Lambda wrapper
- **Casos simples** sin parámetros
- **Prototipado rápido**
- **Generadores sin estado**

### Factory function
- **Balance** entre simplicidad y flexibilidad
- **Generadores con configuración inicial**
- **Código más explícito**

## Consideraciones de rendimiento

⚠️ **Memoria**: Los generadores repetibles pueden requerir almacenar parámetros iniciales  
⚠️ **CPU**: Cada iteración recalcula desde el inicio

La elección depende de si necesitas **repetición exacta** o **reutilización eficiente**.

*Fuente original*: [Stack Overflow](http://stackoverflow.com/questions/1376438/how-to-make-a-repeating-generator-in-python/1376531#1376531)