Managing GitHub installations with gah
######################################

:date: 2026-02-11 20:23
:tags: linux, tools, cli
:lang: en
:category: Linux
:slug: gestionando-instalaciones-desde-github-con-gah
:summary: Install binaries directly from GitHub releases easily with gah.
:status: published

`gah <https://github.com/get-gah/gah>`_ is a tool that simplifies installing programs distributed via GitHub releases. It's a lightweight alternative when you don't want to rely on your distro's package manager or when you need a newer version.

Installation
------------

To install **gah**, you can use the official script:

.. code-block:: bash

    bash -c "$(curl -fsSL https://raw.githubusercontent.com/get-gah/gah/refs/heads/master/tools/install.sh)"

Usage
-----

Once installed, usage is very straightforward. Here are a couple of examples I've used recently to install popular Rust tools:

To install `fd` (a fast alternative to ``find``):

.. code-block:: bash

    gah install sharkdp/fd

To install `ripgrep` (a fast alternative to ``grep``):

.. code-block:: bash

    gah install BurntSushi/ripgrep

Gah handles downloading the correct asset for your architecture, unpacking it, and placing it in your path.
