Django: links in object list
################################

:date: 2014-5-21 10:42
:tags: django, python
:lang: en
:category: Programming
:slug: enlaces-en-listado-de-objectos
:subtitle: change_list

In my projects I usually use links to related items in the admin change_list.

.. contents:: Files

utils.py
========
I have this in :code:`utils.py`

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


I make use of memoize to increase efficiency. I think it is the point between simplicity
in code with ease of use. I have also had decorators to repeat less in admin.py
but when others saw the code they didn't understand it at first.

admin.py
========
A usage example: in :code:`admin.py` (assuming the Link model has a FK called product):

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
