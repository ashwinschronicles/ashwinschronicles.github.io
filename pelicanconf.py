#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ashwin Kumar K'
SITENAME = u"""<span style="color:#329A97;">Ashwin's</span> <span style="color:purple">Chronicles</span> """
SITEURL = ''
#SITENAME = u"Ashwin's Chronicles"
#SITEURL = 'https://ashwinschronicles.github.io/'

PATH = 'content'

TIMEZONE = 'Asia/Calcutta'
DATE_FORMATS = {"en": "%b %d, %Y"}
THEME = 'theme'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
# Feeds
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None


STATIC_PATHS = ["theme/images", "images", "extra/_redirects", "code", "pdfs","extra"]

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'custom.css'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/LICENSE': {'path': 'LICENSE'},
    'extra/README': {'path': 'README'},
    'extra/utterances.json': {'path': 'utterances.json'}
}
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.admonition": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {"permalink": "True"},
    }
}

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Git', 'https://github.com/iamashwin99/'),
          ('Email', 'ashwinkumar.k.rao@gmail.com', 'My Email Address'),
          ('Git', 'https://github.com/iamashwin26/', "Old"),
          ("RSS", SITEURL + "/feeds/all.atom.xml"),
          ('Facebook', 'https://www.facebook.com/iamashwin99'),
          ('LinkedIn','https://www.linkedin.com/in/ashwin-k-4854b8121/'))

# Defaults
DEFAULT_CATEGORY = "Miscellaneous"
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = "{slug}"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"
TAGS_URL = "tags"
CATEGORIES_URL = "categories"
ARCHIVES_URL = "archives"
SEARCH_URL = "search"
TAG_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
USE_SHORTCUT_ICONS = True


TYPOGRIFY = True
DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PLUGIN_PATHS = ['/home/ashwin/Data/Sandbox/website/plugins/']

PLUGINS = ["tipue_search",
           "pelican-toc",
           "neighbors",
           "render_math", 
           "sitemap",
           "more_categories",
           "liquid_tags.include_code",
           "liquid_tags.img",
           "neighbors",
           "related_posts", 
           "share_post",
           "series", 
           "post_stats", 
           "pelican-js",
           "series",
#           "filetime_from_git",
           "extract_toc",
           "assets"]
DIRECT_TEMPLATES = ["index", "tags", "categories", "archives", "search", "404"]


SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}



#### render_math settings
#MATH_JAX = {'color':'red','align':'centre','mathjax_font':'sanserif','linebreak_automatic':'True','tex_extensions': ['color.js','mhchem.js']}
#MATH_JAX = {'color':'blue','align':'left',,'linebreak_automatic':'True','tex_extensions': ['color.js','mhchem.js']}
# Elegant Labels
SOCIAL_PROFILE_LABEL = "Stay in Touch"
RELATED_POSTS_LABEL = "Keep Reading"
SHARE_POST_INTRO = "Like this post? Share on:"
COMMENTS_INTRO = "So what do you think? Did I miss something? Is any part unclear? Leave your comments below."

# Email Subscriptions
EMAIL_SUBSCRIPTION_LABEL = "Get New Release Alert"
EMAIL_FIELD_PLACEHOLDER = "Enter your email..."
SUBSCRIBE_BUTTON_TITLE = "Notify me"

FREELISTS_NAME = "ashwinschronicles@freelists.org" # 203984577130
FREELISTS_FILTER = False

# SMO
TWITTER_USERNAME = "iamashwin99"
FEATURED_IMAGE = SITEURL + "/theme/images/final.png"

# Share links at bottom of articles
# Supported: twitter, facebook, hacker-news, reddit, linkedin, email
SHARE_LINKS = [("twitter", "Twitter"), ("facebook", "Facebook"),("reddit","Reddit"),("linkedin","LinkedIn"), ("email", "Email")]

# Legal
SITE_LICENSE = """All articles written by me in this website are licensed under <a rel="license" 
    href="http://creativecommons.org/licenses/by/4.0/">
    Creative Commons Attribution 4.0 International License</a>.""" 
    
# Landing Page
PROJECTS = [
  {
    'name': 'Cryostat Probe design and optimisation for transport measurement.',
    'url': 'https://ashwinschronicles.github.io/Cryostat-probe-design',
    'description': 'Design of a cryogenic probe for transport measurements and using it to observe Superconducting transition of Niobium Nitrate'
  },
  {
    'name': 'A review of Analog Discovery 2',
    'url': 'https://ashwinschronicles.github.io/analog-discovery-2-labview-home-bundle-review',
    'description': 'A review of Analog discovery 2 in a Lab environment'
  },
  {
    'name': 'A Beginers Guide to IoT',
    'url': 'https://ashwinschronicles.github.io/Intro-to-IoT',
    'description': 'An OTA controlled light'
  },
  {
    'name': 'A Pressure-sensitive mat',
    'url': 'https://ashwinschronicles.github.io/null',
    'description': 'Designed a pressure-sensitive mat that can sense touch enabling the determination of different poses such as Running, Jumping,Rightward-leftward movement,one-leg hop etc.'
  }
]


LANDING_PAGE_TITLE = "The Journey Begins"
# SEO
SITE_DESCRIPTION = u'Im Ashwin Kumar K,currently dual majoring in Physics and Electronics and Instrumentation from BITS Pilani Goa Campus. This is my personal blog.'


#MISC
DISQUS_FILTER = True
UTTERANCES_FILTER = False
COMMENTBOX_FILTER = True
APPLAUSE_BUTTON = True
