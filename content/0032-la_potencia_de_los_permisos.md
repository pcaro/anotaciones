Date: 2008-12-01 14:06
Category: Sistemas
Guid: http://www.pablocaro.es/?p=43
Tags: linux
Title: La potencia de los permisos

Recordar los comandos para controlar las listas de control de acceso en linux.
`man setfacl man getfacl` Tras "setfacl -m user:joe:rwx dir", verás que ls -d
dir muestra un signo + al final que indica que se están utilizado permisos
ampliados. Si quieres saber más, el tío google te lo dirá.

