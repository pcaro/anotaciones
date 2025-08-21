HTTPX: Cliente HTTP moderno para Python
#######################################

:date: 2024-09-23 00:07
:tags: python, http, httpx, async, requests
:lang: es
:category: Programación
:slug: httpx-cliente-http-moderno-python
:summary: HTTPX emerge como el sucesor natural de requests, ofreciendo soporte async, HTTP/2 y una API moderna para aplicaciones Python contemporáneas

HTTPX se presenta como la evolución natural de la popular biblioteca ``requests``, manteniendo su simplicidad pero añadiendo capacidades modernas que las aplicaciones actuales necesitan.

¿Por qué HTTPX?
================

Mientras ``requests`` sigue siendo excelente para uso síncrono, HTTPX aborda las limitaciones que han surgido con el tiempo:

- **Sin soporte async nativo** en requests
- **HTTP/2 no disponible** 
- **Type hints limitados**
- **Timeouts menos precisos**

Instalación y configuración
===========================

.. code-block:: bash

   # Instalación básica
   pip install httpx
   
   # Con soporte HTTP/2
   pip install httpx[http2]
   
   # Con compresión avanzada
   pip install httpx[brotli,zstd]

API familiar, capacidades modernas
==================================

**Uso síncrono** - Compatible con requests:

.. code-block:: python

   import httpx
   
   # GET básico
   r = httpx.get('https://api.github.com/users/octocat')
   print(r.status_code)  # 200
   print(r.json()['login'])  # 'octocat'
   
   # POST con datos JSON
   payload = {'key': 'value'}
   r = httpx.post('https://httpbin.org/post', json=payload)
   
   # Headers personalizados
   headers = {'User-Agent': 'my-app/1.0'}
   r = httpx.get('https://api.example.com/data', headers=headers)

El poder del async/await
========================

**Cliente asíncrono** - La verdadera ventaja:

.. code-block:: python

   import asyncio
   import httpx
   
   async def fetch_user(client, username):
       r = await client.get(f'https://api.github.com/users/{username}')
       return r.json()
   
   async def main():
       async with httpx.AsyncClient() as client:
           users = await asyncio.gather(
               fetch_user(client, 'octocat'),
               fetch_user(client, 'gvanrossum'),
               fetch_user(client, 'kennethreitz')
           )
       
       for user in users:
           print(f"{user['login']}: {user['public_repos']} repos")
   
   asyncio.run(main())

Funcionalidades avanzadas
=========================

**Timeouts estrictos**:

.. code-block:: python

   # Timeout granular
   timeout = httpx.Timeout(10.0, read=5.0)
   
   async with httpx.AsyncClient(timeout=timeout) as client:
       r = await client.get('https://slow-api.example.com')

**Streaming de datos**:

.. code-block:: python

   # Descarga streaming
   async with httpx.AsyncClient() as client:
       async with client.stream('GET', 'https://example.com/bigfile.zip') as r:
           async for chunk in r.aiter_bytes(chunk_size=8192):
               # Procesar chunk
               process_data(chunk)

**Pruebas con aplicaciones WSGI/ASGI**:

.. code-block:: python

   # Testear FastAPI directamente
   from fastapi import FastAPI
   import httpx
   
   app = FastAPI()
   
   @app.get("/")
   def read_root():
       return {"message": "Hello World"}
   
   # Test directo sin servidor
   with httpx.Client(app=app, base_url="http://testserver") as client:
       r = client.get("/")
       assert r.json() == {"message": "Hello World"}

HTTP/2 y conexiones persistentes
=================================

.. code-block:: python

   # Cliente con HTTP/2 y pool de conexiones
   limits = httpx.Limits(max_keepalive_connections=5, max_connections=10)
   
   async with httpx.AsyncClient(http2=True, limits=limits) as client:
       # Múltiples requests reutilizan conexiones
       tasks = [client.get(f'https://httpbin.org/get?page={i}') 
                for i in range(50)]
       
       responses = await asyncio.gather(*tasks)
       print(f"Completed {len(responses)} requests")

Comparativa: requests vs HTTPX
==============================

.. list-table::
   :header-rows: 1
   
   * - Característica
     - requests
     - HTTPX
   * - API familiar
     - ✓
     - ✓
   * - Soporte async
     - ✗
     - ✓
   * - HTTP/2
     - ✗
     - ✓
   * - Type hints
     - Parcial
     - Completo
   * - Timeouts precisos
     - Básico
     - Avanzado
   * - Testing WSGI/ASGI
     - ✗
     - ✓
   * - Streaming
     - Básico
     - Avanzado

Casos de uso ideales
====================

**HTTPX es perfecto para**:

- **APIs concurrentes** con async/await
- **Microservicios** que necesitan HTTP/2
- **Testing de aplicaciones** FastAPI/Django
- **Scraping a gran escala** con streaming
- **Aplicaciones modernas** con type safety

**Mantén requests para**:

- **Scripts simples** sin concurrencia
- **Proyectos legacy** ya establecidos
- **Código con dependencias** que requieren requests

El futuro de HTTP en Python
============================

HTTPX representa el camino hacia adelante para aplicaciones HTTP en Python, ofreciendo:

- **Performance moderna** con async y HTTP/2
- **Developer experience** mejorada con tipos
- **Ecosistema integrado** con frameworks actuales
- **Compatibilidad** que facilita migración

Es hora de considerar HTTPX como el cliente HTTP por defecto para nuevos proyectos Python.

*Documentación oficial*: `python-httpx.org`_

.. _python-httpx.org: https://www.python-httpx.org/