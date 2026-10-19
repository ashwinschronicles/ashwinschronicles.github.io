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
                if not os.environ.get(_k):
                    os.environ[_k] = _v


def _get_env(*keys, default=None):
    for k in keys:
        v = os.environ.get(k)
        if v and v.strip():
            return v.strip()
    return default


sys.path.append(os.curdir)
from pelicanconf import *

# Context can be "production", "test", "development", or "branch-deploy"
CONTEXT = _get_env("CONTEXT", default="production").lower()

if CONTEXT == "production":
    SITEURL = "https://ashwinschronicles.github.io"
    FEED_DOMAIN = SITEURL
    FEED_ALL_ATOM = "feeds/all.atom.xml"
    CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
    CLAIM_GOOGLE = _get_env("CLAIM_GOOGLE_PROD", "CLAIM_GOOGLE")
    STAT_COUNTER_PROJECT = _get_env(
        "STAT_COUNTER_PROJECT_PROD", "STAT_COUNTER_PROJECT", "STATCOUNTER_PROJECT"
    )
    STAT_COUNTER_SECURITY = _get_env(
        "STAT_COUNTER_SECURITY_PROD", "STAT_COUNTER_SECURITY", "STATCOUNTER_SECURITY"
    )
    _ga_prod = _get_env(
        "MODERN_GOOGLE_ANALYTICS_PROD",
        "MODERN_GOOGLE_ANALYTICS",
        "GOOGLE_ANALYTICS_PROD",
        "GOOGLE_ANALYTICS",
    )
    if _ga_prod:
        if _ga_prod.startswith("G-"):
            MODERN_GOOGLE_ANALYTICS = _ga_prod
            GOOGLE_ANALYTICS = None
        else:
            GOOGLE_ANALYTICS = _ga_prod
            MODERN_GOOGLE_ANALYTICS = None
    DISQUS_SITENAME = _get_env("DISQUS_SITENAME")
    HEAP_ANALYTICS = _get_env("HEAP_ANALYTICS_PROD", "HEAP_ANALYTICS")
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
    STAT_COUNTER_PROJECT = _get_env(
        "STAT_COUNTER_PROJECT_TEST",
        "STAT_COUNTER_PROJECT_NEXT",
        "STAT_COUNTER_PROJECT",
        "STATCOUNTER_PROJECT",
    )
    STAT_COUNTER_SECURITY = _get_env(
        "STAT_COUNTER_SECURITY_TEST",
        "STAT_COUNTER_SECURITY_NEXT",
        "STAT_COUNTER_SECURITY",
        "STATCOUNTER_SECURITY",
    )
    _ga_test = _get_env(
        "MODERN_GOOGLE_ANALYTICS_TEST",
        "MODERN_GOOGLE_ANALYTICS_NEXT",
        "GOOGLE_ANALYTICS_TEST",
        "GOOGLE_ANALYTICS_NEXT",
        "MODERN_GOOGLE_ANALYTICS",
        "GOOGLE_ANALYTICS",
    )
    if _ga_test:
        if _ga_test.startswith("G-"):
            MODERN_GOOGLE_ANALYTICS = _ga_test
            GOOGLE_ANALYTICS = None
        else:
            GOOGLE_ANALYTICS = _ga_test
            MODERN_GOOGLE_ANALYTICS = None
    COMMENTBOX_PROJECT = _get_env("COMMENTBOX_PROJECT")
    HEAP_ANALYTICS = _get_env("HEAP_ANALYTICS_NEXT", "HEAP_ANALYTICS")

else:
    SITEURL = ""
    STAT_COUNTER_PROJECT = _get_env("STAT_COUNTER_PROJECT", "STATCOUNTER_PROJECT")
    STAT_COUNTER_SECURITY = _get_env("STAT_COUNTER_SECURITY", "STATCOUNTER_SECURITY")
    _ga_fallback = _get_env("MODERN_GOOGLE_ANALYTICS", "GOOGLE_ANALYTICS")
    if _ga_fallback:
        if _ga_fallback.startswith("G-"):
            MODERN_GOOGLE_ANALYTICS = _ga_fallback
            GOOGLE_ANALYTICS = None
        else:
            GOOGLE_ANALYTICS = _ga_fallback
            MODERN_GOOGLE_ANALYTICS = None

# Set aliases for themes using alternative Pelican naming conventions
STATCOUNTER_PROJECT = STAT_COUNTER_PROJECT
STATCOUNTER_SECURITY = STAT_COUNTER_SECURITY

MAILCHIMP_FORM_ACTION = os.environ.get("MAILCHIMP_FORM_ACTION")
UTTERANCES_REPO = "ashwinschronicles/ashwinschronicles.github.io"
UTTERANCES_LABEL = "💬Website-comments"

RELATIVE_URLS = False


DELETE_OUTPUT_DIRECTORY = True
