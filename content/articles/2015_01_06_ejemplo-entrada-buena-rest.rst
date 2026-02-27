Making a Static Blog with Pelican
#################################

:date: 2015-01-06 14:51
:category: Programming
:tags: python, pelican, static-blog-generator
:slug: making-a-static-blog-with-pelican
:author: Nafiul Islam
:status: draft
:summary: Think of this as a post on all the good features that Pelican has to offer. \
          It shows you the best way to start your blog, write your content and change your \
          blog to however you see fit.

.. contents:: Table of Contents

Pelican allows you to create a static blog. Most blog sites on the web are *dynamic* in the sense that the content of
the site live in a database. In order to view a post on a blog, the server has to *query* the database, get the
right content and then *convert* it into presentable HTML. However, in a static site, every page is pre-rendered
by the static blog generator. This means that your *entire* blog can be uploaded to a server.

Here's a non-exhaustive list of why a static blog generator is good:

* *Cheap Scaling*: Pre-rendered static files can stand the onslaught of traffic if your
  post makes it to the top of hackernews or reddit very cheaply. No queries are being made.
* *Any format*: You can use reStructuredText, Markdown etc. to write your posts.
* *Host Anywhere*: Static sites can be hosted easily on github pages, Amazon S3 and even dropbox.
* *Own Everything*: You have access to all your posts and all your themes. No company in the middle, just you and
  your content.
* *Control*: Static site generators give you a lot of control over pretty much every aspect of your
  site through templates and plugins, allowing you to quickly add complex functionality not found in popular
  web blogging platforms.
* *Update Issues*: If you are using wordpress, you *have* to update your software when a new version comes out; otherwise,
  you have a security risk. However, one can use the same version of a static blog generator indefinitely.

Here's why pelican is a good choice in contrast with other generators: [#assumingPy]_

* *Plugins*: Pelican has a lot of plugins, that allow you to quickly add functionality.
* *Hackable*: Extending pelican as well as altering its behaviour is simple.
* *Themes*: Pelican has *a lot* of themes, and you can make your own.
* *Multi-platform*: Works well on Windows, OSX and Linux. [#windows]_

|
|

I've been using Pelican as my static blog generator for the past year. Over this time,
I have come to recognize its strengths and weaknesses. Pelican allows you to quickly get a themed site up and
running in a matter of minutes. You can also choose to invest more time and create your own theme. In short, if you want
a low hassle setup, its there and if you want a more custom site you can have that too.

However, Pelican's initial setup barely scratches the surface of what's possible with this small yet powerful blog
generator. It has many plugins too for quickly adding extra functionality, like the support of other
document formats; :code:`ipynb` and :code:`asciidoc` for example. Plugins also allow you to support things
like MathJax in your pages and embed disqus comments. [#plugins]_

Getting Started
===============

Before diving in, I expect you to know a few basic things:

* How to use git
* How to use bash or your shell of choice
* How to use Python

Installing Pelican
------------------

Installation is very simple:

.. code-block:: bash

    $ pip install pelican

Feel free to use virtualenv if you want to but its not required.

Pelican works with both Python 2 and Python 3. However, I chose to use Python 2 because I use an automation tool called
Fabric, which only supports python 2 (for the time being).

Basic Setup
-----------

When first beginning with pelican, one can choose to use the pelican skeleton generator to create a basic structure
using :code:`pelican-quickstart`. [#problemsQuickstart]_

.. code-block:: bash

    $ pelican-quickstart
    Welcome to pelican-quickstart v3.5.0.

    This script will help you create a new Pelican-based website.

    Please answer the following questions so this script can generate the files
    needed by Pelican.


    > Where do you want to create your new web site? [.]
    > What will be the title of this web site? Test Site
    > Who will be the author of this web site? Kevin Kevinson
    > What will be the default language of this web site? [en]
    > Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) n
    > Do you want to enable article pagination? (Y/n)
    > How many articles per page do you want? [10] 8
    > Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)
    > Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n)
    > Do you want to upload your website using FTP? (y/N)
    > Do you want to upload your website using SSH? (y/N)
    > Do you want to upload your website using Dropbox? (y/N)
    > Do you want to upload your website using S3? (y/N)
    > Do you want to upload your website using Rackspace Cloud Files? (y/N)
    > Do you want to upload your website using GitHub Pages? (y/N)
    Done. Your new project is available at /Users/quazinafiulislam/Desktop/testingzone

