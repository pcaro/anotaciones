Date: 2010-07-08 05:56
Guid: http://www.pablocaro.es/?p=241
Tags: 
Categories: Linux
Title: Opciones típicas rsync

Para usar un rsync como un scp (pero con las ventajas de rsync como que puedo
parar y continuar después):

    
    
    rsync -azPrv -e 'ssh' usuario@host:/path/to/folder /path/to/destination

