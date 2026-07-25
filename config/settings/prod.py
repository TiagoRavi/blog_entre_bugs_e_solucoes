from dotenv import load_dotenv
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / ".env")

from .base import *

import os
import logging
import dj_database_url
import cloudinary

# ======================================================
# LOGGING
# ======================================================

logging.basicConfig(level=logging.INFO)

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
    raise RuntimeError(
        "DJANGO_ALLOWED_HOSTS não configurado corretamente"
    )

# ======================================================
# SECURITY
# ======================================================

SECURE_SSL_REDIRECT = True

SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https",
)

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SESSION_COOKIE_HTTPONLY = True

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = "DENY"

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.environ.get(
        "DJANGO_CSRF_TRUSTED_ORIGINS",
        "",
    ).split(",")
    if origin.strip()
]

if not CSRF_TRUSTED_ORIGINS:
    raise RuntimeError(
        "DJANGO_CSRF_TRUSTED_ORIGINS não configurado corretamente"
    )

# ======================================================
# DATABASE
# ======================================================

DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL não configurada")

DATABASES = {
    "default": dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=600,
        ssl_require=False,  # True se o provedor exigir SSL
    )
}

# ======================================================
# CACHE
# ======================================================

REDIS_URL = os.environ.get("REDIS_URL")

if REDIS_URL:
    CACHES = {
        "default": {
            "BACKEND": (
                "django.core.cache.backends.redis.RedisCache"
            ),
            "LOCATION": REDIS_URL,
        }
    }
else:
    CACHES = {
        "default": {
            "BACKEND": (
                "django.core.cache.backends.locmem.LocMemCache"
            ),
            "LOCATION": "fallback-cache",
        }
    }

# ======================================================
# CLOUDINARY
# ======================================================

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": os.getenv("CLOUDINARY_API_KEY"),
    "API_SECRET": os.getenv("CLOUDINARY_API_SECRET"),
    "SECURE": True,
}

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True,
)

CLOUDINARY_URL = (
    f"cloudinary://{os.getenv('CLOUDINARY_API_KEY')}:"
    f"{os.getenv('CLOUDINARY_API_SECRET')}@"
    f"{os.getenv('CLOUDINARY_CLOUD_NAME')}?secure=true"
)

DEFAULT_FILE_STORAGE = (
    "cloudinary_storage.storage.MediaCloudinaryStorage"
)

# ======================================================
# STATIC FILES
# ======================================================

STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

# ======================================================
# LOGGING DJANGO
# ======================================================

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}
