Date: 2010-07-16 05:05
Guid: http://www.pablocaro.es/?p=247
Tags: 
Categories: Programación, Yaco, Sistemas
Title: Subversion: Añadiendo contenido a un directorio sin descargarlo

Caso práctico. Tengo un directorio _dev_ dentro del subversión con un montón
de código con sus correspondientes ramas de `trunk`, `branches`, `tags`, etc.
Quiero añadir un nuevo producto pero no descargar todo ese enorme directorio
_dev_:

    
    
    svn co --depth empty https://repositorio/dev dev
    cp loquesea nuevo_producto
    svn add loquesea
    svn ci

Gracias ctabasco por la anotación.

