#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ashwin Kumar K'
SITENAME = u"Ashwin's Chronicles"
#SITEURL = 'https://ashwinschronicles.github.io/'

PATH = 'content'

TIMEZONE = 'Asia/Calcutta'
THEME = 'theme'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#FEED_ALL_RSS = 'feeds/all.rss.xml'
#AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
#RSS_FEED_SUMMARY_ONLY = False

STATIC_PATHS = ['images', 'pdfs','extra']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'custom.css'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/LICENSE': {'path': 'LICENSE'},
    'extra/README': {'path': 'README'},
}

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Git', 'https://github.com/iamashwin99/'),
          ('Git(old)', 'https://github.com/iamashwin26/'),
          ('Facebook', 'https://www.facebook.com/iamashwin99'),)

# clean urls for pages , trailing slash to support HTTPS
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
# clean urls for articles
ARTICLE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{slug}/'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PLUGIN_PATHS = ['/home/ashwin/Data/Downloads/website/plugins/']
PLUGINS = ['tipue_search' , 'pelican-toc','neighbors','render_math', 'sitemap']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))


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


#### render_math settings
MATH_JAX = {'color':'red','align':'centre','mathjax_font':'sanserif','linebreak_automatic':'True','tex_extensions': ['color.js','mhchem.js']}
