#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Pablo Caro'
SITENAME = u"""<span style="color:#AA1032;">Anotaciones</span> <span style="color:darkblue;">por</span> <span style="color:black">Pablo Caro</span>"""
# SITENAME = u'Anotaciones de Pablo Caro'
SITEURL = ''

ARTICLE_PATH = "articles/"
PATH = 'content'
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git', '.gitignore', 'README.rst', 'CNAME', 'robots.txt']
STATIC_PATHS = ['theme/images', 'images', 'extras']
EXTRA_PATH_METADATA = {
    'extras/CNAME': {'path': 'CNAME'},
    'extras/robots.txt': {'path': 'robots.txt'},
}


TIMEZONE = 'Europe/Paris'
DISQUS_SITENAME = 'anotaciones'

DEFAULT_LANG = u'es'

# i18n_subsites
JINJA_EXTENSIONS = ['jinja2.ext.i18n', ]
I18N_TEMPLATES_LANG = "en"

DEFAULT_CATEGORY = 'Miscellaneous'
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = u'{slug}'
PAGE_URL = u'{slug}'
PAGE_SAVE_AS = u'{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

GITHUB_URL = 'http://github.com/pcaro'
TWITTER_USERNAME = 'pcaro'
# Social
SOCIAL = (
    ('Twitter', 'http://twitter.com/pcaro'),
    ('Github', GITHUB_URL),
    ('Linkedin', 'https://www.linkedin.com/in/pcarorevuelta'),
    ('Facebook', 'https://www.facebook.com/pablo.carorevuelta'),
    ('Email', 'mailto:correo@pablocaro.es'),
)

DEFAULT_PAGINATION = 5
PLUGIN_PATHS = ['plugins']

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# THEME = 'pelican-themes/mg'
# THEME = 'pelican-themes/Just-Read'  # Un buen punto de partida. Necesita cosas de elegant
# THEME = 'pelican-themes/svbhack'
THEME = 'pelican-elegant'  # Requiere atribucion

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# THEME settings
TYPOGRIFY = True
DEFAULT_PAGINATION = False

PLUGINS = ['i18n_subsites', 'extended_sitemap', 'extract_toc', 'tipue_search',
           'code_include', 'share_post', 'twitter_bootstrap_rst_directives']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
USE_SHORTCUT_ICONS = True

# Elegant Labels
SOCIAL_PROFILE_LABEL = 'Contacta conmigo'
RELATED_POSTS_LABEL = 'Continue leyendo'
SHARE_POST_INTRO = '¿Te gustó esta anotación? Compártela en:'
COMMENTS_INTRO = u'¿Qué te parece? ¿Piensas que olividé algo? ¿Poco claro? Deja abajo tus comentarios.'

# Mailchimp
# EMAIL_SUBSCRIPTION_LABEL = u'Get Monthly Updates'
# EMAIL_FIELD_PLACEHOLDER = u'Enter your email...'
# SUBSCRIBE_BUTTON_TITLE = u'Send me Free updates'
# MAILCHIMP_FORM_ACTION = u'empty'

# SMO
TWITTER_USERNAME = u'pcaro'
FEATURED_IMAGE = SITEURL + '/theme/images/apple-touch-icon-152x152.png'

SITESUBTITLE = 'Anotaciones'

# Legal
SITE_LICENSE = u'<span xmlns:dct="http://purl.org/dc/terms/" property="dct:title"> Anotaciones</span> de <a xmlns:cc="http://creativecommons.org/ns#" href="http://pablocaro.es" property="cc:attributionName" rel="cc:attributionURL">Pablo Caro</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.'

# SEO
SITE_DESCRIPTION = u'Mi nombre es Pablo Caro \u2015 un ingeniero de software. Soy pcaro en Github y en twitter. Construyo software de todo tipo. Este es mi blog personal.'

# Landing Page
PROJECTS = [
    {
        'name': 'trac2rst',
        'url':
            'https://github.com/pcaro/trac2rst',
            'description': 'I use trac2rst to help me in the task to pass'
            ' documentacion from trac to sphinx'},
    {
        'name': 'Openerp Snippets',
            'url':
            'https://github.com/pcaro/openerp-snippets',
            'description': 'A sublime package which includes a bunch of handy'
            ' snippets for doing OpenERp development'},
    {
        'name': 'Lynx Theme',
            'url':
            'https://github.com/pcaro/lynx-theme',
            'description': 'This is a theme for the Sphinx documentation generator'},
    {
        'name': 'Little Scripts',
            'url':
            'https://github.com/pcaro/little_scripts',
            'description': 'Little simple utilities or alias.'
            ' Most of them are not mine.'},
    {
        'name': 'dotfiles',
            'url': 'https://github.com/pcaro/dotfiles',
            'description': 'Configuration files.'
    }]

LANDING_PAGE_ABOUT = {'title': 'Construyendo sofware de forma innovadora',
                      'details': """<div itemscope itemtype="http://schema.org/Person">
       <p>Mi nombre es <span itemprop="name">Pablo Caro</span>.
       Soy <a href="https://github.com/pcaro/" title="Perfil en github" itemprop="url"><span itemprop="nickname">pcaro</span></a> en Github
       igual que en Twitter (<a href="https://twitter.com/pcaro/" title="Perfil en Twitter" itemprop="url">@pcaro</a>).
       Puedes contactar conmigo por <a href="mailto:correo@pablocaro.es" title="email" itemprop="email">email</a>.</p>

       <p>En este blog llamado <strong>Anotaciones</strong> voy apuntando las notas que
       no quiero que ocupen espacio en mi cabeza. Principalmente recetas de python y linux.</p>

       <p>Como desarrollador trabajo tanto para instuciones públicas como privadas, y
       no tengo problemas para habituarme a nuevos lenguajes o frameworks. Siempre me mantengo
       receptivo para trabajar con nuevas tecnologías. Ahora centrado en proyectos de acompañamiento tecnológico y
       growth hacking. A menudo colaboro con proyectos de sofware libre y siempre estoy dispuesto
       a predicar a favor del opensource.</p>

       <p>En la parte más personal soy un hombre felizmente casado con dos hijos maravillosos
       que vive en Sevilla aunque no leeras mucho de ellos por aquí ya que también resguardo mucho mi privacidad.</p>
       </div>"""}
