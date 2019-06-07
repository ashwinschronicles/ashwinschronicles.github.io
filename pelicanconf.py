#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ashwin Kumar K'
SITENAME = u"Ashwin's Chronicles"
#SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Calcutta'
THEME = 'theme'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#FEED_ALL_RSS = 'feeds/all.rss.xml'
#AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
#RSS_FEED_SUMMARY_ONLY = False

STATIC_PATHS = ['images']
# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Git', 'https://github.com/iamashwin99/'),
          ('Git(old)', 'https://github.com/iamashwin26/'),
          ('Facebook', 'https://www.facebook.com/iamashwin99'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PLUGIN_PATHS = ['/home/ashwin/Data/Downloads/website/plugins/']
PLUGINS = ['tipue_search' , 'extract_toc','extract_toc','neighbors',"render_math", 'sitemap']
