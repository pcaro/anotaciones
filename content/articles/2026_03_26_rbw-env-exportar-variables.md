Title: rbw-env: Exportar variables de entorno desde Bitwarden
Date: 2026-03-26 20:55
Category: Herramientas
Tags: bitwarden, cli, environment, productivity, security
Slug: rbw-env
Lang: es
Summary: Cómo usar rbw para exportar variables de entorno desde Bitwarden, útil para establecer API keys de forma segura sin almacenarlas en el disco.
featured_image: /images/rbw-env-example.png

Siguiendo con la saga de [kitty-rbw]({filename}2026_02_26_kitty-rbw.md), hoy presento otro script del mismo proyecto: **rbw-env**.

![Selección de carpeta en rbw-env]({static}/images/rbw-env-example.png)

## El problema

Uso **pi-agent** con diferentes modelos de IA (Claude, OpenAI, Gemini...) y cada uno requiere su propia `API_KEY`. Mantener estas claves en el disco es un riesgo de seguridad, y tener que introducirlas cada vez es tedioso.

## La solución: rbw-env

El script permite exportar entradas de Bitwarden como variables de entorno. La idea es sencilla pero efectiva:

1. **Seleccionas una carpeta** con `fzf` (por ejemplo, "ai-providers")
2. **rbw-env exporta cada entrada** como `export VARIABLE='valor'`
3. **El archivo temporal se borra solo** después de hacer `source`

## Uso

```bash
# Seleccionar carpeta interactivamente
kitty @ kitten kitty_rbw/rbw_env.py

# O pasar la carpeta como argumento
kitty @ kitten kitty_rbw/rbw_env.py ai-providers
```

El comando crea un archivo temporal en `/tmp/kitty_rbw_env_*` y envía el comando `source` a la ventana:

```bash
source /tmp/kitty_rbw_env_qfdhyh_b
```

La última línea del archivo temporal es el borrado del propio archivo:

```bash
rm -f /tmp/kitty_rbw_env_qfdhyh_b
```

La idea es no hacer los export directamente en la terminal para que no se vean por pantalla (a veces grabo tutoriales por ejemplo)

## Estructura en Bitwarden

Cada entrada en la carpeta exportada usa:

- **Usuario**: nombre de la variable (ej: `ANTHROPIC_API_KEY`)
- **Contraseña**: valor de la variable (ej: `sk-ant-...`)
- **Nombre**: descripción opcional

Si alguna entrada tiene usuario o nombre igual a `NOEXPORT`, se ignora (útil para notas).

## Integración con kitty-rbw

En la [entrada anterior]({filename}2026_02_26_kitty-rbw.md) explico cómo instalar kitty-rbw. Con `Ctrl+Alt+Shift+b` tengo el selector de carpetas para exportar las variables de entorno.
