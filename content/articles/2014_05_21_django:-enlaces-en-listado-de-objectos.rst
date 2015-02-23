Django: enlaces en listado de objectos
######################################

:date: 2014-5-21 10:42
:tags: django, python
:lang: es
:category: Programación
:slug: enlaces-en-listado-de-objectos
:subtitle: change_list

En mis proyectos suelo usar enlaces a elementos relacionados en el change_list del admin.

.. contents:: Ficheros

utils.py
========
Tengo esto en :code:`utils.py`

.. code-block:: python

    from django.contrib import admin
    from django.contrib.contenttypes.models import ContentType
    from django.core import urlresolvers
    from django.utils.datastructures import SortedDict
    from django.utils.functional import memoize

    def get_change_url(obj):
        """ Utility method
            def server_link(self, obj):
                 return self.get_change_url(obj.server)
            server_link.short_description = _('server')
            server_link.allow_tags = True
            server_link.admin_order_field = 'server__name'
        """
        if obj is None:
            return
        content_type = get_content_type(obj.__class__)

        change_url = urlresolvers.reverse(
            "%s:%s_%s_change" % (admin.site.app_name, content_type.app_label, content_type.model),
            args=[obj.pk])
        return '<a href="%s">%s</a>' % (change_url, obj)


    def _get_content_type(klass):
        return ContentType.objects.get_for_model(klass)
    get_content_type = memoize(_get_content_type, SortedDict(), 2)


Hago uso de memoize para aumentar la eficiencia. Creo que es el punto junto entre simplicidad
en el código con facilidad de uso. He tenido también decoradores para repetir menos en el admin.py
pero cuando otros veían el código no lo entendían a la primera.

admin.py
========
Un ejemplo de uso: en :code:`admin.py` (suponiendo que el modelo Link tiene un FK llamado product):

.. code-block:: python

    from utils import get_change_url

    class LinkAdmin(AdminImageMixin, admin.ModelAdmin):
        list_display = ['name', 'is_visible', 'product_link', 'updated_at']
        search_fields = ['name', ]

        def product_link(self, obj):
            return get_change_url(obj.product)
        product_link.short_description = 'Product'
        product_link.allow_tags = True
        product_link.admin_order_field = 'product__name'
