#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'pycnic'
SITENAME = 'The Pycnic'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = None
#LINKS = (
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = None
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DEFAULT_DATE = 'fs'

THEME = 'pelican-themes/pelican-bootstrap3'

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ['liquid_tags.notebook', 'related_posts', 'series']

# pelican-bootstrap3 settings
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
PLUGINS += ['i18n_subsites']
PLUGIN_PATHS = ["pelican-plugins"]

BOOTSTRAP_THEME = 'darkly'
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True

GITHUB_USER = 'pycnic'
GITHUB_SHOW_USER_LINK = True

CC_LICENSE = 'CC-BY'
DISPLAY_TAGS_ON_SIDEBAR = True
PLUGINS += ['tag_cloud']
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True

PYGMENTS_STYLE = 'solarizeddark'
