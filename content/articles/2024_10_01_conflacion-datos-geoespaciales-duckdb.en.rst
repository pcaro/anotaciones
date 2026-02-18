Geospatial Data Conflation with DuckDB and Embeddings
#######################################################

:date: 2024-10-01 07:12
:tags: duckdb, geospatial, embeddings, ollama, h3
:lang: en
:category: Programming
:slug: conflacion-datos-geoespaciales-duckdb
:summary: Advanced techniques to integrate geospatial data sources using DuckDB, H3, Ollama, and embedding models

Drew Breunig presents a fascinating case study of **geospatial data conflation**: the process of identifying and merging similar records from different sources.

The Challenge: Integrating Restaurant Data
==========================================

The goal was to connect two data sources:

- **Restaurant inspections** from Alameda County
- **Place data** from Overture Maps Foundation

Two datasets with similar information but structured differently.

Modern Stack Tools
==================

**DuckDB as the main engine**
  - **Staging and querying** large volumes of data
  - Native support for geospatial formats
  - Exceptional performance for exploratory analysis

**H3 for spatial grouping**

.. code-block:: sql

   -- Group nearby places using H3 hexagons
   SELECT h3_cell_to_lat_lng(h3_latlng_to_cell(lat, lng, 9)) as h3_9
   FROM places 

**Ollama for local embeddings**
  - ML framework running locally
  - Generation of contextual embeddings
  - No dependence on external APIs

Three Matching Approaches
=========================

**1. Exact Name Matching**
  - **Result**: ~31% matches
  - **Limitations**: Chain names, unit numbers in addresses

**2. String Similarity (Jaro-Winkler)**

.. code-block:: sql

   -- Comparison combining name and address
   WHERE jaro_winkler_similarity(name1, name2) > 0.8
     AND levenshtein(address1, address2) < 5

- **Result**: ~68% matches
- **Disadvantage**: Complex SQL with many conditional rules

**3. Embedding-Based Matching**

.. code-block:: python

   # Generate contextual description
   description = f"{name} at {address} in {city}"
   embedding = ollama.embeddings(description)

- **Result**: ~71% matches
- **Advantages**: Simpler pipeline, greater flexibility
- **Disadvantage**: Longer processing time

Key Insights
============

1. **There is no silver bullet** - each method has specific strengths
2. **Local tools are powerful** - DuckDB + Ollama allow sophisticated analysis without cloud
3. **Embeddings are promising** - especially for cases with complex context
4. **Conflation requires iteration** - combining multiple techniques improves results

The Future of Data Integration
==============================

This work shows how modern tools democratize techniques that previously required complex infrastructure. The combination of:

- **Analytical databases** (DuckDB)
- **Spatial indices** (H3)
- **Local ML** (Ollama)

...opens new possibilities for intelligent data integration.

*Original article*: `Conflating Overture Places Using DuckDB, Ollama, Embeddings, and More`_

.. _Conflating Overture Places Using DuckDB, Ollama, Embeddings, and More: https://www.dbreunig.com/2024/09/27/conflating-overture-points-of-interests-with-duckdb-ollama-and-more.html
