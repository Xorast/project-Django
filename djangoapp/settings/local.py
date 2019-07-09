import os
from .base import *


SECRET_KEY = 'luf*lin!+xg$hf2z-m*c9b)kaamk3xm$+xf@5@dxc3tw!t31mt'

DEBUG = True

ALLOWED_HOSTS = ['project-django-pangur.c9users.io']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')