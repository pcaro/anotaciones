Title: SQL: Seleccionar filas con valor máximo por grupo
Date: 2015-10-21 23:05
Tags: sql, mysql, consultas, window-functions, joins
Lang: es
Category: SQL
Slug: sql-select-rows-max-value
Summary: Técnicas SQL para seleccionar filas completas con el valor máximo de una columna dentro de grupos, comparando rendimiento de subqueries, joins y window functions

Un problema común en SQL: **¿cómo seleccionar las filas completas que contienen el valor máximo de una columna para cada grupo?** No solo el valor máximo, sino la **fila entera**.

## El problema

Dado una tabla con `id` y `rev` (revisión), queremos obtener la fila completa con la `rev` más alta para cada `id`.

## Solución 1: Subquery con IN

```sql
SELECT * 
FROM YourTable 
WHERE (id, rev) IN (
    SELECT id, MAX(rev)
    FROM YourTable
    GROUP BY id
)
```

**Ventajas**: Simple y legible  
**Desventajas**: Puede ser lento en tablas grandes

## Solución 2: Join con subquery

```sql
SELECT a.*
FROM YourTable a
INNER JOIN (
    SELECT id, MAX(rev) as maxrev
    FROM YourTable
    GROUP BY id
) b ON a.id = b.id AND a.rev = b.maxrev
```

**Ventajas**: Mejor rendimiento que IN  
**Desventajas**: Más verboso

## Solución 3: Window Functions (MySQL 8+)

```sql
SELECT *
FROM (
    SELECT id, rev, 
    ROW_NUMBER() OVER (PARTITION BY id ORDER BY rev DESC) ranked_order
    FROM YourTable
) a
WHERE a.ranked_order = 1
```

**Ventajas**: Más eficiente para datasets grandes  
**Desventajas**: Requiere versiones modernas de SQL

## Consideraciones de rendimiento

- **Window functions** suelen ser las más eficientes
- **Joins** balancean legibilidad y rendimiento  
- **Subqueries con IN** son las más simples pero menos escalables

## ¿Cuándo usar cada una?

- **Subquery**: Tablas pequeñas, código simple
- **Join**: Balance entre rendimiento y compatibilidad
- **Window functions**: Datasets grandes, SQL moderno disponible

El patrón más robusto y moderno son las **window functions**, que además permiten manejar empates y casos edge más elegantemente.

*Fuente original*: [Stack Overflow](http://stackoverflow.com/questions/7745609/sql-select-only-rows-with-max-value-on-a-column#7745635)