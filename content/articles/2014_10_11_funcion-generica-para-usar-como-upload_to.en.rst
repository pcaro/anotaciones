Generic function to use as upload_to
#######################################

:date: 2014-10-11 11:02
:tags: django, python
:lang: en
:category: Programming
:slug: funcion-generica-para-usar-como-upload_to

FileFields in Django need an `upload_to`_ function that determines where the file will be uploaded.
I usually have a generic function in :code:`utils.py` that leaves them in a subfolder with the model name.

.. code-block:: python

    import os

    def generic_upload_to(instance, filename):
        """
        Generic `upload_to` function for models.FileField and models.ImageField
        which uploads files to `<app_label>/<model_name>/<file_name>`.
        """
        return os.path.join(instance._meta.app_label, instance._meta.model_name, filename)

The usage is predictable:

.. code-block:: python

    featured_image = ImageField(upload_to=generic_upload_to,
                                verbose_name='Featured Image (770x490)',
                                max_length=250, blank=True, null=True)

.. _upload_to: https://docs.djangoproject.com/en/1.7/ref/models/fields/#django.db.models.FileField.upload_to
