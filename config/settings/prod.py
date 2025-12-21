from .base import *
import os

# ======================================================
# CORE
# ======================================================
DEBUG = False

ALLOWED_HOSTS = os.environ.get(
    "DJANGO_ALLOWED_HOSTS", ""
).split(",")

# ======================================================
# SECURITY
# ======================================================

# Força HTTPS
SECURE_SSL_REDIRECT = True

# Cookies seguros (somente HTTPS)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HSTS — habilitar SOMENTE quando HTTPS estiver OK
SECURE_HSTS_SECONDS = 31536000  # 1 ano
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Headers de segurança
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = "DENY"

# CSRF Trusted Origins (vem do .env)
CSRF_TRUSTED_ORIGINS = os.environ.get(
    "DJANGO_CSRF_TRUSTED_ORIGINS", ""
).split(",")

# ======================================================
# CACHE (PROD)
# ======================================================
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": os.environ.get(
            "REDIS_URL",
            "redis://127.0.0.1:6379/1",
        ),
    }
}
