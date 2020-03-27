#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# Important: Changing SITEURL may break links in deploy-previews
if os.environ.get("CONTEXT") == "production":
    SITEURL = "https://ashwinschronicles.github.io"
    FEED_DOMAIN = SITEURL
    FEED_ALL_ATOM = "feeds/all.atom.xml"
    CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
    CLAIM_GOOGLE = os.environ.get("CLAIM_GOOGLE_PROD")
    STAT_COUNTER_PROJECT = os.environ.get("STAT_COUNTER_PROJECT_PROD")
    STAT_COUNTER_SECURITY = os.environ.get("STAT_COUNTER_SECURITY_PROD")
    GOOGLE_ANALYTICS = os.environ.get("GOOGLE_ANALYTICS_PROD")
    DISQUS_SITENAME = os.environ.get("DISQUS_SITENAME")
    HEAP_ANALYTICS = os.environ.get("HEAP_ANALYTICS_PROD")
#    COMMENTBOX_PROJECT = os.environ.get("COMMENTBOX_PROJECT")
# filetime_from_git is very slow. Use it in production only
# to avoid slow build times during development
    PLUGINS.append("filetime_from_git")
    PLUGINS.append("sitemap")

elif os.environ.get("CONTEXT") == "branch-deploy" and os.environ.get("HEAD") == "next":
    SITENAME = "Site (Next)"
    SITESUBTITLE = "Pre Release Documentation of The Best Pelican Theme"
    SITEURL = "https://ashwinschronicles.github.io"
    FEED_DOMAIN = SITEURL
    LANDING_PAGE_TITLE = "Elegant (Next) – Why it is the Best Pelican Theme"
    STAT_COUNTER_PROJECT = os.environ.get("STAT_COUNTER_PROJECT_NEXT")
    STAT_COUNTER_SECURITY = os.environ.get("STAT_COUNTER_SECURITY_NEXT")
    GOOGLE_ANALYTICS = os.environ.get("GOOGLE_ANALYTICS_NEXT")
    COMMENTBOX_PROJECT = os.environ.get("COMMENTBOX_PROJECT")
    HEAP_ANALYTICS = os.environ.get("HEAP_ANALYTICS_NEXT")

else:
    SITEURL = ""

MAILCHIMP_FORM_ACTION = os.environ.get("MAILCHIMP_FORM_ACTION")
UTTERANCES_REPO = "ashwinschronicles/ashwinschronicles.github.io"
UTTERANCES_LABEL = "💬Website-comments"

RELATIVE_URLS = False


DELETE_OUTPUT_DIRECTORY = True
