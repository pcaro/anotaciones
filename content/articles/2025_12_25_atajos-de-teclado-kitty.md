---
title: Atajos de teclado esenciales en Kitty: Dominando tu terminal
date: 2025-12-25 12:15
tags: kitty, terminal, atajos, teclado, productividad
lang: es
category: Sistemas
slug: atajos-de-teclado-kitty
summary: Una guía rápida a los atajos de teclado más útiles de Kitty para optimizar tu flujo de trabajo en la línea de comandos.
---

**Kitty** es un terminal que brilla por su rendimiento y su gran capacidad de personalización, pero donde realmente se potencia es en su interfaz controlada por teclado. Dominar sus atajos te permitirá navegar, gestionar y manipular tus sesiones de terminal con una eficiencia asombrosa.

## Descubre tus atajos: `show_shortcuts`

La forma más rápida de conocer todos los atajos de teclado configurados en tu instancia de Kitty es usando su propia funcionalidad:

```bash
kitty +kitten show_shortcuts
```

Esto abrirá una ventana interactiva donde podrás ver todos los atajos, tanto los predeterminados como los personalizados en tu `kitty.conf`.

## Atajos Esenciales para el Día a Día

Aquí te presento algunos de los atajos más útiles y que más te ayudarán a optimizar tu flujo de trabajo:

### Gestión de Ventanas y Splits (Paneles)

*   `ctrl+shift+enter`: Abre una nueva ventana de Kitty.
*   `ctrl+shift+w`: Cierra la ventana actual de Kitty.
*   `ctrl+shift+o`: Divide la ventana actual verticalmente (nuevo panel a la derecha).
*   `ctrl+shift+e`: Divide la ventana actual horizontalmente (nuevo panel abajo).
*   `ctrl+shift+f`: Alterna entre paneles divididos (focus).
*   `ctrl+shift+[` / `ctrl+shift+]`: Navega entre paneles (izquierda/derecha).
*   `ctrl+shift+alt+[` / `ctrl+shift+alt+]`: Mueve el panel activo (izquierda/derecha).

### Gestión de Pestañas

*   `ctrl+shift+t`: Abre una nueva pestaña.
*   `ctrl+shift+q`: Cierra la pestaña actual.
*   `ctrl+shift+.`: Mueve a la siguiente pestaña.
*   `ctrl+shift+,`: Mueve a la pestaña anterior.
*   `ctrl+shift+alt+.`: Mueve la pestaña actual a la derecha.
*   `ctrl+shift+alt+,`: Mueve la pestaña actual a la izquierda.

### Copiar y Pegar

Kitty tiene su propia implementación de copiar/pegar, que puede ser más fiable que la del sistema cuando trabajas en entornos remotos o con multiplexores:

*   `ctrl+shift+c`: Copia el texto seleccionado al portapapeles del sistema.
*   `ctrl+shift+v`: Pega el texto del portapapeles del sistema.

### Control de Fuentes y Apariencia

*   `ctrl+shift+=` (o `+`): Aumenta el tamaño de la fuente.
*   `ctrl+shift+-`: Disminuye el tamaño de la fuente.
*   `ctrl+shift+backspace`: Restablece el tamaño de la fuente al valor predeterminado.
*   `ctrl+shift+k`: Entra en modo "scrollback" (para buscar o seleccionar texto histórico).

## Personalizando tus Atajos en `kitty.conf`

Puedes añadir o modificar atajos de teclado en tu archivo de configuración `~/.config/kitty/kitty.conf` usando la directiva `map`. Por ejemplo, para mapear `F1` para un script personalizado:

```
map f1 launch --type=overlay bash -c "my_custom_script.sh"
```

Dominar estos atajos transformará tu interacción con la terminal, haciéndola más fluida e intuitiva. ¡Experimenta y personaliza Kitty para que se adapte perfectamente a tu estilo de trabajo!
