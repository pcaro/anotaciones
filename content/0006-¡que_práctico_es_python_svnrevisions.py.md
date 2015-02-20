Date: 2007-04-10 09:55
Guid: http://www.pablocaro.es/?p=10
Tags: 
Categories: Python
Title: ¡Que práctico es python!: svnrevisions.py

Pongo a continuación un script rápido que hice hace ya un tiempo. En ese
momento estaba realizando un backport de código y de forma sucia realicé
varios

    
    
    svn up -rTAL

De esa forma y con unos pequeños cambios obtuve el cambio que necesitaba. Pero
después de un rato no recordaba que fichero cambié exactamente y a qué
revisiones. Un poquito de [terminal](http://ipython.scipy.org/moin/About) y
listo. Se que es sucio, que podría usar las librerías de python para
subversion, etc. Pero se hizo de forma rápida y funciona. El funcionamiento se
puede ver en el código fuente, pero pongo una ayudita:

    
    
    $ python svnrevisions.py
    $ python svnrevisions.py 123
    $ python svnrevisions.py ALL
    

Aquí dejo el código: [svnrevisions](http://www.pablocaro.es/wp-
content/uploads/2009/07/svnrevisions)

