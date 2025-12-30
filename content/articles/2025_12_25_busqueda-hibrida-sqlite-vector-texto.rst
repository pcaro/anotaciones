Búsqueda híbrida con SQLite: vector + texto completo
#####################################################

:date: 2025-12-25 10:00
:tags: sqlite, búsqueda, vectores, fts, sql
:lang: es
:category: Programación
:slug: busqueda-hibrida-sqlite-vector-texto-rrf
:summary: Combinando búsqueda vectorial y texto completo en SQLite usando Reciprocal Rank Fusion para obtener mejores resultados

La búsqueda es una funcionalidad fundamental en muchas aplicaciones, pero a menudo nos enfrentamos a dos tipos principales: la búsqueda tradicional por texto completo (Full-Text Search o FTS) y la búsqueda por similitud vectorial. Cada una tiene sus fortalezas: FTS es excelente para la relevancia basada en palabras clave, mientras que la búsqueda vectorial permite encontrar ítems semánticamente similares. La clave está en cómo combinar ambas de forma efectiva.

Alex de `sqlite-vec` ha investigado un enfoque prometedor para combinar estas dos metodologías en SQLite.

El problema de combinar
=======================

El desafío principal al intentar fusionar resultados de FTS y búsqueda vectorial radica en que los "scores" o puntuaciones de cada método son inherentemente diferentes y no directamente comparables. Una puntuación alta en FTS no es lo mismo que una distancia vectorial pequeña.

Reciprocal Rank Fusion (RRF)
=============================

La solución más elegante y efectiva que surge es **Reciprocal Rank Fusion (RRF)**. RRF es un algoritmo de combinación de resultados que evita la necesidad de normalizar o comparar directamente las puntuaciones de relevancia de diferentes fuentes. En su lugar, se centra en las **posiciones de ranking** de los ítems en cada lista de resultados.

.. raw:: html

   <p>La idea es simple:</p>
   <ol>
       <li>Realiza una búsqueda por texto completo y obtén una lista de resultados ranqueada.</li>
       <li>Realiza una búsqueda vectorial y obtén otra lista de resultados ranqueada.</li>
       <li>Combina ambas listas dando más peso a los ítems que aparecen en las primeras posiciones de cualquiera de las listas.</li>
   </ol>

La belleza de RRF es que no necesita saber nada sobre cómo se calculan las puntuaciones individuales, solo sus rankings.

Implementación en SQLite
========================

Aunque el artículo original de Simon Willison presenta una consulta SQL detallada, la esencia de la implementación con `sqlite-vec` implica:

1.  Ejecutar una consulta FTS5 para obtener los IDs de los documentos y sus rankings.
2.  Ejecutar una consulta de similitud vectorial para obtener los IDs de los documentos y sus rankings.
3.  Aplicar la fórmula RRF, que esencialmente asigna una puntuación combinada basada en la inversa de la posición de cada documento en las listas ranqueadas, con un factor de "constante de suavizado" (comúnmente 60).

.. code-block:: sql

    -- Ejemplo conceptual de cómo RRF combina rankings
    WITH
      fts_ranks AS (SELECT id, row_number() OVER (ORDER BY score DESC) as rank FROM fts_search),
      vector_ranks AS (SELECT id, row_number() OVER (ORDER BY distance ASC) as rank FROM vector_search)
    SELECT
      COALESCE(fr.id, vr.id) AS id,
      SUM(1.0 / (COALESCE(fr.rank, 0) + 60) + 1.0 / (COALESCE(vr.rank, 0) + 60)) AS rrf_score
    FROM fts_ranks fr FULL OUTER JOIN vector_ranks vr ON fr.id = vr.id
    GROUP BY id
    ORDER BY rrf_score DESC;


Conclusión
==========

La combinación de búsqueda de texto completo y vectorial mediante RRF en SQLite ofrece una manera potente y flexible de mejorar la relevancia de los resultados de búsqueda. Permite aprovechar lo mejor de ambos mundos, proporcionando a los usuarios resultados más precisos y contextualmente ricos.

*Artículo original*: `Hybrid full-text search and vector search with SQLite`_

.. _Hybrid full-text search and vector search with SQLite: https://simonwillison.net/2024/Oct/4/hybrid-full-text-search-and-vector-search-with-sqlite/