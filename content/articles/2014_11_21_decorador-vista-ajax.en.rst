Ajax view decorator
###################

:date: 2014-11-21 11:12
:tags: python, django
:lang: en
:category: Programming
:slug: decorador-vista-ajax

To force a `django`_ view to be called only via AJAX calls.

.. code-block:: python

    def ajax_required(f):
        """
        AJAX request required decorator
        use it in your views:

        @ajax_required
        def my_view(request):
            ....

        """
        def wrap(request, *args, **kwargs):
            if not request.is_ajax():
                return HttpResponseBadRequest()
            return f(request, *args, **kwargs)
        wrap.__doc__ = f.__doc__
        wrap.__name__ = f.__name__
        return wrap


A possible usage example:

.. code-block:: python

    @login_required
    @ajax_required
    def update_starts(request):
        ...
        return JsonResponse({'result': 'ok'})

.. _django: https://www.djangoproject.com/
