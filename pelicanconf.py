#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ashwin Kumar K'
SITENAME = u"""<span style="color:#329A97;">Ashwin's</span> <span style="color:purple">Chronicles</span> """
SITEURL = '/'
#SITENAME = u"Ashwin's Chronicles"
#SITEURL = 'https://ashwinschronicles.github.io/'

PATH = 'content'

TIMEZONE = 'Asia/Calcutta'
THEME = 'theme'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
# Feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
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

TYPOGRIFY = False
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PLUGIN_PATHS = ['/home/ashwin/Data/Downloads/website/plugins/']
PLUGINS = ['tipue_search' , 'pelican-toc','neighbors','render_math', 'sitemap','more_categories','liquid_tags.img','neighbors', 'related_posts', 'share_post',
           'series']
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

# Elegant Labels
SOCIAL_PROFILE_LABEL = u'Stay in Touch'
RELATED_POSTS_LABEL = 'Keep Reading'
SHARE_POST_INTRO = 'Like this post? Share on:'
COMMENTS_INTRO = u'So what do you think? Did I miss something? Is any part unclear? Leave your comments below.'

# Mailchimp
EMAIL_SUBSCRIPTION_LABEL = u'Get Monthly Updates'
EMAIL_FIELD_PLACEHOLDER = u'Enter your email...'
SUBSCRIBE_BUTTON_TITLE = u'Send me Free updates'
MAILCHIMP_FORM_ACTION = u'empty'

# Legal
SITE_LICENSE = """All articles written by me in this weebsite are licensed under a <a rel="license" 
    href="http://creativecommons.org/licenses/by/4.0/">
    Creative Commons Attribution 4.0 International License</a>.""" 
    
# Landing Page
PROJECTS = [{'name': 'New', 'url': 'new',
             'description': 'More comming up'}]

LANDING_PAGE_ABOUT = {'title': 'The Journey Begins',
                      'details': """<p>Thanks for joining me!</p>
<p>I am Ashwin Kumar K, a Dual Degree BE &ndash; Int. MSc Physics at BITS Pilani KK Birla Goa campus (Batch of 2017).</p>
<p>This is the first post of this site where I intend to post some of my works related to the field of Science and Engineering.</p>
<p>I had always wanted to publish some of my projects and experiments on a public platform so that people working on similar projects can give and take ideas. It also serves as a way to showcase the experience that I have gained while doing such projects.</p>
<p>I intend to post details of projects or experiments that I have performed mostly in the field of Science and Engineering as I complete them.</p>
<p>Take a trip down my memory lane. I hope to see you around!</p>
<p><a href="https://ashwinschronicles.github.io/pdfs/Academic_CV.pdf">Here is my CV :</a></p>"""}


# SEO
SITE_DESCRIPTION = u'Im Ashwin Kumar K,currently dual majouring in Physics and Electronics and Instrumentation from BITS Pilani Goa Campus. This is my personal blog.'
