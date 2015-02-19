Anotaciones. Blog de Pablo Caro
===============================

This are my blog (anotaciones_) contents pelican_



Getting up and running
----------------------

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* pip
* virtualenv

First make sure to create and activate a virtualenv_, then open a terminal at the project root and install the requirements for local development::

    $ pip install -r requirements.txt


**Live reloading and Sass CSS compilation**

If you'd like to take advantage of live reloading you can do so with the included fabric task. Make sure requirements are installed and virtualenv activated. Then, in the project root run::

    $ fab develop


To get live reloading to work you'll probably need to install an `appropriate browser extension`_

**New entries**

I have a *make_entry* task too. Use it::

    $ fab make_entry:"un titulo"

And a new file (restructured text) is created with de actual date and contents like::

    un titulo
    #########

    :date: 2015-2-19 12:24
    :tags:
    :lang: es
    :category:
    :slug: un-titulo
    :summary:
    :status: draft

Note: A good rst previewer is http://rst.ninjs.org/ or you can use restview_

It's time to write entries!!!

.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/
.. _pelican: http://getpelican.com
.. _anotaciones: http://pablocaro.es
.. _appropriate browser extension: http://feedback.livereload.com/knowledgebase/articles/86242-how-do-i-install-and-use-the-browser-extensions-
.. _restview: https://mg.pov.lt/restview/
