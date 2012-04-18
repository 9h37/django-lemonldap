#!/usr/bin/env python

from distutils.core import setup

import os
import glob

def tree(path):
    files = []

    for f in glob.iglob(path + '/*'):
        if os.path.isdir(f):
            files = files + tree(f)
        else:
            files.append(f)

    return files


setup(
    name='Django-LemonLDAP',
    version='0.1',
    description='LemonLDAP authentication with Django',
    license='MIT',
    author='David Delassus',
    author_email='david.jose.delassus@gmail.com',
    url='http://github.com/9h37/django-lemonldap',

    packages = ['django_lemonldap.lemonsso.auth'],

    data_files=[
        ('share/django-lemonldap/apache/', [
            'django_lemonldap/apache/__init__.py',
            'django_lemonldap/apache/django.wsgi',
        ]),

        ('share/django-lemonldap/lemonsso/', [
            'django_lemonldap/lemonsso/__init__.py',
            'django_lemonldap/lemonsso/manage.py',
            'django_lemonldap/lemonsso/settings.py',
            'django_lemonldap/lemonsso/urls.py',
            'django_lemonldap/lemonsso/views.py',
        ]),

        ('share/django-lemonldap/lemonsso/auth/', [
            'django_lemonldap/lemonsso/auth/__init__.py',
            'django_lemonldap/lemonsso/auth/backends.py',
            'django_lemonldap/lemonsso/auth/middleware.py',
        ]),

        ('share/django-lemonldap/lemonsso/media/', [
            'django_lemonldap/lemonsso/media/index.html',
        ]),

        ('share/django-lemonldap/lemonsso/templates/', [
            'django_lemonldap/lemonsso/templates/test.html'
        ]),
    ]
)
