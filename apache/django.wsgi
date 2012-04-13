#!/usr/bin/env python

import sys
import os

sys.path.append ("/var/www/django-lemonldap/")
os.environ['DJANGO_SETTINGS_MODULE'] = "lemonsso.settings"

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
