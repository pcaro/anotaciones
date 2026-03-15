Title: sem: Control de versiones semántico
Date: 2026-03-15 14:11
Category: Programación
Tags: cli, versionado, rust, herramientas
Slug: sem-control-de-versiones-semantico
Lang: es
featured_image: /images/sem-cli.png
Summary: Descubriendo sem, una herramienta CLI que entiende la semántica de tu código y te dice qué entidades cambiaron, no solo qué líneas.
Status: published

Me encontré con [sem](https://github.com/Ataraxy-Labs/sem) hace unas semanas y me parece una idea brutal. Es un CLI que va más allá del diff tradicional línea a línea y entiende la estructura real del código.

## La diferencia entre líneas y entidades

Cuando haces un `git diff` tradicional, ves algo como:

```diff
- const oldAuth = function(user) { ... }
+ const newAuth = async function(user) { ... }
```

Pero con `sem diff` ves:

```
⊕ function validateToken          [added]
∆ function authenticateUser       [modified]
⊖ function legacyAuth             [deleted]
```

No líneas añadidas o eliminadas, sino **entidades** que cambiaron: funciones, clases, métodos. Mucho más útil para entender qué pasó realmente en el PR.

## Comandos disponibles

- **`sem diff`**: Muestra qué entidades cambiaron
- **`sem impact <entidad>`**: Analiza qué se rompería si cambias esa entidad (dependencias entrantes)
- **`sem blame`**: Blame a nivel de entidad — quién cambió cada función/clase
- **`sem graph`**: Muestra el grafo de dependencias entre entidades

## Ejemplo práctico

```bash
# Ver qué entidades cambiaron en working directory
sem diff

# Ver solo cambios staged
sem diff --staged

# Ver cambios de un commit específico
sem diff --commit abc1234

# Ver impacto de cambiar una función
sem impact validateToken

# Salida JSON para pipelines CI
sem diff --format json
```

## Instalación

```bash
# macOS
brew install sem-cli

# Linux (mi caso)
brew install sem-cli
# o descargar binario de GitHub Releases
```

O build from source si tienes Rust instalado:

```bash
git clone https://github.com/Ataraxy-Labs/sem
cd sem/crates
cargo install --path sem-cli
```

## Why esto es útil

Para mí, principalmente dos casos:

1. **Code reviews más rápidas** — Entiendes el impacto real de un cambio en segundos
2. **Refactors seguros** — Antes de renombrar una función crítica, `sem impact` te dice qué puede romperse

Soporta 20 lenguajes (incluyendo Python, Rust, Go, TypeScript, Java, C++, etc.) usando tree-sitter para parsear el código.

Una herramienta que va directo a mi toolkit diario.
