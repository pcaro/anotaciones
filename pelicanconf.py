#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Pablo Caro"
SITENAME = "Anotaciones por Pablo Caro"
SITEURL = ""  # Empty for development, set in publishconf.py for production

ARTICLE_PATH = "articles/"
PATH = "content"
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git", ".gitignore", "README.rst", "CNAME", "robots.txt"]
STATIC_PATHS = ["theme/images", "images", "extras"]
EXTRA_PATH_METADATA = {
    "extras/CNAME": {"path": "CNAME"},
    "extras/robots.txt": {"path": "robots.txt"},
    "extras/README.rst": {"path": "README.rst"},
}


TIMEZONE = "Europe/Paris"
# DISQUS_SITENAME = 'anotaciones'  # Disabled in development - only works in production

DEFAULT_LANG = "es"

# Manual Spanish translations for Elegant theme
# (Alternative to i18n_subsites plugin which has compatibility issues)

DEFAULT_CATEGORY = "Miscellaneous"
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = "{slug}"
ARTICLE_SAVE_AS = "{slug}.html"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("@pcaro at X.com", "http://x.com/pcaro"),
    ("Linkedin", "https://www.linkedin.com/in/pcarorevuelta/"),
    ("Python.org", "http://python.org/"),
    ("Jinja2", "http://jinja.pocoo.org/"),
)

GITHUB_URL = "http://github.com/pcaro"
TWITTER_USERNAME = "pcaro"
# Social
SOCIAL = (
    ("Twitter", "http://twitter.com/pcaro"),
    ("Github", GITHUB_URL),
    ("Linkedin", "https://www.linkedin.com/in/pcarorevuelta"),
    ("Facebook", "https://www.facebook.com/pablo.carorevuelta"),
    ("Email", "mailto:correo@pablocaro.es"),
)

DEFAULT_PAGINATION = 5

PLUGIN_PATHS = ["plugins"]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# THEME = 'pelican-themes/mg'
# THEME = 'pelican-themes/Just-Read'  # Un buen punto de partida. Necesita cosas de elegant
# THEME = 'pelican-themes/svbhack'
THEME = "themes/Flex"
THEME_TEMPLATES_OVERRIDES = ["themes/custom/templates"]

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

# THEME settings
TYPOGRIFY = True
DEFAULT_PAGINATION = False

PLUGINS = [
    "sitemap",
    "neighbors",
    "related_posts",
    "search",
    "i18n_subsites",
]

# I18N
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
I18N_TEMPLATES_LANG = "en"
I18N_UNTRANSLATED_ARTICLES = "remove"
I18N_UNTRANSLATED_PAGES = "remove"
I18N_SUBSITES = {
    "en": {
        "SITENAME": "Annotations by Pablo Caro",
        "SITESUBTITLE": "Annotations",
        "LOCALE": "en_US.UTF-8",
        "THEME_STATIC_DIR": "theme",
        "THEME_STATIC_PATHS": ["static"],
        "MENUITEMS": (
            ("Archives", "/en/archives.html"),
            ("Categories", "/en/categories.html"),
            ("Tags", "/en/tags.html"),
            ("Search", "/en/search.html"),
            ("Español", "/"),
        ),
        "SITESUBTITLE": "Annotations",
        "SITE_DESCRIPTION": "My name is Pablo Caro — a software engineer. I am pcaro on Github and twitter. I build software of all kinds. This is my personal blog.",
        "LANDING_PAGE_ABOUT": {
            "title": "Building software innovatively",
            "details": """<div itemscope itemtype="http://schema.org/Person">
       <p>My name is <span itemprop="name">Pablo Caro</span>.
       I am <a href="https://github.com/pcaro/" title="Github profile" itemprop="url"><span itemprop="nickname">pcaro</span></a> on Github
       as well as on Twitter (<a href="https://twitter.com/pcaro/" title="Twitter profile" itemprop="url">@pcaro</a>).
       You can contact me via <a href="mailto:correo@pablocaro.es" title="email" itemprop="email">email</a>.</p>

       <p>In this blog called <strong>Annotations</strong> I write down notes that
       I don't want to occupy space in my head. Mainly Python and Linux recipes.</p>

       <p>As a developer I work for both public and private institutions, and
       I have no problem getting used to new languages or frameworks. I always keep
       receptive to working with new technologies. Now focused on technology accompaniment projects and
       growth hacking. I often collaborate with open source software projects and I am always willing
       to preach in favor of opensource.</p>

       <p>On the more personal side I am a happily married man with two wonderful children
       living in Seville although you won't read much about them here as I also guard my privacy very much.</p>
       </div>""",
        },
    }
}

