Date: 2010-01-04 14:31
Category: Sin Categoría
Guid: http://www.pablocaro.es/?p=217
Title: Descargar código de un repositorio publicado con gitweb

Quería probar un software disponible en la red ([Perfect Sale](http://www
.perfect-sale.com/)). Sabía que tenía que usar _git clone_ pero no la url.

No queda claro (al menos a mí) [en el repositorio
gitweb](http://git.hforge.org/?p=shop.git;a=tree) la url a usar.

Al fin, encontré la solución en [un repositorio mejor
documentado](http://gitweb.codeendeavor.com/) (gracias).

El protocolo es git y la url no incluye ese "projects" que vemos en el rastro
de migas. Lo anoto para no volver a perder el tiempo otra vez.

Así que para el proyecto citado la orden queda así:

    
    
    
    $ git clone git://git.hforge.org/shop.git
    

