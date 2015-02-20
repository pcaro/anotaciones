Date: 2011-03-04 03:49
Category: Programación
Guid: http://www.pablocaro.es/?p=278
Tags: linux, zope
Title: scp con compresión

La mejor forma de descargar una zodb:

    
    
    scp -C -o CompressionLevel=9 user@yoursite.com:~/plonefolder/zinstance/var/filestorage/Data.fs .

Leído en: <http://blog.mfabrik.com/2011/03/02/scp-file-copy-with-on-line-
compression/>

