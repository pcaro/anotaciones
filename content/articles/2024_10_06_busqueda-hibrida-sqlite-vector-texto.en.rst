Hybrid Search with SQLite: Vector + Full-Text
###################################################

:date: 2024-10-06 11:43
:tags: sqlite, search, vectors, fts, sql
:lang: en
:category: Programming
:slug: busqueda-hibrida-sqlite-vector-texto
:summary: Combining vector search and full-text search in SQLite using Reciprocal Rank Fusion for better results

Simon Willison presents a fascinating approach to combining vector search and traditional full-text search in SQLite, using a technique called **Reciprocal Rank Fusion (RRF)**.

The Core Problem
================

When we have vector searches (based on semantic similarity) and full-text searches (FTS), each returns scores on completely different scales:

- FTS returns relevance scores
- Vector search returns similarity distances

How to combine these results effectively?

The Solution: Reciprocal Rank Fusion
====================================

The RRF technique avoids comparing incompatible scores and instead relies on the **ranking** of each result within its respective search method.

.. code-block:: sql

    SELECT 
        content,
        1.0 / (:rrf_k + coalesce(fts_rank, 999)) * :fts_weight +
        1.0 / (:rrf_k + coalesce(vec_rank, 999)) * :vec_weight as combined_rank
    FROM (
        -- FTS subquery with row_number()
        SELECT *, row_number() OVER (ORDER BY rank) as fts_rank
        FROM fts_search(:query)
    ) fts
    FULL OUTER JOIN (
        -- Vector subquery with row_number()
        SELECT *, row_number() OVER (ORDER BY distance) as vec_rank  
        FROM vector_search(:query, :k)
    ) vec ON fts.id = vec.id
    ORDER BY combined_rank DESC;

Advantages of the Hybrid Approach
=================================

1. **Flexibility**: Allows adjusting weights between FTS and vector search
2. **Robustness**: Results can appear in one or both methods
3. **Scalability**: Does not require complex score normalization
4. **Simplicity**: A single SQL query handles all the logic

SQLite as a Unified Platform
============================

With extensions like `sqlite-vec`_, SQLite becomes a powerful platform for:

- Full-text search (Native FTS5)
- Vector embedding search
- Hybrid combination of both techniques

This approach democratizes advanced search techniques, making them accessible without complex infrastructure.

.. _sqlite-vec: https://github.com/asg017/sqlite-vec

*Original article*: `Hybrid full-text search and vector search with SQLite`_

.. _Hybrid full-text search and vector search with SQLite: https://simonwillison.net/2024/Oct/4/hybrid-full-text-search-and-vector-search-with-sqlite/
