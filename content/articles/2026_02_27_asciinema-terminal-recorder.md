Title: Graba y Comparte tus Sesiones de Terminal con asciinema
Date: 2026-02-27 12:00
Tags: asciinema, terminal, linux, productivity
Lang: es
Category: Herramientas
Slug: asciinema-terminal-recorder
Summary: Descubre asciinema, la herramienta perfecta para grabar tus sesiones de terminal de forma ligera, reproducible y fácil de compartir.
Featured-Image: /images/asciinema_help.png

A menudo necesitamos compartir lo que sucede en nuestra terminal, ya sea para un tutorial, demostrar un error o simplemente documentar un proceso. Aunque existen herramientas para grabar vídeo tradicional, **asciinema** ofrece una alternativa mucho más potente y ligera.

## ¿Qué es asciinema?

[asciinema](https://github.com/asciinema/asciinema) no graba vídeo en el sentido tradicional (píxeles). En su lugar, captura el flujo de texto de la terminal junto con los tiempos exactos. Esto tiene varias ventajas:

- **Archivos diminutos**: En lugar de megabytes de vídeo, obtienes archivos de texto muy pequeños.
- **Texto seleccionable**: Al reproducir una sesión en la web, puedes copiar y pegar el código directamente.
- **Calidad perfecta**: No hay pérdida de resolución ni artefactos de compresión.

## Instalación y Ayuda

Ya tengo `asciinema` instalado en mi sistema. Aquí puedes ver el resumen de comandos disponibles:## Ejemplo interactivo

A continuación puedes ver una pequeña demostración de `asciinema` en acción, ejecutando el comando `cowsay Muuuuu`:

<link rel="stylesheet" type="text/css" href="/theme/asciinema-player/asciinema-player.css" />
<div id="demo-player"></div>
<script src="/theme/asciinema-player/asciinema-player.js"></script>
<script>
    window.addEventListener('load', function() {
        AsciinemaPlayer.create('/images/demo.cast', document.getElementById('demo-player'), {
            cols: 80,
            rows: 10,
            autoPlay: true,
            loop: true
        });
    });
</script>

## Comandos básicos

Para empezar a grabar, simplemente ejecuta:

```bash
asciinema rec demo.cast
```

Esto comenzará a grabar todo lo que ocurra en tu sesión actual de terminal. Cuando termines, simplemente presiona `Ctrl-D` o escribe `exit`. El resultado se guardará en el archivo `demo.cast`.

Para reproducirlo localmente:

```bash
asciinema play demo.cast
```

Y si quieres compartirlo con el mundo, puedes subirlo a su servicio de alojamiento gratuito:

```bash
asciinema upload demo.cast
```

## ¿Por qué usarlo?

Es ideal para desarrolladores que escriben blogs técnicos (como este), ya que permite insertar las grabaciones directamente en el navegador con un reproductor ligero basado en JavaScript. ¡Adiós a los GIFs borrosos de 20MB!

![asciinema help]({static}/images/asciinema_help.png)
