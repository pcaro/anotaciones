Date: 2007-10-06 05:28
Category: Sistemas
Guid: http://www.pablocaro.es/?p=13
Tags: linux
Title: Knetworkmanager

Ahora una de esas entradas para que me sirva de recordatorio. Habitualmente
estoy acostumbrado, cuando voy a un lugar y me dan conexión wifi, a
configurarla a mano en /etc/network/interfaces. Esto hace que deje de
funcionar el knetwormanager. Indica "configuración manual de red". Para que
vuelva a tomar el control de las interaces de red tengo que comentar todas las
líneas en ese fichero como bien se indica [en la documentación de
ubuntu](https://help.ubuntu.com/community/WifiDocs/NetworkManager). Para
manejar el demonio NetWorkmanger tengo que usar: `
/etc/dbus-1/event.d/25NetworkManager {start|stop|restart|force-reload} `
`/etc/dbus-1/event.d/26NetworkManagerDispatcher {start|stop|restart|force-
reload}`

