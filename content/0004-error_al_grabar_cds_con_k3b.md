Date: 2006-12-18 05:18
Guid: http://www.pablocaro.es/?p=7
Title: Error al grabar CDs con k3b

Tengo un Dell latitude D610 y kubuntu edgy. Desde dapper siempre me ha
ocurrido un error al copiar cds con k3b. El problema es que no tengo acceso al
dispositivo /dev/sg0 con <strike>sudo chown /dev/sg0 root:cdrom</strike> sudo
root:cdrom /dev/sg0 lo soluciono (doy grupo cdrom a quién quiera que use la
grabadora). El problema es que al reiniciar se vuelve a colocar el grupo a
root y no se como cambiar esto en el udev. ¿Alguna idea?

