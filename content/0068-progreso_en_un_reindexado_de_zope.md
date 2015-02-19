Date: 2010-09-18 06:06
Guid: http://www.pablocaro.es/?p=253
Title: Progreso en un reindexado de zope

Visto en el producto contentleadimage:

    
    
    from Products.ZCatalog.ProgressHandler import ZLogHandler
    ctool.reindexIndex(['hasContentLeadImage'], portal.REQUEST, pghandler=ZLogHandler())

Esto muestra un progreso en la consola si estás ejecutando en primer plano.

