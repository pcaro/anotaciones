Settings vars processor
#######################

:date: 2014-1-08 11:23
:tags: python, django
:lang: es
:category: Programación
:slug: settings-vars-processor

Lo suelo usar durante el principio de los proyectos.

.. code-block:: python

    from django.conf import settings as django_settings
    from django.core.exceptions import ImproperlyConfigured


    def settings(request):
        """
        Adds the settings specified in settings.TEMPLATE_VISIBLE_SETTINGS to
        the request context.
        """
        new_settings = {}
        for attr in django_settings.TEMPLATE_VISIBLE_SETTINGS:
            try:
                new_settings[attr] = getattr(django_settings, attr)
            except AttributeError:
                m = "TEMPLATE_VISIBLE_SETTINGS: '{0}' does not exist".format(attr)
                raise ImproperlyConfigured(m)
        return new_settings

Se usa así:

.. code-block:: python

    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        ...
        'web.context_processors.settings',
    )

    DEBUG = True
    CLIENT_SLOGAN = 'Esto es un ejemplo'
    TEMPLATE_VISIBLE_SETTINGS = (
        'DEBUG',
        'CLIENT_SLOGAN'
    )


