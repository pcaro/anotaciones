Date: 2010-02-22 10:09
Category: Sin Categoría
Guid: http://www.pablocaro.es/?p=228
Title: Descargar una web para visualización local con wget

El comando es

    
    
    $ wget -E -H -k -K -p  http://www.google.es

Con _-p_ hacemos que se descarguen los enlaces requeridos (css, javascript),
con _-k_ convertimos los enlaces dentro del html para visualización local
(_-K_ copia de seguriad) y con _-E_ aseguramos que los ficheros descargados
tengan extensión html para la visualización en local.

