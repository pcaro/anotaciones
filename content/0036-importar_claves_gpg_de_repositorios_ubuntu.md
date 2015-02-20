Date: 2009-02-01 13:00
Guid: http://www.pablocaro.es/?p=51
Tags: 
Categories: Linux
Title: Importar claves gpg de repositorios ubuntu

Ante un error como este: W: GPG error: http://ppa.launchpad.net intrepid
Release: The following signatures couldn't be verified because the public key
is not available: NO_PUBKEY 3B81A3FBA47394CE Hay que importar las claves:

    
    
    gpg --keyserver keyserver.ubuntu.com --recv 3B81A3FBA47394CE
    gpg --export --armor 3B81A3FBA47394CE | sudo apt-key add -
    
    _UPDATE:_
    _Corregido el tema de los guiones, gracias a miguelbf por la indicación y perdón por la tardanza en arreglarlo_

