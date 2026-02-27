Title: Renderizando Markdown en la terminal con Glow
Date: 2026-02-20
Tags: cli, markdown, herramientas, linux, kitty
Category: Linux
Slug: renderizando-markdown-en-la-terminal-con-glow
Lang: es
Summary: Descubre Glow, una herramienta para renderizar Markdown directamente en la terminal, ideal para leer documentación y READMEs.

[Glow](https://github.com/charmbracelet/glow) es un renderizador de Markdown para la línea de comandos. Permite leer archivos Markdown locales o remotos, y renderizarlos con resaltado de sintaxis y estilos, directamente en tu terminal.

Esta herramienta me resulta especialmente útil ahora que paso más tiempo usando la terminal con [Kitty]({filename}2025_12_25_de-yakuake-a-kitty.md), ya que me permite consultar documentación y READMEs sin tener que abrir un navegador o un editor gráfico.

## Instalación

Para instalar Glow, utilizaremos [gah]({filename}2026_02_11_gestionando-instalaciones-desde-github-con-gah.rst), una herramienta que facilita la instalación de binarios desde GitHub Releases.```bash
gah install charmbracelet/glow
```

El proceso de instalación es muy sencillo:

```text
$ gah install charmbracelet/glow
Fetching release info for: charmbracelet/glow [latest]
Found release: v2.1.1
Downloading: glow_2.1.1_Linux_x86_64.tar.gz
############################################################################################################################################################################### 100.0%
GitHub Release did not provide digest for glow_2.1.1_Linux_x86_64.tar.gz. Skipping verification.
Extracting: glow_2.1.1_Linux_x86_64.tar.gz
Installing: glow
Give a new name or keep 'glow'? (Leave empty to keep the same)
New name: 
Installed: glow
Done!
```

Una vez instalado, simplemente ejecuta `glow` seguido del archivo que quieras visualizar, o incluso la URL de un README en GitHub.

![glow help]({static}/images/glow_help.png)
