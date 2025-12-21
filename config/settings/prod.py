from .base import *
import os
import logging

# ======================================================
# LOGGING (TEMPORÁRIO PARA DEBUG NO RENDER)
# ======================================================
logging.basicConfig(level=logging.DEBUG)

# ======================================================
# CORE
# ======================================================
DEBUG = False

# ======================================================
# HOSTS
# ======================================================
ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")
    if host.strip()
]

if not ALLOWED_HOSTS:
    raise RuntimeError("DJANGO_ALLOWED_HOSTS não configurado corretamente")

# ======================================================
# SECURITY
# ======================================================
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.environ.get("DJANGO_CSRF_TRUSTED_ORIGINS", "").split(",")
    if origin.strip()
]

if not CSRF_TRUSTED_ORIGINS:
    raise RuntimeError("DJANGO_CSRF_TRUSTED_ORIGINS não configurado corretamente")

# ======================================================
# CACHE
# ======================================================
REDIS_URL = os.environ.get("REDIS_URL")

if REDIS_URL:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": REDIS_URL,
        }
    }
else:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": "render-fallback-cache",
        }
    }
