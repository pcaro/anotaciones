---
title: Detectando secretos en git con gitleaks
slug: gitleaks-deteccion-secrets-git
lang: es
date: 2026-05-28
category: herramientas
tags: git, seguridad, gitleaks, herramientas, cli
featured_image: /images/gitleaks-deteccion-secrets-git.png
Summary: gitleaks escanea repositorios git en busca de secretos, claves API y contraseñas filtradas. Se instala en segundos con gah y puede ahorrarte un disgusto.
---

![gitleaks detectando secretos en un repo git](/images/gitleaks-deteccion-secrets-git.png)

`gitleaks` es una herramienta que escanea repositorios git —incluyendo todo el historial— en busca de secretos: claves API, contraseñas, tokens de AWS, credenciales de base de datos y más de 150 patrones predefinidos.

## Instalación con gah

La forma más rápida de instalarlo en Linux es con [`gah`](https://github.com/user/gah), un descargador de assets de GitHub releases:

```bash
$ gah install gitleaks/gitleaks
Fetching release info for: gitleaks/gitleaks [latest]
Found release: v8.30.1
Downloading: gitleaks_8.30.1_linux_x64.tar.gz
############################################### 100.0%
Verifying digest sha256 551f6fc8... ...
Digest verification succeeded!
Extracting: gitleaks_8.30.1_linux_x64.tar.gz
Installing: gitleaks
Done!
```

Binario único, sin dependencias, listo en segundos.

## Uso básico

Para escanear un repo local, incluyendo todo el historial de commits:

```bash
$ gitleaks git --verbose -v /ruta/al/repo
```

Esto rastrea cada commit y te muestra qué secretos encontró, en qué archivo y en qué línea.

Algunas flags útiles:

- `--no-banner`: quita el banner ASCII al inicio.
- `--exit-code 0`: no devuelve error si encuentra leaks (útil en CI).
- `--config .gitleaks.toml`: usa una configuración personalizada con reglas propias.
- `--gitleaks-ignore-path .`: respeta el archivo `.gitleaksignore` para falsos positivos.
- `--redact`: oculta los secretos en la salida (útil en logs públicos).

También puedes escanear directorios sueltos con `gitleaks dir` o pipear contenido con `gitleaks stdin`.

## ¿Cuándo usarlo?

- **Antes de hacer público un repo**: escanea el historial completo para asegurarte de que no hay claves coladas.
- **En CI/CD**: añádelo como paso en GitHub Actions para que falle el build si alguien commitea un secreto.
- **Auditorías de seguridad**: ideal para revisar repos viejos que han pasado por muchas manos.

## Pre-commit hook

La forma más efectiva de usarlo es como [hook de pre-commit](https://github.com/BadLiveware/pi/blob/main/.githooks/pre-commit) para que bloquee automáticamente cualquier commit que contenga secretos:

```bash
#!/usr/bin/env bash
set -euo pipefail

if [[ "${SKIP_GITLEAKS:-}" == "1" || "${SKIP_GITLEAKS:-}" == "true" ]]; then
  echo "Skipping gitleaks pre-commit scan because SKIP_GITLEAKS=${SKIP_GITLEAKS}." >&2
  exit 0
fi

if ! command -v gitleaks >/dev/null 2>&1; then
  cat >&2 <<'EOF'
gitleaks is required by this repository's pre-commit hook but was not found.
Install gitleaks, or set SKIP_GITLEAKS=1 for an intentional one-off bypass.
EOF
  exit 1
fi

echo "Running gitleaks on staged changes..." >&2
gitleaks protect --staged --source . --redact --no-banner
```

Guarda esto en `.githooks/pre-commit`, hazlo ejecutable (`chmod +x`) y configura git para que use esa carpeta:

```bash
git config core.hooksPath .githooks
```

A partir de ahí, cada `git commit` escaneará los cambios en busca de secretos. Si necesitas saltártelo puntualmente, `SKIP_GITLEAKS=1 git commit`.

Es de esas herramientas que no necesitas hasta que la necesitas. Y cuando la necesitas, te alegras de tenerla a un `gah install` de distancia.
