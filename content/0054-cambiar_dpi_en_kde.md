Date: 2009-12-04 05:35
Category: Sistemas
Guid: http://www.pablocaro.es/?p=196
Tags: linux
Title: Cambiar dpi en kde

Siempre que reinstalo me encuentro con el mismo problema. No tengo el dpi
estándar de 96, sino uno extraño de 113.

    
    
    pcaro@davinci$ xdpyinfo | grep resolutio
      resolution:    113x113 dots per inch

Como resultado, muchas páginas webs no se visualizan correctamente. Para
solucionarlo tengo que decirle al servidor X que arranque con un dpi
predeterminado. Eso lo hago en los ficheros de configuración de kdm que es el
encargado de ejecutar el servidor. Concretamente en _/etc/kde4/kdm/kdmrc_.
Basta con indicar al servidor X qué valor de dpi usar. Para ello usamos la
opción _-dpi_.

    
    
    # This string is subject to word splitting.
    # Default is ""
    ServerArgsLocal=-br -nolisten tcp -dpi 96

Eso es todo. Reiniciar las X y listo. PD: No se el motivo pero el nuevo dpi y
mi tarjeta gráfica intel integrada, yo tengo mucho mejor rendimiento en la
aceleración gráfica.