There's no need to change much in the default quickstart wizard. Default values are indicated by :code:`[default]`
and :code:`(y/N)`, where the capitalized letter is the default value. Just one thing to note here is URL prefix; don't
set it right now, set it when you actually want to take your site online, and we will go over how to do that later
in this tutorial.

Your First Post
---------------

After :code:`pelican-quickstart` is done, this is what the directory should look like:

.. code-block:: text

    .
    ├── Makefile
    ├── content/
    ├── develop_server.sh
    ├── fabfile.py
    ├── output/
    ├── pelicanconf.py
    └── publishconf.py

Pelican supports reStructuredText out of the box. If you want to use another format like markdown then just install it:

.. code-block:: bash

    $ pip install markdown

More uncommon formats will be discussed later. With this out of the way, we can create our first post inside the
content folder. All our writing has to be inside the :code:`content` folder, so we change our directory to the
:code:`content` folder:

.. code-block:: bash

    $ cd content

My file is called :code:`first_post.rst` and it looks like this:

.. code-block:: rst

    first_post
    ##########

    :date: 2014-12-13 18:32
    :category: Test

    Hello World from Pelican!

Basically, all one needs is a category and a date. A markdown version of the same post would be:

.. code-block:: markdown

    Title: first_post
    Date: 2014-12-13 18:32
    Category: Test

    Hello world from Pelican!

This is what my project directory looks like now:

.. code-block:: text

    .
    ├── Makefile
    ├── content
    │   └── first_post.rst
    ├── develop_server.sh
    ├── fabfile.py
    ├── pelicanconf.py
    ├── pelicanconf.pyc
    └── publishconf.py

Now changing back to our project directory, we can start the development server, and see the generated blog post:

.. code-block:: bash

    $ make devserver

Once this is done, we should be able to see our post on :code:`localhost:8000`:

.. image:: /images/pelican_05.png
    :alt: Our First post with pelican
    :align: center

We can stop the server through:

.. code-block:: bash

    $ make stopserver

Automation
==========

Although only a title, date and category are required for a post, pelican allows you to add a lot more information like
tags, authors and much more. However, creating a new file with the right date and time can be time consuming,
so we can use certain tools to automate the task for us.

Vanilla Python
--------------

We can create simple scripts to automatically create our
entries with the right date and time. Here is an example script that I use called :code:`make_entry.py`:

.. code-block:: python

    import sys
    from datetime import datetime

    TEMPLATE = """
    {title}
    {hashes}

    :date: {year}-{month}-{day} {hour}:{minute:02d}
    :tags:
    :category:
    :slug: {slug}
    :summary:
    :status: draft


    """


    def make_entry(title):
        today = datetime.today()
        slug = title.lower().strip().replace(' ', '-')
        f_create = "content/{}_{:0>2}_{:0>2}_{}.rst".format(
            today.year, today.month, today.day, slug)
        t = TEMPLATE.strip().format(title=title,
                                    hashes='#' * len(title),
                                    year=today.year,
                                    month=today.month,
                                    day=today.day,
                                    hour=today.hour,
                                    minute=today.minute,
                                    slug=slug)
        with open(f_create, 'w') as w:
            w.write(t)
        print("File created -> " + f_create)


    if __name__ == '__main__':

        if len(sys.argv) > 1:
            make_entry(sys.argv[1])
        else:
            print "No title given"

With this, making a new file can be created like so:

.. code-block:: bash

     $ python make_entry.py "New Post"
    File created -> content/2014_12_13_new-post.rst

Fabric
------

*Jump to the next section if you're not using Python 2* [#fabpy3support]_

Using Vanilla Python is great, but imagine trying to make a script for *every single* task you need done. This would
be a nightmare. Of course, one can keep using if-else statements to add more argument parameters but that is tiring
and not very flexible (not to mention error prone). This is why one option to making scripts that can take in
different parameters is to use a handy library called `Fabric <http://www.fabfile.org/>`__.

I use fabric for most of my tooling, since pelican already generates a :code:`fabfile.py`. Getting a new
command line function in fabric is very easy:

- If you don't have a :code:`fabfile.py`, create one.
- Create a new function inside :code:`fabfile.py`
- Run the function like so: :code:`fab do_something`
- If the function has positional arguments, :code:`fab do_something:True, False`
- If the function has optional keyword arguments :code:`fab do_something:kill_p=True, be_happy=False`

Installing Fabric is easy:

.. code-block:: bash

    $ pip install Fabric

The body of the function to make an entry is the same as before:

