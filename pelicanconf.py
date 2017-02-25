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
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

# Blogroll
LINKS = None
#LINKS = (
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('atom feed', FEED_ALL_ATOM, 'rss'),
    ('github', 'http://github.com/pycnic'),
    ('docker', 'https://hub.docker.com/u/pycnic/'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DEFAULT_DATE = 'fs'

THEME = 'pelican-themes/pelican-bootstrap3'

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = [
    'liquid_tags.notebook',
    'related_posts',
    'series',
    'category_order',
    'render_math',
]

# pelican-bootstrap3 settings
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
PLUGINS += ['i18n_subsites']
PLUGIN_PATHS = ["pelican-plugins"]

BOOTSTRAP_THEME = 'darkly'
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True

GITHUB_USER = 'pycnic'
GITHUB_SHOW_USER_LINK = False

CC_LICENSE = 'CC-BY'
DISPLAY_TAGS_ON_SIDEBAR = True
PLUGINS += ['tag_cloud']
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True

PYGMENTS_STYLE = 'solarizeddark'

SHOW_SERIES = True
DISPLAY_SERIES_ON_SIDEBAR = True
