Botón central en firefox
########################

:date: 2016-01-01 07:00
:tags: linux
:lang: es
:category: Sistemas
:slug: boton_central_firefox
:summary: Que firefox deje de abrir la url pegada con el botón central del ratón

Otra nota recordatoria.
Habitualmente abro los enlaces en nueva ventana en firefox usando el botón central.
Me ocurre a menudo que tengo una url en el clipboard y firefox entonces me la abre en lugar del enlace.
Para evitarlo, simplemente  :code:`about:config` y establecer la propiedad :code:`middlemouse.contentLoadURL` a false.