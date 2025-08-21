#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = "http://pablocaro.es"
RELATIVE_URLS = False

# Following items are often useful when publishing

DISQUS_SITENAME = "anotaciones"
GOOGLE_ANALYTICS = "UA-60035125-1"

# Disable typogrify to avoid SyntaxWarnings in Python 3.13
TYPOGRIFY = False

# Fix FEATURED_IMAGE for production
FEATURED_IMAGE = SITEURL + "/theme/images/apple-touch-icon-152x152.png"

# Feeds
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"
CATEGORY_FEED_ATOM = "feeds/categories/{slug}.atom.xml"
CATEGORY_FEED_RSS = "feeds/categories/{slug}.rss.xml"
TAG_FEED_ATOM = "feeds/tags/{slug}.atom.xml"
TAG_FEED_RSS = "feeds/tags/{slug}.rss.xml"
