Title: SQL: Select Rows with Max Value per Group
Date: 2015-10-21 23:05
Tags: sql, mysql, queries, window-functions, joins
Lang: en
Category: SQL
Slug: sql-select-rows-max-value
Summary: SQL techniques to select complete rows with the maximum value of a column within groups, comparing performance of subqueries, joins, and window functions

A common problem in SQL: **how to select the complete rows that contain the maximum value of a column for each group?** Not just the maximum value, but the **entire row**.

## The Problem

Given a table with `id` and `rev` (revision), we want to get the complete row with the highest `rev` for each `id`.

## Solution 1: Subquery with IN

```sql
SELECT * 
FROM YourTable 
WHERE (id, rev) IN (
    SELECT id, MAX(rev)
    FROM YourTable
    GROUP BY id
)
```

**Pros**: Simple and readable
**Cons**: Can be slow on large tables

## Solution 2: Join with Subquery

```sql
SELECT a.*
FROM YourTable a
INNER JOIN (
    SELECT id, MAX(rev) as maxrev
    FROM YourTable
    GROUP BY id
) b ON a.id = b.id AND a.rev = b.maxrev
```

**Pros**: Better performance than IN
**Cons**: More verbose

## Solution 3: Window Functions (MySQL 8+)

```sql
SELECT *
FROM (
    SELECT id, rev, 
    ROW_NUMBER() OVER (PARTITION BY id ORDER BY rev DESC) ranked_order
    FROM YourTable
) a
WHERE a.ranked_order = 1
```

**Pros**: More efficient for large datasets
**Cons**: Requires modern SQL versions

## Performance Considerations

- **Window functions** are usually the most efficient
- **Joins** balance readability and performance
- **Subqueries with IN** are the simplest but less scalable

## When to Use Each?

- **Subquery**: Small tables, simple code
- **Join**: Balance between performance and compatibility
- **Window functions**: Large datasets, modern SQL available

The most robust and modern pattern is **window functions**, which also allow handling ties and edge cases more elegantly.

*Original source*: [Stack Overflow](http://stackoverflow.com/questions/7745609/sql-select-only-rows-with-max-value-on-a-column#7745635)
