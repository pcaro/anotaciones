Date: 2011-08-24 04:11
Guid: http://www.pablocaro.es/?p=299
Tags: 
Categories: Linux, Yaco
Title: virtualbox: Actualizar las Guest Additions en máquinas ubuntu

Si usas [vagrant](http://vagrantup.com/) para gestionar máquinas virtuales con
[virtualbox](http://www.virtualbox.org/), un buen lugar para obtener boxes es
[vagrantboxes](http://www.vagrantbox.es/). Pero a veces la versión que traen
de las Guest Additions no coincide con el virtualbox que tienes (en mi caso el
último). Vagrant se queja y puede ocasionar problemas. Lo más simple es
arrancar la máquina en modo gráfico (config.vm.boot_mode = :gui en vagrant) e
indicar en el menu de virtualbox en "Dispositivos" -> "CD/DVD" que se ponga
VBoxGuestAddions.iso. Luego vasta con montar el cdrom y ejecutar el comando de
instalación:

    
    
    $ sudo mount -t auto /dev/cdrom /mnt
    $ cd mnt
    $ sudo ./VBoxLinuxAdditions.run

Puede que tengas de instalar dkms. Si el sistema no tiene sistema gráfico
instalado (como en este caso), se quejará pero quedará instalado todo bien.

