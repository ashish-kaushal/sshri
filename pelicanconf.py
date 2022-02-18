#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'abodewithin'
SITEURL = 'abodewithin.com'
SITENAME = 'AbodeWithin'
SITELOGO = 'tales-logo.png'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'English'
THEME = 'themes/tales'
PATH = 'content'
STATIC_PATHS = ['pages', 'extra/robots.txt', 'extra/favicon.ico',]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

MAIN_STYLESHEET = 'styles-brightblue.css'

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

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/username'), ('Bitbucket', 'https://bitbucket.org/username'))

DEFAULT_PAGINATION = 4
SIDEBARMAIN = "sidebar_main.html"
SIDEBAR_ARTICLE = "sidebar_article.html"
LIKEUS = "social_likeus.html"
SHAREUS = "social_shareus.html"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False
DISPLAY_PAGES_ON_MENU = True

# plugins
PLUGIN_PATHS = ['plugins']
#PLUGINS = ['autostatic', 'advthumbnailer',]
PLUGINS = ['thumbnailer',]

# Summary plugin

SUMMARY_USE_FIRST_PARAGRAPH = True

# Thumbnailer plugin

IMAGE_PATH = 'photos'
THUMBNAIL_DIR = 'photos/thumbnails/'
THUMBNAIL_SIZES = {'thumb': '183x183', 'medium': '740x280'}
THUMBNAIL_KEEP_NAME = True

# ignore html files
READERS = {'html': None}
PAGE_PATHS = ['pages']
