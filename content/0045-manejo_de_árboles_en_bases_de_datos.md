Date: 2009-07-07 16:59
Category: Sin Categoría
Guid: http://www.pablocaro.es/?p=68
Title: Manejo de árboles en bases de datos

Hay cuatro formas de guardar árboles en bases de datos relacionales:

  1. Adjacency List
  2. Materialized Paths
  3. Nested Sets o Modified Preorder Tree Traversal (MPTT)
  4. Nested intervals
Dejo unos enlaces:

  * [Trees in SQL: Nested Sets and Materialized Path](http://www.dbazine.com/oracle/or-articles/tropashko4) El articulo y el hombre de referencia
  * [Storing Hierarchical Data in a Database](http://www.sitepoint.com/article/hierarchical-data-database/) Todo muy clarito con muy buenos ejemplos
  * [Mysql: datos jerárquicos](http://http://dev.mysql.com/tech-resources/articles/hierarchical-data.html) Explicación clara y general
  * [ Materialized Path + Nested Sets ](http://www.ibstaff.net/fmartinez/?p=18) Una forma de mezclar estos dos metodos
Algunas implentacionaciones:

  * [sqlamp — Materialized Path for SQLAlchemy](http://sqlamp.angri.ru/)
  * [Django Treebeard](http://code.google.com/p/django-treebeard/) Adjacency List, Materialized Path y Nested Sets para django
  * [django-mptt](http://code.google.com/p/django-mptt/)

