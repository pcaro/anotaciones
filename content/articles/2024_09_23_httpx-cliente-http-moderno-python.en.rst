HTTPX: Modern HTTP Client for Python
####################################

:date: 2024-09-23 00:07
:tags: python, http, httpx, async, requests
:lang: en
:category: Programming
:slug: httpx-cliente-http-moderno-python
:summary: HTTPX emerges as the natural successor to requests, offering async support, HTTP/2, and a modern API for contemporary Python applications.

HTTPX presents itself as the natural evolution of the popular ``requests`` library, maintaining its simplicity but adding modern capabilities that current applications need.

Why HTTPX?
==========

While ``requests`` remains excellent for synchronous use, HTTPX addresses limitations that have arisen over time:

- **No native async support** in requests
- **HTTP/2 not available**
- **Limited type hints**
- **Less precise timeouts**

Installation and Configuration
==============================

.. code-block:: bash

   # Basic installation
   pip install httpx
   
   # With HTTP/2 support
   pip install httpx[http2]
   
   # With advanced compression
   pip install httpx[brotli,zstd]

Familiar API, Modern Capabilities
=================================

**Synchronous usage** - Compatible with requests:

.. code-block:: python

   import httpx
   
   # Basic GET
   r = httpx.get('https://api.github.com/users/octocat')
   print(r.status_code)  # 200
   print(r.json()['login'])  # 'octocat'
   
   # POST with JSON data
   payload = {'key': 'value'}
   r = httpx.post('https://httpbin.org/post', json=payload)
   
   # Custom headers
   headers = {'User-Agent': 'my-app/1.0'}
   r = httpx.get('https://api.example.com/data', headers=headers)

The Power of Async/Await
========================

**Asynchronous client** - The real advantage:

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

Advanced Features
=================

**Strict Timeouts**:

.. code-block:: python

   # Granular timeout
   timeout = httpx.Timeout(10.0, read=5.0)
   
   async with httpx.AsyncClient(timeout=timeout) as client:
       r = await client.get('https://slow-api.example.com')

**Data Streaming**:

.. code-block:: python

   # Streaming download
   async with httpx.AsyncClient() as client:
       async with client.stream('GET', 'https://example.com/bigfile.zip') as r:
           async for chunk in r.aiter_bytes(chunk_size=8192):
               # Process chunk
               process_data(chunk)

**Testing with WSGI/ASGI Applications**:

.. code-block:: python

   # Test FastAPI directly
   from fastapi import FastAPI
   import httpx
   
   app = FastAPI()
   
   @app.get("/")
   def read_root():
       return {"message": "Hello World"}
   
   # Direct test without server
   with httpx.Client(app=app, base_url="http://testserver") as client:
       r = client.get("/")
       assert r.json() == {"message": "Hello World"}

HTTP/2 and Persistent Connections
=================================

.. code-block:: python

   # Client with HTTP/2 and connection pooling
   limits = httpx.Limits(max_keepalive_connections=5, max_connections=10)
   
   async with httpx.AsyncClient(http2=True, limits=limits) as client:
       # Multiple requests reuse connections
       tasks = [client.get(f'https://httpbin.org/get?page={i}') 
                for i in range(50)]
       
       responses = await asyncio.gather(*tasks)
       print(f"Completed {len(responses)} requests")

Comparison: requests vs HTTPX
=============================

.. list-table::
   :header-rows: 1
   
   * - Feature
     - requests
     - HTTPX
   * - Familiar API
     - ✓
     - ✓
   * - Async support
     - ✗
     - ✓
   * - HTTP/2
     - ✗
     - ✓
   * - Type hints
     - Partial
     - Full
   * - Precise timeouts
     - Basic
     - Advanced
   * - WSGI/ASGI Testing
     - ✗
     - ✓
   * - Streaming
     - Basic
     - Advanced

Ideal Use Cases
===============

**HTTPX is perfect for**:

- **Concurrent APIs** with async/await
- **Microservices** that need HTTP/2
- **Application testing** FastAPI/Django
- **Large-scale scraping** with streaming
- **Modern applications** with type safety

**Keep requests for**:

- **Simple scripts** without concurrency
- **Legacy projects** already established
- **Code with dependencies** that require requests

The Future of HTTP in Python
============================

HTTPX represents the way forward for HTTP applications in Python, offering:

- **Modern performance** with async and HTTP/2
- **Developer experience** improved with types
- **Integrated ecosystem** with current frameworks
- **Compatibility** that eases migration

It's time to consider HTTPX as the default HTTP client for new Python projects.

*Official documentation*: `python-httpx.org`_

.. _python-httpx.org: https://www.python-httpx.org/
