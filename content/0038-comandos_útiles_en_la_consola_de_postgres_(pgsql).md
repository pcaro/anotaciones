Date: 2009-03-30 06:04
Guid: http://www.pablocaro.es/?p=55
Tags: 
Categories: Yaco
Title: Comandos útiles en la consola de postgres (pgsql)

Otra de las cosas que simpre olvido. Así que lo anoto. Para sacar el resultado
de una consulta sql a un fichero desde el pgsql.

  1. \a
  2. \f ,
  3. \o /tmp/salida.csv
  4. select * from ...
Se trata de:

  1. Cambiar entre modo de salida alineado y sin alinear
  2. Definir separador de campos (en el ejemplo a una coma)
  3. Envíar resultados de consultas a archivo
  4. Ejecutar la consulta

