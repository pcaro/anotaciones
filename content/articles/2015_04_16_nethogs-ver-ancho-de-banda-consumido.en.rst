NetHogs see consumed bandwidth
################################

:date: 2015-4-16 11:37
:tags: linux
:lang: en
:category: Systems
:slug: nethogs-ver-ancho-de-banda-consumido


To measure the bandwidth I am using right now, I use NetHogs

By default, it looks for a network interface called "eth0". If it doesn't find it, it complains like this::

	ioctl failed while establishing local IP for selected device eth0. You may specify the device on the command line.

You can see your network configuration with the *ip* command::

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


As you can see on my computer, I have two interfaces (apart from the loopback one) which are enp0s25 (my wired network card)
and the wifi wlp3s0, which I am connected to now and is the one I will use (I could list both).

So by running::

    $ sudo nethogs enp0s25


I can see the processes that are consuming the most bandwidth.

.. image:: images/nethogs.png
    :alt: Nethogs
    :align: center


The command help is::

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
