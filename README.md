# Anotaciones - Blog de Pablo Caro

Este repositorio contiene mi blog ([anotaciones](http://pablocaro.es)) generado con Pelican.

Las configuraciones y convenciones detalladas (pensadas para agentes e IAs) están documentadas en `AGENTS.md`. Este README es solo una referencia rápida (para mí) de los comandos de desarrollo.

## Flujo de Trabajo (Tasks)

Todo el flujo local se gestiona mediante `invoke` a través de `uv`.

### Levantar el entorno de desarrollo

```bash
uv run invoke develop
```
Realiza una compilación inicial completa, arranca un servidor local en `http://localhost:7000` (con soporte para URLs limpias) y deja a Pelican "escuchando" en segundo plano. Cualquier cambio en los archivos `.md` reconstruirá el HTML al instante. 
*(Para detenerlo y limpiar los procesos, pulsa `Ctrl+C`).*

### Crear una nueva entrada

```bash
uv run invoke write "Título de tu nueva entrada"
```
Genera automáticamente las dos plantillas obligatorias (`.md` y `.en.md`) en `content/articles/` con los metadatos correctos (fecha, slug, etc.) listas para empezar a escribir.

### Editar la última entrada generada/modificada

```bash
uv run invoke edit-latest
```
Busca la entrada más reciente en la carpeta `content/articles/` (por fecha de modificación) y abre tanto su versión en español como en inglés simultáneamente en tu `$EDITOR` (por defecto `vim`). Es el comando ideal para revisar rápidamente las notas que te acaba de generar una IA.

### Limpieza de código

```bash
uv run invoke format-code   # Formatea Python con black
uv run invoke lint          # Revisa Python con ruff
```

---

## Despliegue

El blog se publica **automáticamente** vía GitHub Actions al hacer `git push` a `master`. No hagas push a master sin haber revisado los cambios en local previamente.