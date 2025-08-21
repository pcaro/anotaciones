Cómo uso git worktrees para trabajo concurrente
###############################################

:date: 2025-07-23 06:12
:tags: git, worktrees, flujo-trabajo, productividad
:lang: es
:category: Programación
:slug: como-uso-git-worktrees
:summary: Un enfoque práctico para usar git worktrees y maximizar la productividad con múltiples contextos de trabajo simultáneos

Aleksey Kladov comparte su enfoque único para usar git worktrees, que va más allá del simple cambio de ramas y se convierte en una metodología completa para el trabajo concurrente.

.. image:: https://matklad.github.io/images/worktree-structure.png
   :alt: Estructura de worktrees
   :align: center

La filosofía central
====================

**"Git no es un sistema de control de versiones, Git es una caja de herramientas para construir un VCS"**

Esta perspectiva cambia completamente cómo pensamos sobre git. En lugar de limitarnos a las funcionalidades básicas, podemos crear nuestro propio flujo de trabajo optimizado.

Los 5 worktrees especializados
===============================

El autor mantiene 5 worktrees, cada uno con un propósito específico:

1. **main** - Snapshot de solo lectura
   - Reflejo limpio del main remoto
   - Referencia para comparaciones
   - Nunca se modifica localmente

2. **work** - Espacio de trabajo principal
   - Desarrollo activo día a día
   - Commits frecuentes con mensajes mínimos
   - HEAD desacoplado para máxima flexibilidad

3. **review** - Dedicado a revisiones de código
   - Contexto limpio para analizar PRs
   - Sin interferir con el trabajo en curso

4. **fuzz** - Pruebas de larga duración
   - Fuzzing y tests que duran horas
   - Corre en paralelo sin bloquear el desarrollo

5. **scratch** - Tareas rápidas no relacionadas
   - Experimentos
   - Fixes urgentes
   - Investigaciones puntuales

.. code-block:: bash

    # Estructura típica de directorios
    ~/projects/my-project/
    ├── main/        # worktree principal
    ├── work/        # desarrollo activo
    ├── review/      # revisiones
    ├── fuzz/        # testing
    └── scratch/     # experimentos

Ventajas del enfoque
====================

**Trabajo verdaderamente concurrente**
   - Múltiples actividades de codificación simultáneas
   - Sin necesidad de stash o branch switching complejo
   - Separación limpia de contextos

**Flujo de trabajo sin fricción**
   - Cambio instantáneo entre tareas
   - Commits frecuentes sin presión por mensajes perfectos
   - Experimentación libre en HEAD desacoplado

**Paralelización real**
   - Fuzzing corriendo mientras desarrollas
   - Reviews sin interrumpir el trabajo principal
   - Tests en background sin bloqueos

Técnicas avanzadas
==================

**HEAD desacoplado estratégico**

.. code-block:: bash

    # En el worktree 'work', trabajar sin rama
    git checkout --detach HEAD
    # Commit frecuente, reorganizar después
    git commit -m "wip"

**Scripts personalizados para operaciones comunes**

.. code-block:: bash

    # Script para crear/cambiar worktrees rápidamente
    #!/bin/bash
    git worktree add "../$1" "$2"
    cd "../$1"

**Flujo de integración**

.. code-block:: bash

    # Desde el worktree 'work'
    git log --oneline  # revisar commits
    git reset HEAD~5   # deshacer commits temporales
    git add -p         # seleccionar cambios
    git commit         # commit final limpio

Lecciones clave
===============

1. **Git es flexible**: No hay "una forma correcta" de usar git
2. **Automatiza lo repetitivo**: Scripts personalizados para operaciones comunes
3. **Separa contextos**: Cada tipo de trabajo merece su propio espacio
4. **Commits baratos**: Commitea frecuentemente, organiza después

Este enfoque transforma git de una herramienta de versionado en una plataforma completa de gestión de flujo de trabajo, maximizando la productividad a través del trabajo verdaderamente concurrente.

*Artículo original*: `How I Use Git Worktrees`_

.. _How I Use Git Worktrees: https://matklad.github.io/2024/07/25/git-worktrees.html