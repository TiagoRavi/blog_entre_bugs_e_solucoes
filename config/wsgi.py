"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named
``application``.

For more information:
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# ======================================================
# DJANGO SETTINGS
# ======================================================

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings.prod",
)

# ======================================================
# WSGI APPLICATION
# ======================================================

application = get_wsgi_application()