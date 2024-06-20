import os
from guess_number.settings import *


# This settings should be adjust to production environment
# Current settings here are just temporary

DEBUG = False

ALLOWED_HOSTS = ["*"]

CORS_ALLOW_ALL_ORIGINS = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATIC_URL = '/assets/'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
