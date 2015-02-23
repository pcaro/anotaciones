#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import SocketServer
import sys
from datetime import datetime
import livereload
import SimpleHTTPServer
from fabric.api import *


def _build():
    local('pelican -s pelicanconf.py -o output_dev')


def _regenerate():
    local('pelican -r -s pelicanconf.py -o output_dev')


def _serve():
    os.chdir('output_dev')

    PORT = 7000

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()


def develop():
    _serve()
    _regenerate()


def develop_live(port=7000):
    "Develop using livereload"
    HERE = os.path.dirname(__file__)
    sys.path.append(HERE)
    from pelicanconf import THEME
    _build()
    os.chdir('output_dev')
    server = livereload.Server()
    server.watch('../content/*',
                 livereload.shell('pelican -s ../pelicanconf.py -o ../output_dev'))

    server.watch(THEME,
                 livereload.shell('pelican -s ../pelicanconf.py -o ../output_dev'))
    server.watch('*.html')
    server.watch('*.css')
    server.serve(liveport=35729, port=port)


def production():
    local('pelican -s publishconf.py')


def sent_to_githubpages(publish_drafts=False):

    try:
        if os.path.exists('output/drafts'):
            if not publish_drafts:
                local('rm -rf output/drafts')
    except Exception:
        pass

    # production()
    os.chdir('output')
    local('git add *')
    local('git ci')
    local('git push origin master')

TEMPLATE = """
{title}
{hashes}

:date: {year}-{month}-{day} {hour}:{minute:02d}
:tags: django, python
:lang: es
:category: Progamación
:slug: {slug}
:summary:
:status: draft

# These are the optional article meta data variables that you can use
# subtitle
# summary
# disqus_identifier
# modified
# keywords

"""


def write(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    f_create = "content/articles/{}_{:0>2}_{:0>2}_{}.rst".format(
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
