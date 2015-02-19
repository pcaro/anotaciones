Date: 2010-07-25 05:33
Guid: http://www.pablocaro.es/?p=250
Title: Zope y noatime

Una fácil mejora para el rendimiento de un zope con problemas de acceso a
disco es[ no actualizar la fecha de último acceso](http://tldp.org/LDP/solrhe
/Securing-Optimizing-Linux-RH-Edition-v1.3/chap6sec73.html) al fichero de la
base de datos Data.fs:

    
    
    chattr -R +A Data.fs
    

Simple y efectivo.

