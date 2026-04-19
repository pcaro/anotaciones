---
Title: broot, una forma diferente de navegar por tus directorios
Date: 2026-01-02 10:00
Tags: terminal, cli, broot, rust, herramientas
Lang: es
Category: Herramientas
Slug: broot-una-forma-diferente-de-navegar-directorios
Summary: broot es una herramienta para la terminal que permite explorar directorios de forma interactiva, con búsqueda fuzzy, paneles múltiples y previsualización de archivos.
featured_image: /images/broot_terminal.png
---

Llevaba tiempo buscando un reemplazo para `ls` y `tree` que me permitiera navegar por directorios grandes sin perder el contexto. broot es la herramienta que necesitaba.

## Instalación

```bash
# Con cargo (Rust)
cargo install broot

# O con tu gestor de paquetes
brew install broot  # macOS
apt install broot   # Debian/Ubuntu
```

## Primeros pasos

El comando básico es simplemente `br` (puedes crear un alias para que reemplace a `cd`):

```bash
br
```

Esto abre una vista de árbol interactiva del directorio actual. Las teclas principales:

- `↓` / `↑` - Navegar entre archivos y directorios
- `/` - Búsqueda fuzzy (ej: `/config` encuentra todos los archivos con "config" en el nombre)
- `Enter` - Entrar en un directorio
- `alt + Enter` - Hacer `cd` al directorio seleccionado y salir de broot
- `:e` - Abrir el archivo seleccionado con el editor definido en `$EDITOR`
- `:q` - Salir

## Características que uso

### Búsqueda sin perder el contexto

A diferencia de `find`, broot muestra dónde está cada resultado dentro del árbol de directorios:

```bash
br
/pytest  # Encuentra todos los archivos/directorios con "pytest"
```

Esto es útil cuando sabes el nombre de un archivo pero no recuerdas en qué carpeta está.

### Paneles múltiples

Puedes dividir la vista para comparar o mover archivos entre directorios:

```
:pp  # Crear panel derecho
:pc  # Crear panel inferior
:pt  # Intercambiar paneles
```

En cada panel puedes navegar independientemente y usar verbos como `:copy` o `:move`.

### Previsualización de archivos

Selecciona un archivo y usa `:preview` para ver su contenido sin salir de broot. Para imágenes en terminales que lo soporten (kitty, iterm2):

```bash
:preview
```

### Ver solo archivos relevantes

broot oculta automáticamente archivos ignorados por Git y directorios comunes como `node_modules`. Para verlos:

```bash
:show_git_ignored
```

### Verbos personalizados

En `~/.config/broot/conf.toml` puedes añadir comandos personalizados:

```toml
[[verbs]]
name = "edit"
invocation = "e"
execution = "$EDITOR {file}"

[[verbs]]
name = "git status"
invocation = "gs"
execution = "git status"
```

## Integración con el shell

Para usar `br` como reemplazo de `cd`, añade esto a tu `.bashrc` o `.zshrc`:

```bash
# Esto permite que br cambie el directorio del shell padre
source /usr/share/broot/launcher/bash/br
```

Ahora `br directorio` te deja en ese directorio al salir.

## Cuándo usar broot

- Navegar por proyectos grandes con muchas carpetas
- Buscar archivos cuando no recuerdas la ruta exacta
- Mover/copiar archivos entre directorios distantes
- Explorar directorios con muchos archivos ignorados por Git

## Enlaces

- [Documentación oficial](https://dystroy.org/broot/)
- [Repositorio GitHub](https://github.com/Canop/broot)

*Fuente original*: [Documentación de broot](https://dystroy.org/broot/)

![broot terminal interface]({static}/images/broot_terminal.png)
