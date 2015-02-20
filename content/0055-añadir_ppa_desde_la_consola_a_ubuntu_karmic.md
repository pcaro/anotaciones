Date: 2009-12-09 03:18
Guid: http://www.pablocaro.es/?p=200
Tags: 
Categories: Linux, Sistemas
Title: Añadir PPA desde la consola a ubuntu karmic

Para añadir un PPA a ubuntu karmic desde la consola basta con:

    
    
     sudo add-apt-repository ppa:kubuntu-ppa/ppa
    
    [sudo] password for pcaro:                                
    Executing: gpg --ignore-time-conflict --no-options --no-default-keyring --secret-keyring /etc/apt/secring.gpg --trustdb-name /etc/apt/trustdb.gpg --keyring /etc/apt/trusted.gpg --keyserver keyserver.ubuntu.com --recv E4DFEC907DEDA4B8A670E8042836CB0A8AC93F7A                                                                                  
    gpg: solicitando clave 8AC93F7A de hkp servidor keyserver.ubuntu.com                                             
    gpg: clave 8AC93F7A: clave pública "Launchpad Kubuntu Updates" importada                                         
    gpg: no se encuentran claves totalmente fiables                                                                  
    gpg: Cantidad total procesada: 1                                                                                 
    gpg:  
    

