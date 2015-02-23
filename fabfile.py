#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import SocketServer
import sys
from datetime import datetime

import fabric.contrib.project as project
import livereload
import SimpleHTTPServer
from fabric.api import *

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path


def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))


def build():
    local('pelican -s pelicanconf.py')


def rebuild():
    clean()
    build()


def regenerate():
    local('pelican -r -s pelicanconf.py')


def serve():
    os.chdir(env.deploy_path)

    PORT = 8000

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()


def devserve():
    build()
    serve()


def preview():
    local('pelican -s publishconf.py')


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


def develop(port=7000):
    "Develop using livereload"
    HERE = os.path.dirname(__file__)
    sys.path.append(HERE)
    from pelicanconf import THEME
    rebuild()
    os.chdir('output')
    server = livereload.Server()
    server.watch('../content/*',
                 livereload.shell('pelican -s ../pelicanconf.py -o ../{}'.format(env.deploy_path)))

    server.watch(THEME,
                 livereload.shell('pelican -s ../pelicanconf.py -o ../output'))
    server.watch('*.html')
    server.watch('*.css')
    server.serve(liveport=35729, port=port)


def enter_dns_file():
    with open('output/CNAME', 'w') as f:
        f.write('pablocaro.es')


def github(publish_drafts=False):

    try:
        if os.path.exists('output/drafts'):
            if not publish_drafts:
                local('rm -rf output/drafts')
    except Exception:
        pass

    local('ghp-import output')
    local('git push'
          'git@github.com:pcaro/pcaro.github.io.git'
          'gh-pages:master')
    local('rm -rf output')