.. code-block:: python

    # TEMPLATE is declared before hand, and all the necessary imports made
    def make_entry(title):
        today = datetime.today()
        slug = title.lower().strip().replace(' ', '-')
        f_create = "content/{}_{:0>2}_{:0>2}_{}.rst".format(
            today.year, today.month, today.day, slug)
        t = TEMPLATE.strip().format(title=title,
                                    hashes='#' * len(title),
                                    year=today.year,
                                    month=today.month,
                                    day=today.day,
                                    hour=today.hour,
                                    minute=today.minute,
                                    slug=slug)
        with open(f_create, 'w') as w:
            w.write(t)
        print("File created -> " + f_create)

However, this time we can call it like so:

.. code-block:: bash

     $ fab make_entry:"New Post"

Fabric alternatives
-------------------

There are tonnes of alternatives that allow you to make a simple command line interface quickly:

* `Click <http://click.pocoo.org/3/>`__ : A simple to use CLI by Armin Ronacher.
* `Clip <https://github.com/willyg302/clip.py>`__ : Like click, but newer, and has more features
* `Argparse <https://docs.python.org/3/library/argparse.html>`__ : This package comes with python by default. Its not
  the easiest to use package out there, but if you don't want to install a new package, then this should work fine.

All three work with python 3.

Themes
======

Using a Theme
-------------

Pelican has many themes to choose from its `themes repository`_. These
are the steps:

* Clone a theme repo, or if you want clone the entire `themes repository`_.
* Inside :code:`pelicancon.py` file, change the :code:`THEME` variable, to the directory
  of your theme.

.. _themes repository: https://github.com/getpelican/pelican-themes

On a side note, if you're looking for a place where you can view a screenshot of all the different themes,
`this <http://ptd.pronoiac.org/>`__ site has nice screen-shots of each.

For example, if you wanted to use the `maggner-pelican <https://github.com/kplaube/maggner-pelican>`__ theme:

* Clone it into your project directory, :code:`git clone https://github.com/kplaube/maggner-pelican.git`
* Change the :code:`THEME` variable to :code:`'maggner-pelican'` and you're done :)

Creating Themes
---------------

