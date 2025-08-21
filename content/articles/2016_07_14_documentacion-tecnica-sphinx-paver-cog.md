Title: Documentación técnica con Sphinx, Paver y Cog
Date: 2016-07-14 00:47
Tags: sphinx, paver, cog, documentación, rst, automation
Lang: es
Category: Documentación
Slug: documentacion-tecnica-sphinx-paver-cog
Summary: Workflow automatizado para crear documentación técnica usando Sphinx, Paver y Cog, eliminando tareas repetitivas y errores manuales en ejemplos de código

**Doug Hellmann** presenta un workflow robusto para documentación técnica que elimina el trabajo manual repetitivo y los errores en ejemplos de código.

## El problema a resolver

> "Automation is important for my sense of well being. I hate dealing with mundane repetitive tasks."

**Desafíos comunes**:
- Mantener **ejemplos de código actualizados**
- **Múltiples formatos** de salida (HTML, PDF, blog)
- **Tareas repetitivas** de construcción y publicación
- **Errores de copy-paste** en output de programas

## La solución: Trio de herramientas

### Sphinx: Motor de documentación
- **Conversión reStructuredText** a múltiples formatos
- **Temas personalizables** con Jinja templates
- **Generación automática** de índices y referencias cruzadas

### Paver: Automatización de builds
```python
# pavement.py
@task
def html():
    """Build HTML documentation"""
    call_task('cog')
    sphinx_build('html')

@task  
def pdf():
    """Build PDF documentation"""
    call_task('cog')
    sphinx_build('latex')
    make_pdf()
```

**Resuelve**: Automatización de procesos repetitivos de construcción

### Cog: Inserción automática de código
```rst
.. cog::
   
   import cog
   import subprocess
   
   result = subprocess.run(['python', 'ejemplo.py'], 
                          capture_output=True, text=True)
   cog.out(result.stdout)

.. cog::
```

**Ventaja clave**: El output de programas se **actualiza automáticamente** al regenerar la documentación.

## Workflow de producción

### 1. Escritura en reStructuredText
```rst
Ejemplo de uso
==============

Ejecutamos el script:

.. cog::
   cog.out("$ python mi_script.py\n")
   result = subprocess.run(['python', 'mi_script.py'], 
                          capture_output=True, text=True)
   cog.out(result.stdout)
.. cog::
```

### 2. Construcción automatizada
```bash
# Un solo comando para todo
paver html

# O para múltiples destinos
paver all_formats
```

### 3. Publicación multi-destino
- **Python Module of the Week (PyMOTW)**
- **Blog personal** 
- **Sitio web del proyecto**
- **O'Reilly blog**
- **Documentación PDF**

## Ventajas del enfoque

### Consistencia garantizada
- **Ejemplos siempre actualizados** con el código real
- **Formato uniforme** across múltiples destinos
- **Sin errores de transcripción** manual

### Eficiencia maximizada
- **Un source, múltiples outputs**
- **Automatización completa** del pipeline
- **Focus en contenido**, no en proceso

### Mantenibilidad
- **Cambios en una sola fuente** se propagan automáticamente
- **Testing integrado** de ejemplos de código
- **Versionado único** para toda la documentación

## Implementación práctica

```python
# pavement.py completo
from paver.easy import *
import paver.doctools

@task
def cog():
    """Run Cog to update code examples"""
    sh('cog -r *.rst')

@task
@needs('cog')
def html():
    """Build HTML docs"""
    paver.doctools.html()

@task
@needs('cog') 
def blog_post():
    """Generate blog post version"""
    # Custom blog formatting
    pass
```

Este workflow representa la **automatización inteligente** de documentación técnica: escribes una vez, publicas en todas partes, siempre actualizado.

*Fuente original*: [Doug Hellmann](https://doughellmann.com/blog/2009/02/02/writing-technical-documentation-with-sphinx-paver-and-cog/)