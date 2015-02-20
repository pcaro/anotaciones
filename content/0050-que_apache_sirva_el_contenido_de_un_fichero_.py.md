Date: 2009-10-13 05:36
Category: Sin Categoría
Guid: http://www.pablocaro.es/?p=161
Title: Que apache sirva el contenido de un fichero .py

Para que el servidor apache de [webfaction](http://www.webfaction.com/) no
intentara ejecutar los scripts python que dejo para la descarga en este blog,
me creé un fichero
_[.htaccess_](http://httpd.apache.org/docs/1.3/howto/htaccess.html) y dentro:

    
    
    
    removeHandler cgi-script .pl .py .cgi
    

