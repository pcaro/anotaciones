Búsqueda híbrida con SQLite: vector + texto completo
####################################################

:date: 2024-10-06 11:43
:tags: sqlite, búsqueda, vectores, fts, sql
:lang: es
:category: Programación
:slug: busqueda-hibrida-sqlite-vector-texto
:summary: Combinando búsqueda vectorial y texto completo en SQLite usando Reciprocal Rank Fusion para obtener mejores resultados

Simon Willison presenta una aproximación fascinante para combinar búsqueda vectorial y tradicional búsqueda de texto completo en SQLite, usando una técnica llamada **Reciprocal Rank Fusion (RRF)**.

El problema central
===================

Cuando tenemos búsquedas vectoriales (basadas en similitud semántica) y búsquedas de texto completo (FTS), cada una devuelve puntuaciones en escalas completamente diferentes:

- FTS devuelve puntuaciones de relevancia
- Búsqueda vectorial devuelve distancias de similitud

¿Cómo combinar estos resultados de manera efectiva?

La solución: Reciprocal Rank Fusion
===================================

La técnica RRF evita comparar puntuaciones incompatibles y en su lugar se basa en el **ranking** de cada resultado dentro de su respectivo método de búsqueda.

.. code-block:: sql

    SELECT 
        content,
        1.0 / (:rrf_k + coalesce(fts_rank, 999)) * :fts_weight +
        1.0 / (:rrf_k + coalesce(vec_rank, 999)) * :vec_weight as combined_rank
    FROM (
        -- Subconsulta FTS con row_number()
        SELECT *, row_number() OVER (ORDER BY rank) as fts_rank
        FROM fts_search(:query)
    ) fts
    FULL OUTER JOIN (
        -- Subconsulta vectorial con row_number()
        SELECT *, row_number() OVER (ORDER BY distance) as vec_rank  
        FROM vector_search(:query, :k)
    ) vec ON fts.id = vec.id
    ORDER BY combined_rank DESC;

Ventajas del enfoque híbrido
============================

1. **Flexibilidad**: Permite ajustar pesos entre FTS y búsqueda vectorial
2. **Robustez**: Los resultados pueden aparecer en uno o ambos métodos
3. **Escalabilidad**: No requiere normalización compleja de puntuaciones
4. **Simplicidad**: Una sola consulta SQL maneja toda la lógica

SQLite como plataforma unificada
=================================

Con extensiones como `sqlite-vec`_, SQLite se convierte en una plataforma poderosa para:

- Búsqueda de texto completo (FTS5 nativo)
- Búsqueda vectorial de embeddings
- Combinación híbrida de ambas técnicas

Esta aproximación democratiza las técnicas avanzadas de búsqueda, haciéndolas accesibles sin infraestructura compleja.

.. _sqlite-vec: https://github.com/asg017/sqlite-vec

*Artículo original*: `Hybrid full-text search and vector search with SQLite`_

.. _Hybrid full-text search and vector search with SQLite: https://simonwillison.net/2024/Oct/4/hybrid-full-text-search-and-vector-search-with-sqlite/