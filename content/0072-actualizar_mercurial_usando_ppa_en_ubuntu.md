Date: 2011-02-25 05:12
Guid: http://www.pablocaro.es/?p=274
Tags: 
Categories: Programación, Linux, Yaco
Title: Actualizar Mercurial usando ppa en ubuntu

Existen tres PPA para mercurial: <https://launchpad.net/~mercurial-
ppa/+archive/releases> (última release, actualmente 1.7.5-0ppa1~maverick1)
<https://launchpad.net/~mercurial-ppa/+archive/stable-snapshots> (snapshots de
la rama estable, actualmente ﻿1.7.5+2-5fc7c84ed9b0-0ppa1~maverick1)
<https://launchpad.net/~mercurial-ppa/+archive/snapshots> (snapshots de lo
último, actualmente 1.8~1.7.5+4-8f5c865b7b4a-0ppa1~maverick1) Como decía en la
última anotación para añadir el PPA basta con:

    
    
    $ sudo add-apt-repository ppa:mercurial-ppa/stable-snapshots
    $ sudo aptitude update
    $ sudo aptitude  install Mercurial



