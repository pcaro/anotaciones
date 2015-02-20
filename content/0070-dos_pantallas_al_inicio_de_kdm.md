Date: 2011-02-01 02:32
Category: Sistemas
Guid: http://www.pablocaro.es/?p=268
Title: Dos pantallas al inicio de kdm

Para que ya el mismo kdm se ejecute con dos pantallas basta con poner la
configuración deseada (usando [xrandr](http://www.x.org/wiki/Projects/XRandR))
en el fichero ﻿**/etc/kde4/kdm/Xsetup**. Por ejemplo, en mi caso uso dos
pantallas en la oficina de modo que ese fichero contiene:

    
    
    INT="LVDS1"
    EXT="VGA1"
    xrandr -q | grep -q "$EXT connected"   && {
    xrandr --output $EXT --mode 1280x1024
    xrandr --output $INT --mode 1280x800
    xrandr --output $INT --bellow $EXT
    xrandr --output $INT --primary
    }

Estas lineas hacen que se consulte si tengo el segundo monitor conectado y en
se caso se configure de la forma deseada.

