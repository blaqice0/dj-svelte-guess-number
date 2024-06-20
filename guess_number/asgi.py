"""
ASGI config for guess_number project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from guess_number.settings import DEBUG

if DEBUG:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'guess_number.development.settings'
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'guess_number.production.settings')

application = get_asgi_application()
