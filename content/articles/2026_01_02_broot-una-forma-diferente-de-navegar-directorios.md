---
Title: broot, una forma diferente de navegar por tus directorios
Date: 2026-01-02 10:00
Tags: terminal, cli, broot, rust, herramientas
Lang: es
Category: Herramientas
Slug: broot-una-forma-diferente-de-navegar-directorios
Summary: broot es una herramienta para la terminal que te permite explorar tus directorios de una forma interactiva y mucho más potente que los comandos tradicionales como ls o tree.
Status: draft
---

¡Hola! ¿Qué tal? Hoy te quiero contar sobre una herramienta que me ha volado la cabeza para moverme por los directorios de mi ordenador: se llama **broot**. Si eres de los que se lía con el `ls` o el `cd` y siempre acabas perdido, esto te va a encantar.

### broot, una forma diferente de navegar por tus directorios

Imagina que tienes un montón de carpetas y archivos, y quieres encontrar algo rápido o simplemente entender qué hay por ahí. Con los comandos de siempre, a veces es un rollo, ¿verdad? Pues broot viene a solucionar eso de una manera súper visual y eficiente.

**¿Qué es broot?**

En pocas palabras, broot es una herramienta para la terminal que te permite explorar tus directorios de una forma interactiva y mucho más potente que los comandos tradicionales como `ls` o `tree`. Es como tener un explorador de archivos gráfico, pero directamente en tu terminal.

**¿Para qué sirve? Sus características principales:**

*   **Visión general al instante:** Te da una vista de árbol de tus directorios, incluso si son enormes, pero de forma inteligente. No te abruma con miles de líneas, sino que oculta lo que no es relevante (como los archivos ignorados por Git) para que te centres en lo importante. ¡Pero si quieres verlos, también puedes!
*   **Navegación rápida:** ¿Recuerdas ese directorio que no sabes dónde metiste? Con broot, solo tienes que escribir unas pocas letras de lo que buscas, y él te lo encuentra. Puedes moverte entre los resultados, subir y bajar por la jerarquía, y cuando encuentres el lugar, un `alt + enter` te lleva directamente a ese directorio en tu terminal. ¡Adiós a los `cd ../../cosas/mas_cosas`!
*   **No te pierdes en la búsqueda:** A diferencia de otros buscadores, broot siempre te muestra dónde está el archivo o directorio que buscas dentro de la estructura de carpetas. Así, nunca pierdes el contexto. Puedes buscar por nombre, por contenido del archivo, ¡e incluso usar expresiones regulares!
*   **Manipulación de archivos sin ciegas:** ¿Necesitas mover, copiar, borrar o crear un directorio? Con broot, puedes hacerlo viendo la estructura de archivos en todo momento. Es mucho más seguro y visual que hacerlo "a ciegas" con `mv` o `cp`.
*   **Paneles para trabajar mejor:** Una de las cosas más chulas es que puedes abrir varios paneles. Imagina que quieres copiar algo de una carpeta a otra: abres un panel con el origen, otro con el destino, y arrastras (bueno, no arrastras, pero casi) los archivos entre ellos. ¡Ideal para organizar!
*   **Previsualización de archivos:** Si seleccionas un archivo, puedes previsualizar su contenido directamente en un panel lateral. ¡Incluso imágenes si tu terminal lo soporta!
*   **Ejecuta comandos sobre archivos:** Encuentras un archivo que quieres editar, escribes `:e` y `enter`, y broot lo abre con tu editor favorito. Puedes configurar tus propios "verbos" (comandos) para hacer lo que quieras con los archivos seleccionados.
*   **Reemplaza a `ls` con esteroides:** Si quieres ver tamaños, fechas, permisos, etc., broot te lo muestra de forma clara y ordenada. Además, puedes ordenar por tamaño o fecha para ver qué está ocupando más espacio o qué has modificado recientemente.
*   **Control de Git:** Si trabajas con Git, broot te muestra el estado de tus archivos (modificados, nuevos, etc.), la rama actual y estadísticas de cambios. ¡Incluso puedes ver solo los archivos que `git status` te mostraría!

En resumen, broot es una navaja suiza para la terminal que te hace la vida mucho más fácil a la hora de interactuar con tus archivos y directorios. Si pasas mucho tiempo en la terminal, te recomiendo que le eches un vistazo. ¡Te va a encantar!