STORK_VERSION = "1.6.0"

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.toc": {"permalink": True},
    },
    "output_format": "html5",
}
DIRECT_TEMPLATES = ["index", "tags", "categories", "archives", "search"]

# Enable tag and category pages for Flex
TAG_SAVE_AS = "tag/{slug}.html"
TAG_URL = "tag/{slug}.html"
TAGS_SAVE_AS = "tags.html"
TAGS_URL = "tags.html"

CATEGORY_SAVE_AS = "category/{slug}.html"
CATEGORY_URL = "category/{slug}.html"
CATEGORIES_SAVE_AS = "categories.html"
CATEGORIES_URL = "categories.html"

AUTHOR_SAVE_AS = ""
USE_SHORTCUT_ICONS = True

# Flex theme configuration
SITETITLE = "Anotaciones"
SITELOGO = "/theme/img/profile.png"  # Optional: add a logo image
FAVICON = "/theme/img/favicon.ico"  # Optional: add a favicon

# Browser tab title
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "github"

# Footer
COPYRIGHT_YEAR = 2025
CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "3.0",
    "slug": "by-sa",
}

# Flex theme menu
MAIN_MENU = True
MENUITEMS = (
    ("Archivo", "/archives.html"),
    ("Categorías", "/categories.html"),
    ("Etiquetas", "/tags.html"),
    ("Búsqueda", "/search.html"),
    ("English", "/en/"),
)

# Mailchimp
# EMAIL_SUBSCRIPTION_LABEL = u'Get Monthly Updates'
# EMAIL_FIELD_PLACEHOLDER = u'Enter your email...'
# SUBSCRIBE_BUTTON_TITLE = u'Send me Free updates'
# MAILCHIMP_FORM_ACTION = u'empty'

# SMO
TWITTER_USERNAME = "pcaro"
# FEATURED_IMAGE defined in publishconf.py for production

SITESUBTITLE = "Anotaciones"

# Legal
SITE_LICENSE = '<span xmlns:dct="http://purl.org/dc/terms/" property="dct:title"> Anotaciones</span> de <a xmlns:cc="http://creativecommons.org/ns#" href="http://pablocaro.es" property="cc:attributionName" rel="cc:attributionURL">Pablo Caro</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.'

# SEO
SITE_DESCRIPTION = "Mi nombre es Pablo Caro — un ingeniero de software. Soy pcaro en Github y en twitter. Construyo software de todo tipo. Este es mi blog personal."

# Landing Page
PROJECTS = [
    {
        "name": "trac2rst",
        "url": "https://github.com/pcaro/trac2rst",
        "description": "I use trac2rst to help me in the task to pass"
        " documentacion from trac to sphinx",
    },
    {
        "name": "Openerp Snippets",
        "url": "https://github.com/pcaro/openerp-snippets",
        "description": "A sublime package which includes a bunch of handy"
        " snippets for doing OpenERp development",
    },
    {
        "name": "Lynx Theme",
        "url": "https://github.com/pcaro/lynx-theme",
        "description": "This is a theme for the Sphinx documentation generator",
    },
    {
        "name": "Little Scripts",
        "url": "https://github.com/pcaro/little_scripts",
        "description": "Little simple utilities or alias. Most of them are not mine.",
    },
    {
        "name": "dotfiles",
        "url": "https://github.com/pcaro/dotfiles",
        "description": "Configuration files.",
    },
]

LANDING_PAGE_ABOUT = {
    "title": "Construyendo sofware de forma innovadora",
    "details": """<div itemscope itemtype="http://schema.org/Person">
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
       </div>""",
}

# Trigger rebuild
