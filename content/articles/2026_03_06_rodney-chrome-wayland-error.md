Title: Solución al Error de Rodney con Chrome en Wayland
Date: 2026-03-06 09:00
Tags: rodney, chrome, wayland, linux, debugging
Lang: es
Category: Problemas
Slug: rodney-chrome-wayland-error
Summary: Cómo resolver el crash de Rodney al iniciar Chrome en sistemas Wayland usando el Chrome del sistema.

[Rodney](https://github.com/simonw/rodney/) es una herramienta CLI creada por Simon Willison diseñada específicamente para que agentes de IA puedan controlar una instancia de Chrome mediante el Chrome DevTools Protocol. Es similar a `agent-browser` de Vercel, pero usando CDP en lugar de Playwright.

## El Problema

Al ejecutar `uvx rodney open https://google.es` sin iniciar primero Rodney con `rodney start`, el proceso falla porque:

1. Rodney intenta iniciar Chrome con el Chromium que descarga automáticamente en `~/.cache/rod/browser/`
2. Ese Chromium (v128.0.6568.0) tiene un bug conocido con el backend Ozone en sistemas Wayland
3. El crash ocurre debido a la combinación de flags `--single-process` + `--ozone-platform=headless`
4. El error en los logs indica: `gl_factory_ozone.cc(62): "Expected Mock or Stub, actual:0"`

## La Solución

La forma más sencilla de solucionar este problema es configurar Rodney para que use el Chrome de tu sistema en lugar del Chromium descargado automáticamente. Esto se hace mediante la variable de entorno `ROD_CHROME_BIN`:

```bash
# Añadir a ~/.bashrc o ~/.zshrc
echo 'export ROD_CHROME_BIN=/usr/bin/google-chrome' >> ~/.bashrc
source ~/.bashrc
```

Después de configurar esto, Rodney funcionará correctamente:

```bash
uvx rodney start
uvx rodney open https://google.es
```

## Ejemplo de funcionamiento

Una vez configurado, el flujo de trabajo es:

```bash
~/src/anotaciones [cv|…2] 
09:39 $ uvx rodney start
Chrome started (PID 2981885)
Debug URL: ws://127.0.0.1:34373/devtools/browser/319c905a-83a2-47d9-a6e0-8e6a4f2ff830
~/src/anotaciones [cv|…2] 
09:39 $ uvx rodney open https://google.es
Google
~/src/anotaciones [cv|…2] 
09:39 $ uvx rodney screenshot
screenshot.png
~/src/anotaciones [cv|…3] 
```

![Ejemplo de Rodney funcionando]({static}/images/rodney_example.png)

## ¿Por qué pasa esto?

El Chromium que Rodney descarga automáticamente tiene un bug conocido con el backend Ozone en sistemas Linux que usan Wayland (la alternativa a X11). Cuando se usan ciertas combinaciones de flags de Chrome, el proceso falla porque el sistema gráfico no está configurado como "Mock" o "Stub" (que es lo que esperan las pruebas).

Usar el Chrome del sistema evita este problema porque:
- El Chrome del sistema está compilado con soporte completo para Wayland
- Generalmente es una versión más estable y actualizada
- No tiene los mismos flags de desarrollo que causan conflictos

## Enlace

- [Repositorio de Rodney en GitHub](https://github.com/simonw/rodney/)
