Date: 2009-11-12 05:20
Guid: http://www.pablocaro.es/?p=181
Title: Añadiendo lenguaje procedural a base de datos postgres: createlang

Postgres 8.3 incluye 4 [lenguajes
procedurales](http://www.postgresql.org/docs/8.3/static/external-pl.html) en
la distribución y se pueden instalar más, pero hay que activarlos por base de
datos. Para ello, hay varios métodos (lo clásico es [create
language](http://www.postgresql.org/docs/8.3/static/sql-createlanguage.html))
pero los más cómodo es usar
[createlang](http://www.postgresql.org/docs/8.3/static/app-createlang.html).
Usa [droplang](http://www.postgresql.org/docs/8.3/static/app-droplang.html)
para eliminar el lenguaje.

