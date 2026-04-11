Title: rbw sync: missing field `access_token`
Date: 2026-04-11 19:30
Category: Linux
Tags: bitwarden, cli, bug, linux
Slug: rbw-sync-access-token
Lang: es
Summary: Error conocido de rbw al sincronizar con Bitwarden o Vaultwarden: "failed to parse JSON: missing field access_token". La solución es limpiar el caché local.
featured_image: /images/rbw-sync-access-token.png

Hoy me he encontrado con este error al intentar sincronizar mi vault de Bitwarden con **rbw**:

```bash
$ rbw sync
rbw sync: failed to sync database from server: failed to parse JSON: missing field access_token at line 1 column 393
```

![Issue #202 en el repo de rbw]({static}/images/rbw-sync-access-token.png)

## Diagnóstico

Es un bug conocido de rbw que existe desde 2020 ([#32](https://github.com/doy/rbw/issues/32)) y sigue abierto. Ocurre tanto con Bitwarden oficial como con Vaultwarden. No es un problema de la versión de Vaultwarden.

**Causa:** rbw guarda un token de sesión localmente que se corrompe o expira, y al intentar sincronizar, el servidor devuelve una respuesta JSON sin el campo `access_token` que rbw espera. El caché local de rbw queda en un estado inválido.

## Solución

```bash
rbw purge
rbw sync
```

`rbw purge` limpia el caché local de la vault. Después, `rbw sync` te pedirá la master password y volverá a descargar todo desde cero.

## Contexto del bug

- Abierto desde diciembre de 2020 ([#32](https://github.com/doy/rbw/issues/32)), 19 👍, sin fix
- Reabierto en agosto 2024 ([#202](https://github.com/doy/rbw/issues/202)) con la misma sintomatía
- El maintainer (doy) no ha podido reproducirlo → sigue sin arreglarse
- Aparece con más frecuencia tras añadir entradas nuevas (TOTP, SSH keys) desde otro cliente (browser extension, web vault) y luego intentar sync desde rbw

**TL;DR:** `rbw purge && rbw sync` y debería funcionar.
