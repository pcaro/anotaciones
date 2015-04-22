NetHogs ver ancho de banda consumido
####################################

:date: 2015-4-16 11:37
:tags: linux
:lang: es
:category: Sistemas
:slug: nethogs-ver-ancho-de-banda-consumido


Para medir el ancho de banda que estoy utilizando en este momento utilizo NetHogs

Por defecto busca una interfaz de red llamada "eth0" si no la encuenta se queja así::

	ioctl failed while establishing local IP for selected device eth0. You may specify the device on the command line.

Puedes ver tu configuración de red con el comando *ip*::

    $ ip a
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host
           valid_lft forever preferred_lft forever
    2: wlp3s0: <BROADCAST,MULTICAST> mtu 1500 qdisc mq state DOWN group default qlen 1000
        link/ether 84:3a:4b:50:14:cc brd ff:ff:ff:ff:ff:ff
    3: enp0s25: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        link/ether 3c:97:0e:77:76:d3 brd ff:ff:ff:ff:ff:ff
        inet 192.168.1.39/24 brd 192.168.1.255 scope global dynamic enp0s25
           valid_lft 28955sec preferred_lft 28955sec
        inet6 fe80::3e97:eff:fe77:76d3/64 scope link
           valid_lft forever preferred_lft forever


Como podéis ver en mi equipo tengo dos interfaces (aparte de la de loopback) que son enp0s25 (mi tarjeta de red con cable)
y la wifi wlp3s0, en la que estoy conectado ahora que es la que voy a usar (podría listar las dos).

De forma que ejecutando::

    $ sudo nethogs enp0s25


Puedo ver los procesos que están consumiendo más ancho de banda.

.. image:: images/nethogs.png
    :alt: Nethogs
    :align: center


La ayuda del comando es::

    20:02 $ nethogs -h
    usage: nethogs [-V] [-b] [-d seconds] [-t] [-p] [device [device [device ...]]]
                    -V : prints version.
                    -d : delay for update refresh rate in seconds. default is 1.
                    -t : tracemode.
                    -b : bughunt mode - implies tracemode.
                    -p : sniff in promiscious mode (not recommended).
                    device : device(s) to monitor. default is eth0

    When nethogs is running, press:
     q: quit
     m: switch between total and kb/s mode