Creating themes in Pelican is well documented in their documentation about `theme creation`_. Although creating themes
is beyond the scope of this post (because there's a lot that could be said), here are a few pointers:

* Target one format, if you try to create a theme for multiple formats like both rst and md, you're doing to run
  into a lot of issues.
* Using preprocessors can be more effective than using raw css since they allow you create a single css file and provides
  you with a lot more flexibility.
* If you wish to embed disqus or google comments or other third party dynamic content, then I suggest that you use
  separate include files instead of plugins.

.. _theme creation: http://docs.getpelican.com/en/3.5.0/themes.html

Settings
========

The Two Settings Files
----------------------

By default, pelican comes with both a :code:`pelicanconf.py` and :code:`publishconf.py`. When you are writing content
and wish to see a preview, the settings in :code:`pelicanconf.py` are used. When you choose to publish, for example to
github or some other place, the settings in :code:`pelicanconf.py` and :code:`publishconf.py` are used as
:code:`pelicanconf.py` is imported in [>1] below:

.. code-block:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*- #
    from __future__ import unicode_literals

    # This file is only used if you use `make publish` or
    # explicitly specify it as your config file.

    import os
    import sys
    sys.path.append(os.curdir)
    from pelicanconf import *  # 1

    (...)

How Settings Work
-----------------

By convention all settings are capitalized:

.. code-block:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*- #
    from __future__ import unicode_literals

    AUTHOR = u'Nafiul Islam'
    SITENAME = u'fUNNY bLOG'
    SITEURL = ''

If we take a look in the default theme, they are used like so:

.. code-block:: jinja

    {% if DISQUS_SITENAME and SITEURL and article.status != "draft" %}
    <div class="comments">
    <h2>Comments !</h2>
    <div id="disqus_thread"></div>
    <script type="text/javascript">
    var disqus_shortname = '{{ DISQUS_SITENAME }}';
    var disqus_identifier = '{{ article.url }}';
    var disqus_url = '{{ SITEURL }}/{{ article.url }}';
    (function() {
    var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
    (...)

Here, :code:`SITEURL` AND :code:`DISQUS_SITENAME` are both settings that are described in either :code:`pelicanconf.py`
or :code:`publishconf.py`. They appear as variables inside the jinja template. [#notmyideaArticlehtml]_

Most settings that we put into our settings files are used in the theme, however, some settings like
:code:`DEFAULT_PAGINATION` are used to determine other things.

Writing Content
===============

Pelican supports reStructuredText as its default document format. However, there is also support for markdown, ipython
notebook, asciidoc and probably much more. To write in any of these formats, one needs to install the plugin associated
with the file extension, such as `asciidoc_reader <https://github.com/getpelican/pelican-plugins/tree/master/asciidoc_reader>`__
for the asciidoc format and `pelican-ipynb <https://github.com/danielfrg/pelican-ipynb>`__ for the ipython notebook
format. [#notAllPluginsAreFound]_

I would suggest reStructuredText, since it has the most features and can
offer many ways to extend the syntax with features such as directives and interpreted roles. For example, reStructuredText
supports footnotes out of the box, whereas if one were to use markdown, one would need to install a separate plugin and
attach it to pelican. [#footnotesRST]_

However, pelican has many third party plugins for markdown documents as well so if you prefer using markdown, then
please do so, I only recommend reStructuredText because its easy to extend.

Previewing Content
==================

devserver
---------

The default way to see a preview of the generated blog is to use :code:`make devserver`, this regenerates your blog
every time that you change your :code:`content` folder. This option is a horrible way to preview your blog for a couple
of reasons:

* You need to hit the refresh button in your browser to see the changes after a save. This can often get tiring.
* :code:`make devserver` runs two processes in background for no good reason, the processes log data into the console
  anyways, so why not just have a tool that generates your content and terminates when you hit [k:ctrl] + [k:C] ?
* Furthermore, in the transformation from your chosen format to html, if you hit an error, the daemon that keeps
  transforming your files to html also stops, and the error is often buried deep inside the logs

livereload
----------

We need a solution that does two things for us:

* Allows us to see live previews on each save without having to refresh the browser.
* Does not stop unexpectedly from an error.
* Has an easy to use CLI

The solution is to use a neat little package called :code:`livereload` and can be installed through:

.. code-block:: bash

    $ pip install livereload

Once this has been installed, we need to install the livereload plugin for our respective browser. For example in chrome:

.. image:: /images/pelican_01.png
    :alt: Searching for the livereload extension
    :align: center

|

.. image:: /images/pelican_02.png
    :alt: Installing the right plugin
    :align: center

In firefox, we head over to addons.mozilla.org and search for :code:`livereload`:

.. image:: /images/pelican_03.png
    :alt: Installing on Firefox
    :align: center

Once this has been installed, we need to run the livereload server. I do this by adding an extra function to my :code:`fabfile.py` file:

.. code-block:: python

    import livereload

    def live_build(port=8080):

        local('make clean')  # 1
        local('make html')  # 2
        os.chdir('output')  # 3
        server = livereload.Server()  # 4
        server.watch('../content/*.rst',  # 5
            livereload.shell('pelican -s ../pelicanconf.py -o ../output'))  # 6
        server.watch('../naffy/',  # 7
            livereload.shell('pelican -s ../pelicanconf.py -o ../output'))  # 8
        server.watch('*.html')  # 9
        server.watch('*.css')  # 10
        server.serve(liveport=35729, port=port)  # 11

We have a lot to explain here so lets begin with [>1] and [>2]. In both [>1] and [>2], we use the :code:`local` function
from fabric. :code:`local` allows us to run shell commands like :code:`cd`. In this case, we are using the :code:`make`
command because pelican comes with a Makefile. If we involve :code:`make help` from the command line in our project
directory, we get the following:

.. code-block:: bash

    $ make help
    Makefile for a pelican Web site

    Usage:
       make html                        (re)generate the web site
       make clean                       remove the generated files

So, in [>1] we clean out output folder, and in [>2] we generate our html files from our content.

In [>3], we change the directory to our newly created output folder and in [>4] we create an instance
of the :code:`livereload` server. In [>5], we use the :code:`server.watch` function to watch all the :code:`rst` files
since my content is written in reStructuredText. We can change this to :code:`../content/*.md` for markdown files for
example.

:code:`server.watch` had one required argument and two optional arguments. The first argument is :code:`filepath`,
the second is :code:`func`, a function that you run every time watched files are changed.
The last argument is :code:`delay`, which delays function execution. [#livereload]_

In [>6], we specify the function to be run as :code:`livereload.shell('pelican -s ../pelicanconf.py -o ../output')`.
The :code:`shell` function from :code:`livereload` allows us to run shell functions every time a watched file is changed.
In this case, we ask pelican to remake our html files. Why was :code:`make html` not used here? This is because the
:code:`make` command looks for a Makefile and we are right now in our output directory.

In [>7], the server is directed to watch the "naffy" directory. The "naffy" directory is the directory that
houses my theme; if any change is made to my theme, livereload refreshes the server. Replace "naffy" with whatever
folder you are housing your theme in. If you're using the default theme, then do not add [>7] and [>8]. [>8] is the
same as [>6], we just rebuild the html.

In [>9] and [>10], the server is further instructed to watch html and css files that change within the output directory.

Finally in [>11], we tell livereload to serve on port :code:`35729`. This is the default port for the livereload plugin [#chromedoesntwork]_.
The :code:`port` variable is the port of the server serving the files, the :code:`liveport` variable is a port that
livereload uses to make changes directly to the HTML file.

.. image:: /images/pelican_04.png
    :alt: Livereload plugin preferences on FireFox
    :align: center

Plugins
=======

Using Plugins
-------------

Most plugins in pelican tell you how to install them. For example, the `render_math`_ plugin allows you to embed math
inside your posts. Here's the basic gist of what you need to do in order to install them:

* Download the plugin package into your plugins folder, which is set inside your :code:`pelicanconf.py` file in the
  :code:`PLUGIN_PATHS` variable.
* Then append the name of your plugin package inside your :code:`pelicanconf.py` file. [#settingspy]_
* Follow any other additional instructions that your plugin might have.

If just adding the name does not work, then one might consider adding :code:`<plugin_name>.<plugin_file>`. [#pluginsimport]_

.. _render_math: https://github.com/getpelican/pelican-plugins/tree/master/render_math

Creating Plugins
----------------

Creating plugins in pelican basically means that you create a function to do your processing. You then register that
function as a plugin. Creating plugins is
`well documented <http://docs.getpelican.com/en/latest/plugins.html#how-to-create-plugins>`__ and an example of creating
a reader is given.

In my use of pelican, more often than not, I've needed to create plugins that are process text in a given document, not
add support for new document formats. So, I'll show you how I created a plugin for adding keyboard keys like [k:alt]
and [k:⌘] .

I like to create my plugins as packages, but you can create them as simple files as well. So, inside our plugins folder,
create a new package, and inside the package, we create a new file for the plugin:

.. code-block:: bash

     $ cd plugins  # Or whatever your plugins folder is called
     $ mkdir keyboard
     $ cd keyboard
     $ touch __init__.py kb.py
     $ ls
     __init__.py kb.py

Inside :code:`kb.py`, we can need a function that modifies existing code, and a function that registers the function:

.. code-block:: python

    from pelican import signals

    import logging
    import re

    logging.Logger(__name__)


    def content_object_init(instance):
        """
        Provides the key plugin, make sure that you have Keys.css, http://michaelhue.com/keyscss/
        imported inside your HTML. How to use:

            So you hit [kb:CTRL] + [kb:ALT] + [kb:DEL] when in doubt

        Note, that light keyboard keys are enabled by default.
        """
        if instance._content is not None:  # 1
            content = instance._content
            new_content = re.sub(r"\[kb:(.+?)\]", r'<kbd class="light">\1</kbd>', content)  # 2
            instance._content = new_content
            return instance


    def register():
        signals.content_object_init.connect(content_object_init)  # 3

In [>1], we check if the article, page or blog post in question has content; essentially does it have a body. If we
don't have a body, then we skip this object. In [>2], replace  with the corresponding stylized version, so that typing
:code:`[kb:alt]` will give you [k:alt] .

In [>3], we register the function with pelican. Registering this plugin is simple, inside :code:`pelicanconf.py`, we
merely append to the list of :code:`PLUGINS`:

.. code-block:: python

    (...)
    PLUGINS += ['keyboard.kb']
    (...)

I used `key.css <http://michaelhue.com/keyscss/>`__ to style my keys, and I simply added the css file to my theme's
:code:`article.html`.

Once can create far more interesting plugins than the one I've shown, by looking at the plugin repository for
more interesting plugins or even reading the documentation (although its not exhaustive in its explanations).

Hosting on Github Pages
=======================

Github is the best way to host your static blog. Some notable sites which get a substantial amount of traffic are
hosted on github like `Bootstrap <http://getbootstrap.com/>`__, `Yeoman <http://yeoman.io/>`__,
`Pythonic Perambulations <https://jakevdp.github.io/>`__ are hosted on github pages. If you don't have a github
account, creating one is simple and quick.

Creating the repo
-----------------

In order to get a site name like :code:`username.github.io`, one needs to create a repo with that name on github,
set the visibility to public and do not initialize with anything, you want an empty repo that you can push to.

ghp-import
----------

:code:`ghp-import` is a simple plugin that allows you to easily push your content to a github repo. You can install it
using pip:

.. code-block:: bash

    $ pip install ghp-import

There are two steps to doing this:

.. code-block:: bash

    $ ghp-import output
    $ git push git@github.com:<username>/<username>.github.io.git gh-pages:master

This will push the files in your :code:`output` folder directly to the master branch of the :code:`<username>.github.io`
repository. It may take some time initially, but you will be able to see your fully generated blog on this domain.

Custom domains
--------------

In order to get your own top level domain like I have with :code:`nafiulis.me`, you simply need to add a :code:`CNAME`
file with your domain. The :code:`CNAME` file must me located *inside* your output directory and must only have the
domain name. My :code:`CNAME` file looks like this:

.. code-block:: text

    nafiulis.me

The :code:`CNAME` file must be included when you are pushing to your github repo.

Once this is done, you need to link your domain up with github, and this is wonderfully explained in this
`article <http://davidensinger.com/2013/03/setting-the-dns-for-github-pages-on-namecheap/>`__

Automating Publication
======================

I use fabric to automate my publication, I just have two functions to do this:

.. code-block:: python

    def enter_dns_file():  # 1
        with open('output/CNAME', 'w') as f:
            f.write('nafiulis.me')


    def github(publish_drafts=False): # 2

        try:  # 3
            if os.path.exists('output/drafts'):
                if not publish_drafts:
                    local('rm -rf output/drafts')
        except Exception:
            pass

        local('ghp-import output')  # 4
        local('git push'
              'git@github.com:<username>/<username>.github.io.git
              'gh-pages:master') # 5
        local('rm -rf output')  # 6

In [>1], the function :code:`enter_dns_file` is used to insert the :code:`CNAME` file into the output folder before
pushing to github because in [>6], we delete the entire output folder.

In [>2], the :code:`github` function is used to publish the content of the output folder to our github repo, with the
option of publishing drafts which is :code:`False` by default. The :code:`try-catch` block in [>3] is there to check if
we have any drafts in the first place, and if the :code:`publish_drafts` variable is :code:`True`, then we publish them.

From [>4] to [>5], we push the content to the repository. Replace :code:`<username>` with your username.

Acknowledgements
================

I would like to thank **Ashwini Chaudhury**, **Karan Sikka**, **Mahmud Ridwan**, **Sahib bin Mahboob** and
**Keiron Pizzey** for proofreading this article before publication.

-----------------------------------------------------------------------------------------------------------------------

.. [#assumingPy] Assuming that you are proficient in Python.

.. [#windows] Don't use virtualenv, just use your base python when using windows. If using Windows,
              make sure that you have 2.7.9 or 3.4.2, both of which have "ensurepip".

.. [#plugins] | Pelican has its own plugin repository on github. Please note however, that some plugins are defunct \
                and are not supported by newer versions of pelican.
              | https://github.com/getpelican/pelican-plugins

.. [#problemsQuickstart] If you cannot access this, restart your virtualenv if you are currently in one. Otherwise \
                         use restart your shell.

.. [#fabpy3support] | Check out the wall of superpowers if this has changed
                    | http://python3wos.appspot.com/

.. [#notmyideaArticlehtml] | This piece of code is taken from the default theme that comes with pelican called "notmyidea"
                           | https://github.com/getpelican/pelican/blob/3.5.0/pelican/themes/notmyidea/templates/article.html#L17

.. [#notAllPluginsAreFound] The ipython notebook plugin is one example of a plugin that you can't find on the official plugin
                            repository. This may be, because the plugin does not support the newest version, Pelican 3.5, since
                            the plugin says that it required pelican 3.4 to function.

.. [#footnotesRST] | reStructuredText also allows for more versatile footnotes as well. `Check out their quickstart guide <http://docutils.sourceforge.net/docs/user/rst/quickstart.html>`__.

.. [#livereload] `Livereload has documentation on the server class on its documentation website <https://livereload.readthedocs.org/en/latest/#shell>`__

.. [#chromedoesntwork] I cannot find the same options for chrome, hence I use firefox to see live builds of the \
                       generated site

.. [#settingspy] In some documentation regarding plugins, the pelicanconf.py file is called settings.py.

.. [#pluginsimport] Sometimes, Pelican packages do not import the functions necessary inside their :code:`__init__.py`
                    file. In this case you import one of the plugins's files. In most cases it is the file with a
                    :code:`register` method.
