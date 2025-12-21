from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "")
ALLOWED_HOSTS = [host for host in ALLOWED_HOSTS.split(",") if host]

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = "DENY"

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

CSRF_TRUSTED_ORIGINS = os.environ.get(
    "DJANGO_CSRF_TRUSTED_ORIGINS", ""
)
CSRF_TRUSTED_ORIGINS = [
    origin for origin in CSRF_TRUSTED_ORIGINS.split(",") if origin
]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": os.environ.get(
            "REDIS_URL",
            "redis://127.0.0.1:6379/1",
        ),
    }
}
