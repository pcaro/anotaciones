Date: 2009-06-16 10:31
Guid: http://www.pablocaro.es/?p=94
Title: Un servidor web de bolsillo gracias a python

Otra cosita para recordar. La forma más simple de servir unos ficheros vía
web:

    
    
    python -m SimpleHTTPServer 8080

Nota: Antes usaba:

    
    
    python -c "import SimpleHTTPServer;SimpleHTTPServer.test()"

Pero no permite indicar el puerto y es más tedioso de escribir.

