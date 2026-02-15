Settings vars processor
#######################

:date: 2014-1-08 11:23
:tags: python, django
:lang: en
:category: Programming
:slug: settings-vars-processor

I usually use this at the beginning of projects.

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

It is used like this:

.. code-block:: python

    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        ...
        'web.context_processors.settings',
    )

    DEBUG = True
    CLIENT_SLOGAN = 'This is an example'
    TEMPLATE_VISIBLE_SETTINGS = (
        'DEBUG',
        'CLIENT_SLOGAN'
    )
