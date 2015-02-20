Date: 2010-04-28 03:33
Category: Programación
Guid: http://www.pablocaro.es/?p=237
Tags: web
Title: Completar mientras se depura en zope

Siempre tengo que buscar esto en google, para esto tengo el blog:

    
    
    
    $ bin/instance debug
    
    
    
    
    >>> import readline, rlcompleter
    >>> readline.parse_and_bind('tab: complete')
    >>> app.
    Display all 760 possibilities? (y or n)
    >>> 
    

