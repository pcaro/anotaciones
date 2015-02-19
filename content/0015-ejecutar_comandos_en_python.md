Date: 2008-03-04 06:18
Guid: http://www.pablocaro.es/ejecutar-comandos-de-sistemas-en-python/
Title: Ejecutar comandos en python

Hago a menudo pequeños scripts en python. Y muchas de las veces necesito
ejecutar algún comando del sistema. Habitualmente importaba el módulo `os` y
llamaba a alguna de sus funciones (las popen). Pero en general no hace falta
importar os. Existe un módulo llamado `[commands`](http://docs.python.org/lib
/module-commands.html)` `(sólo para unix) que permite realizar esta tarea con
suma facilidad y mejor lectura del código. Dejar claro que para cosas más
avanzadas es mejor usar `[subprocess](http://docs.python.org/lib/module-
subprocess.html) ` que pretende reemplazarlo.

