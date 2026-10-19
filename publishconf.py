#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

# Automatically load .env file if present
_env_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(_env_path):
    with open(_env_path, "r", encoding="utf-8") as _f:
        for _line in _f:
            _line = _line.strip()
            if _line and not _line.startswith("#") and "=" in _line:
                _k, _v = _line.split("=", 1)
                _k = _k.strip()
                _v = _v.strip().strip("'\"")
                os.environ.setdefault(_k, _v)

sys.path.append(os.curdir)
from pelicanconf import *

# Context can be "production", "test", "development", or "branch-deploy"
CONTEXT = os.environ.get("CONTEXT", "production").lower()

if CONTEXT == "production":
    SITEURL = "https://ashwinschronicles.github.io"
    FEED_DOMAIN = SITEURL
    FEED_ALL_ATOM = "feeds/all.atom.xml"
    CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
    CLAIM_GOOGLE = os.environ.get("CLAIM_GOOGLE_PROD") or os.environ.get("CLAIM_GOOGLE")
    STAT_COUNTER_PROJECT = (
        os.environ.get("STAT_COUNTER_PROJECT_PROD")
        or os.environ.get("STAT_COUNTER_PROJECT")
        or os.environ.get("STATCOUNTER_PROJECT")
    )
    STAT_COUNTER_SECURITY = (
        os.environ.get("STAT_COUNTER_SECURITY_PROD")
        or os.environ.get("STAT_COUNTER_SECURITY")
        or os.environ.get("STATCOUNTER_SECURITY")
    )
    GOOGLE_ANALYTICS = os.environ.get("GOOGLE_ANALYTICS_PROD") or os.environ.get("GOOGLE_ANALYTICS")
    DISQUS_SITENAME = os.environ.get("DISQUS_SITENAME")
    HEAP_ANALYTICS = os.environ.get("HEAP_ANALYTICS_PROD") or os.environ.get("HEAP_ANALYTICS")
#    COMMENTBOX_PROJECT = os.environ.get("COMMENTBOX_PROJECT")
# filetime_from_git is very slow. Use it in production only
# to avoid slow build times during development
    if "filetime_from_git" not in PLUGINS:
        PLUGINS.append("filetime_from_git")
    if "sitemap" not in PLUGINS:
        PLUGINS.append("sitemap")

elif CONTEXT in ("test", "development", "branch-deploy") or (CONTEXT == "branch-deploy" and os.environ.get("HEAD") == "next"):
    SITENAME = "Ashwin's Chronicles (Test)" if CONTEXT in ("test", "development") else "Site (Next)"
    SITESUBTITLE = "Pre Release Documentation / Test Environment"
    SITEURL = os.environ.get("SITEURL_TEST", "https://ashwinschronicles.github.io")
    FEED_DOMAIN = SITEURL
    LANDING_PAGE_TITLE = "The Journey Begins (Test)"
    STAT_COUNTER_PROJECT = (
        os.environ.get("STAT_COUNTER_PROJECT_TEST")
        or os.environ.get("STAT_COUNTER_PROJECT_NEXT")
        or os.environ.get("STAT_COUNTER_PROJECT")
        or os.environ.get("STATCOUNTER_PROJECT")
    )
    STAT_COUNTER_SECURITY = (
        os.environ.get("STAT_COUNTER_SECURITY_TEST")
        or os.environ.get("STAT_COUNTER_SECURITY_NEXT")
        or os.environ.get("STAT_COUNTER_SECURITY")
        or os.environ.get("STATCOUNTER_SECURITY")
    )
    GOOGLE_ANALYTICS = (
        os.environ.get("GOOGLE_ANALYTICS_TEST")
        or os.environ.get("GOOGLE_ANALYTICS_NEXT")
        or os.environ.get("GOOGLE_ANALYTICS")
    )
    COMMENTBOX_PROJECT = os.environ.get("COMMENTBOX_PROJECT")
    HEAP_ANALYTICS = os.environ.get("HEAP_ANALYTICS_NEXT") or os.environ.get("HEAP_ANALYTICS")

else:
    SITEURL = ""
    STAT_COUNTER_PROJECT = os.environ.get("STAT_COUNTER_PROJECT") or os.environ.get("STATCOUNTER_PROJECT")
    STAT_COUNTER_SECURITY = os.environ.get("STAT_COUNTER_SECURITY") or os.environ.get("STATCOUNTER_SECURITY")
    GOOGLE_ANALYTICS = os.environ.get("GOOGLE_ANALYTICS")

# Set aliases for themes using alternative Pelican naming conventions
STATCOUNTER_PROJECT = STAT_COUNTER_PROJECT
STATCOUNTER_SECURITY = STAT_COUNTER_SECURITY

MAILCHIMP_FORM_ACTION = os.environ.get("MAILCHIMP_FORM_ACTION")
UTTERANCES_REPO = "ashwinschronicles/ashwinschronicles.github.io"
UTTERANCES_LABEL = "💬Website-comments"

RELATIVE_URLS = False


DELETE_OUTPUT_DIRECTORY = True
