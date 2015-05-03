Repitiendo una función con hilos
#################################

:date: 2015-5-3 21:00
:tags: python
:lang: es
:category: Progamación
:slug: repetiendo-una-función-con-hilos
:summary: Vamos a utilizar hilos en python para ejecutar periodicamente una función


Tengo un servicio (con `daemonocle`_  del que ya hablaré otro día) corriendo todo el tiempo en una `odroid c1`_.
Consideré que era mejor controlar con hilos unas tareas periódicas que tengo que repetir (que ya estaba usando)
en lugar de la típica entrada en cron.

.. _odroid c1: http://www.hardkernel.com/main/products/prdt_info.php

Así puedo contrar mejor el funcionamiento de las mismas. Las ventajas para mí en este caso y para estas tareas concretas:

- Ya tengo la configuración de logging realizada por el proceso principal. Estas tareas dejan su info en mis log rotacionales.
- Parando  (arrancando) el servicio lo paro todo y a la vez.
- Mido el consumo de recursos en su conjunto

Dejo el snippet utilizado.

En  :code:`utils.py`:

.. code-block:: python

    # -*- coding: utf-8 -*-
    from __future__ import unicode_literals
    import threading


    class RepeatedTimer(object):

        def __init__(self, interval, function, *args, **kwargs):
            self._timer = None
            self.interval = interval
            self.function = function
            self.args = args
            self.kwargs = kwargs
            self.is_running = False
            self.start()

        def _run(self):
            self.is_running = False
            self.start()
            self.function(*self.args, **self.kwargs)

        def start(self):
            if not self.is_running:
                self._timer = threading.Timer(self.interval, self._run)
                self._timer.start()
                self.is_running = True

        def stop(self):
            self._timer.cancel()
            self.is_running = False



En :code:`main.py` podeís ver su uso, una de las funciones recibe un parámetro:

.. code-block:: python

    setup_logging()
    youtube = youtube_api.get_authenticated_service(None)
    events_thread = RepeatedTimer(UPDATE_EVENTS_SECONDS, backend_api.update_events_database)
    streams_thread = RepeatedTimer(UPDATE_STREAM_SECONDS, youtube_api.update_streams_database, youtube)


Deciros que paro estos hilos y limpio recursos en el evento de callback para shutdown que es de lo mejor de :code:`daemonocle`.
Ya sabéis que python no es capaz de paralelizar del todo los hilos debido a al GIL, pero para tareas simples como estas con muy poca carga
es simple y funciona a la perfección.

.. _daemonocle: https://github.com/jnrbsn/daemonocle