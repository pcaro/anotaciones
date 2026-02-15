Repeating a function with threads
#################################

:date: 2015-5-3 21:00
:tags: python
:lang: en
:category: Programming
:slug: repetiendo-una-función-con-hilos
:summary: Let's use threads in python to periodically execute a function


I have a service (with `daemonocle`_ which I will talk about another day) running all the time on an `odroid c1`_.
I considered it was better to control with threads some periodic tasks that I have to repeat (which I was already using)
instead of the typical cron entry.

.. _odroid c1: http://www.hardkernel.com/main/products/prdt_info.php

This way I can better control their operation. The advantages for me in this case and for these specific tasks:

- I already have the logging configuration performed by the main process. These tasks leave their info in my rotational logs.
- Stopping (starting) the service stops everything at once.
- I measure resource consumption as a whole

Here is the snippet used.

In :code:`utils.py`:

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



In :code:`main.py` you can see its usage, one of the functions receives a parameter:

.. code-block:: python

    setup_logging()
    youtube = youtube_api.get_authenticated_service(None)
    events_thread = RepeatedTimer(UPDATE_EVENTS_SECONDS, backend_api.update_events_database)
    streams_thread = RepeatedTimer(UPDATE_STREAM_SECONDS, youtube_api.update_streams_database, youtube)


I should tell you that I stop these threads and clean resources in the shutdown callback event which is one of the best things about :code:`daemonocle`.
You already know that python is not capable of fully parallelizing threads due to the GIL, but for simple tasks like these with very little load
it is simple and works perfectly.

.. _daemonocle: https://github.com/jnrbsn/daemonocle
