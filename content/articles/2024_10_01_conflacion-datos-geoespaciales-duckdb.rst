Conflación de datos geoespaciales con DuckDB y embeddings
#########################################################

:date: 2024-10-01 07:12
:tags: duckdb, geoespacial, embeddings, ollama, h3
:lang: es
:category: Programación
:slug: conflacion-datos-geoespaciales-duckdb
:summary: Técnicas avanzadas para integrar fuentes de datos geoespaciales usando DuckDB, H3, Ollama y modelos de embeddings

Drew Breunig presenta un fascinante caso práctico de **conflación de datos geoespaciales**: el proceso de identificar y unir registros similares de fuentes diferentes.

El reto: Integrar datos de restaurantes
========================================

El objetivo era conectar dos fuentes de datos:

- **Inspecciones de restaurantes** del condado de Alameda
- **Datos de lugares** de Overture Maps Foundation

Dos datasets con información similar pero estructurada de forma diferente.

Herramientas del stack moderno
==============================

**DuckDB como motor principal**
  - **Staging y consultas** de grandes volúmenes de datos
  - Soporte nativo para formatos geoespaciales
  - Performance excepcional para análisis exploratorio

**H3 para agrupación espacial**

.. code-block:: sql

   -- Agrupar lugares cercanos usando hexágonos H3
   SELECT h3_cell_to_lat_lng(h3_latlng_to_cell(lat, lng, 9)) as h3_9
   FROM places 

**Ollama para embeddings locales**
  - Framework de ML ejecutándose localmente
  - Generación de embeddings contextuales
  - Sin dependencia de APIs externas

Tres enfoques de matching
=========================

**1. Matching exacto por nombre**
  - **Resultado**: ~31% de coincidencias
  - **Limitaciones**: Nombres de cadenas, números de unidad en direcciones

**2. Similitud de strings (Jaro-Winkler)**

.. code-block:: sql

   -- Comparación combinando nombre y dirección
   WHERE jaro_winkler_similarity(name1, name2) > 0.8
     AND levenshtein(address1, address2) < 5

- **Resultado**: ~68% de coincidencias
- **Desventaja**: SQL complejo con muchas reglas condicionales

**3. Matching basado en embeddings**

.. code-block:: python

   # Generar descripción contextual
   description = f"{name} at {address} in {city}"
   embedding = ollama.embeddings(description)

- **Resultado**: ~71% de coincidencias
- **Ventajas**: Pipeline más simple, mayor flexibilidad
- **Desventaja**: Mayor tiempo de procesamiento

Insights clave
==============

1. **No existe la bala de plata** - cada método tiene fortalezas específicas
2. **Las herramientas locales son poderosas** - DuckDB + Ollama permiten análisis sofisticados sin cloud
3. **Los embeddings son prometedores** - especialmente para casos con contexto complejo
4. **La conflación requiere iteración** - combinar múltiples técnicas mejora los resultados

El futuro de la integración de datos
====================================

Este trabajo muestra cómo las herramientas modernas democratizan técnicas que antes requerían infraestructura compleja. La combinación de:

- **Bases de datos analíticas** (DuckDB)
- **Índices espaciales** (H3) 
- **ML local** (Ollama)

...abre nuevas posibilidades para la integración inteligente de datos.

*Artículo original*: `Conflating Overture Places Using DuckDB, Ollama, Embeddings, and More`_

.. _Conflating Overture Places Using DuckDB, Ollama, Embeddings, and More: https://www.dbreunig.com/2024/09/27/conflating-overture-points-of-interests-with-duckdb-ollama-and-more.html