Anotaciones. Blog de Pablo Caro
===============================

This are my blog (anotaciones_) contents pelican_



Getting up and running
----------------------

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* uv (https://docs.astral.sh/uv/)

First install dependencies using uv::

    $ uv sync

Then download theme and plugins::

    git clone https://github.com/pcaro/pelican-elegant.git
    git clone https://github.com/getpelican/pelican-plugins.git plugins

**Development Commands**

Build the site::

    $ uv run invoke build

Develop with local server::

    $ uv run invoke develop

Live reloading (recommended for development)::

    $ uv run invoke develop-live

Build for production::

    $ uv run invoke production

**Publishing**

The site is automatically deployed to GitHub Pages when you push to the master branch using GitHub Actions.

For manual publishing::

    $ uv run invoke publish

**New entries**

Create a new post::

    $ uv run invoke write "título del post"

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


A good editor (with preview) is https://github.com/retext-project/retext
Note: A good rst previewer is http://rst.ninjs.org/ or you can use restview_

It's time to write entries!!!

.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/
.. _pelican: http://getpelican.com
.. _anotaciones: http://pablocaro.es
.. _appropriate browser extension: http://feedback.livereload.com/knowledgebase/articles/86242-how-do-i-install-and-use-the-browser-extensions-
.. _restview: https://mg.pov.lt/restview/
