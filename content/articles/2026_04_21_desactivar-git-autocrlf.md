Title: Desactivar git autocrlf
Date: 2026-04-21 12:00
Category: Git
Tags: Git, Windows, WSL, Line Endings
Slug: desactivar-git-autocrlf
Lang: es
featured_image: /images/git-disable-autocrlf.png
Summary: Si usas Windows (o WSL), Git te está convirtiendo los saltos de línea en silencio. Un solo comando lo arregla.

No soy usuario habitual de Windows, pero si me viese obligado una temporada WSL sería para mí casi una obligación. No está de más tener esta nota a mano (por Ryan Harrison).

Si usas Windows, Git lleva años modificando tus saltos de línea sin que te des cuenta. El culpable es `core.autocrlf`, activado por defecto.

```bash
git config --global core.autocrlf false
```

## Qué hace `core.autocrlf`

Windows usa históricamente `CRLF` (`\r\n`) como salto de línea, mientras que Linux y macOS usan `LF` (`\n`). Con `autocrlf true` (el default en Windows):

- En **checkout**: Git convierte `LF` del repositorio a `CRLF` en tu working directory
- En **commit**: Git convierte `CRLF` de vuelta a `LF` antes de guardar

En teoría, tus ficheros locales quedan en formato Windows y el repositorio se mantiene limpio con `LF`. En la práctica, es fuente constante de problemas.

## Por qué es un mal default

**WSL lo agrava.** Tu entorno Linux espera `LF`, pero Git ha convertido todo a `CRLF`. Resultado: cada script y config file tiene un `\r` fantasma al final de cada línea, provocando fallos silenciosos. Y si no has visto el warning de marras, es que ya te has acostumbrado a ignorarlo:

```
warning: LF will be replaced by CRLF in some-file.sh.
The file will have its original line endings in your working directory
```

**Los editores modernos soportan LF sin problema.** El argumento original era que el Bloc de notas de Windows no podía manejar `LF` — algo que era cierto en 2003. Desde Windows 10 (2018) el Bloc de notas soporta `LF`. VS Code, Sublime, Vim, IntelliJ, Notepad++... todos lo manejan perfectamente desde hace años.

**La conversión es pérdida en la práctica.** Ficheros binarios se pueden corromper si Git los clasifica mal como texto. Y si en un equipo alguien tiene `autocrlf true` y otro `false`, aparecerán commits que son solo cambios de saltos de línea.

## La solución: desactívalo y usa `.gitattributes`

```bash
git config --global core.autocrlf false
```

A partir de ahí, Git deja tus saltos de línea tal cual — sin conversiones silenciosas. Para equipos, un fichero `.gitattributes` en el repositorio es un enfoque mucho mejor, porque aplica las mismas reglas para todos independientemente de su config local.

Usa `LF` en todas partes, configura tu editor para que guarde con `LF` por defecto, y no pienses más en ello.

*Fuente original*: [Git - Disable autocrlf (Ryan Harrison)](https://ryanharrison.co.uk/2026/04/21/git-disable-autocrlf.html)