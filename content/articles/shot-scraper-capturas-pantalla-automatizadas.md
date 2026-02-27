Title: Shot-scraper: Capturas de pantalla automatizadas para la web
Slug: shot-scraper-capturas-pantalla-automatizadas
Date: 2026-02-20
Tags: python, cli, tools, web, scraping, screenshots
Category: Python
Lang: es

¿Alguna vez has necesitado tomar capturas de pantalla de una página web de forma programática? Tal vez para documentar tu proyecto, monitorizar cambios en una UI, o generar imágenes para redes sociales. Existen muchas formas de hacerlo, pero **[shot-scraper](https://shot-scraper.datasette.io/)** destaca por su facilidad de uso y potencia.

Creada por Simon Willison, `shot-scraper` es una herramienta de línea de comandos (CLI) que envuelve Playwright para hacer que tomar screenshots sea trivial.

## Instalación

Al igual que con otras herramientas modernas de Python, la mejor forma de instalarla es usando `uv`:```bash
uv tool install shot-scraper
```

Una vez instalada, necesitarás descargar el navegador que utiliza por debajo (Chromium):

```bash
shot-scraper install
```

## Uso básico

La forma más sencilla de usarlo es darle una URL y un nombre de archivo:

```bash
shot-scraper https://pablocaro.es/ blog.png
```

Esto generará una imagen llamada `blog.png` con la captura de la página.

### Capturando selectores específicos

Una de las características más potentes es la capacidad de capturar solo un elemento específico de la página usando selectores CSS:

```bash
shot-scraper https://github.com/pcaro -s ".js-calendar-graph" calendar.png
```

Este comando capturará únicamente el gráfico de contribuciones de GitHub.

### Interactuando con JavaScript

A veces necesitas ejecutar algo de código antes de tomar la foto. Por ejemplo, para ocultar un banner de cookies o esperar a que cargue algo.

```bash
shot-scraper https://pablocaro.es/ \
  --javascript "document.querySelector('header').style.display = 'none';" \
  -o sin-header.png
```

## Automatización avanzada

Si necesitas tomar muchas capturas, puedes definir un archivo YAML de configuración:

```yaml
# shots.yml
- url: https://pablocaro.es/
  output: home.png
  height: 800
- url: https://pablocaro.es/archives.html
  output: archives.png
  wait: 1000  # Esperar 1 segundo
```

Y ejecutarlas todas de una vez:

```bash
shot-scraper multi shots.yml
```

## Más allá de las capturas

`shot-scraper` también incluye utilidades para:

*   **Accesibilidad**: Volcar el árbol de accesibilidad de una página (`shot-scraper accessibility`).
*   **PDF**: Generar PDFs de páginas web (`shot-scraper pdf`).
*   **HAR**: Grabar archivos HAR para analizar el tráfico de red (`shot-scraper har`).

Es una de esas herramientas que, una vez instaladas, encuentras usos para ella constantemente. Perfecta para integrar en pipelines de CI/CD para generar visuales de documentación automáticamente.

Más info en la [documentación oficial](https://shot-scraper.datasette.io/).

![shot-scraper help]({static}/images/shot_scraper_help.png)
