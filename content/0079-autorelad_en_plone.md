Date: 2012-07-27 04:38
Guid: http://www.pablocaro.es/?p=319
Title: Autorelad en plone

Otro recordatorio. Para recargar mientras desarrollo una browserview en plone:

    
    
    $ when-changed.py *.py -c wget -q -O /dev/null  \
    http://admin:admin@localhost:8080/@@reload?action=code

Basta pues con usar [when-changed](https://github.com/joh/when-changed) y
[plone.reload](http://pypi.python.org/pypi/plone.reload/) Se que existen
extensiones  para el navegador  que recargan una  pestaña cuando cambia un
fichero, pero yo soy más de consola.

