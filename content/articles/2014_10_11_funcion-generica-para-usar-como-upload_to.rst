Función genérica para usar como upload_to
###########################################

:date: 2014-10-11 11:02
:tags: django, python
:lang: es
:category: Programación
:slug: funcion-generica-para-usar-como-upload_to

Los FileField en django necesitan ana función `upload_to`_ que determine donde se subirá el fichero.
Yo suelo tener en :code:`utils.py` una función genérica que los deja en una subcarpeta con el nombre del modelo.

.. code-block:: python

    import os

    def generic_upload_to(instance, filename):
        """
        Generic `upload_to` function for models.FileField and models.ImageField
        which uploads files to `<app_label>/<model_name>/<file_name>`.
        """
        return os.path.join(instance._meta.app_label, instance._meta.model_name, filename)

El uso el previsible:

.. code-block:: python

    featured_image = ImageField(upload_to=generic_upload_to,
                                verbose_name='Imagen Destacada (770x490)',
                                max_length=250, blank=True, null=True)

.. _upload_to: https://docs.djangoproject.com/en/1.7/ref/models/fields/#django.db.models.FileField.upload_to 
