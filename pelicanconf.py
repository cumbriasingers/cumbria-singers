#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Cumbria Singers'
SITENAME = u'Cumbria Singers'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = u'en-gb'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
CATEGORY_URL = 'seasons/{slug}.html'
CATEGORY_SAVE_AS = 'seasons/{slug}.html'
CATEGORIES_SAVE_AS = 'seasons/index.html'
# We could also have this save over the archive, which could be quite elegant.
# ^^ Nope; Overwriting an existing page throws an error. Maybe better to chage the theme

MENUITEMS = (
    #('Current Season', 'https://colinbrislawn.github.io/CamerataMusica/seasons/current-season.html'),
)


# Blogroll
LINKS = (
# Absolute paths seem to work best
	#('Facebook', 'https://www.facebook.com/pages/cumbria-singers'),
	('Cumbria Rural Choirs', 'https://www.cumbria-rural-choirs.org.uk'),
	)

SIDEBAR_EMAIL_SIGNUP_URL = 'http://eepurl.com/'

# Social widget
SOCIAL = (
	('Facebook', 'https://www.facebook.com/pages/cumbria-singers'),
#	('Past Seasons', 'https://colinbrislawn.github.io/CamerataMusica/seasons/'),

#	('Origional Site','http:///www.cameratamusica.com'),
	)

DISPLAY_TAGS_ON_SIDEBAR = False
SIDEBAR_IMAGES = ["http://manifestimage.co.uk/cumbriasingers/images/cs3g.png"]
#SIDEBAR_CONSTANT_CONTACT = 'asdf'

NEWEST_FIRST_ARCHIVES = True
DEFAULT_PAGINATION = 10
#ARTICLE_ORDER_BY = 'date'
#ARTICLE_ORDER_BY = 'reversed-date'

PAGE_ORDER_BY = 'reversed-date'

# caching options 
CACHE_CONTENT = True
CHECK_MODIFIED_METHOD = 'mtime'
LOAD_CONTENT_CACHE = True
GZIP_CACHE = False


STATIC_PATHS = ['images', 'pages', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}


SUMMARY_MAX_LENGTH = 20

BANNER_ALL_PAGES = True
BANNER_SUBTITLE = 'making music together'
BANNER = '/images/DSF0118-large.jpg'
BANNER_LOGO = '/images/cs3banner1.png'

RELATIVE_URLS = True
THEME = "./pelican-bootstrap3"

PLUGIN_PATHS = ['../pelican-plugins']
