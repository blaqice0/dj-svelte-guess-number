"""
WSGI config for guess_number project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from guess_number.settings import DEBUG

if DEBUG:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'guess_number.development.settings'
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'guess_number.production.settings')

application = get_wsgi_application()
