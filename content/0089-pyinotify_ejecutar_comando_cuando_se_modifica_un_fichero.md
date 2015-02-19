Date: 2013-04-03 05:09
Guid: http://www.pablocaro.es/?p=379
Title: pyinotify: Ejecutar comando cuando se modifica un fichero

Ya he comentado por aquí un comando _when-changed_. Ahora anoto otra
alternativa, esta vez python. Se trata de pyinotify. Yo lo uso para generar la
documentación de sphinx mientras estoy escribiendo:

    
    
    python -m pyinotify -r -c "make html" -e IN_MODIFY source
    

