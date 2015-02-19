Date: 2009-12-16 10:18
Guid: http://www.pablocaro.es/?p=207
Title: Parcheando, parcheando ...

Siempre tengo que buscar cómo usar patch. Como tengo un blog que se llama
anotaciones pues apunto:

    
    
    $ patch -p1 < baz.diff

Donde el número 1 viene de mirar en el fichero .diff y contar las barras "/"
que hay antes que el directorio donde estoy. Por ejemplo si veo
_/users/stephen/package/src/net/http.c_ y estoy en un directorio que contiene
_net/http.c_ pues es 5 (ojo, hay que contar la primera). Para referencia [The
Ten Minute Guide to diff and
patch](http://stephenjungels.com/jungels.net/articles/diff-patch-ten-
minutes.html)

