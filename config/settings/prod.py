from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / ".env")

from .base import *

import os
<<<<<<< HEAD
import dj_database_url
=======
import logging
import dj_database_url

# ======================================================
# LOGGING
# ======================================================

logging.basicConfig(level=logging.INFO)
>>>>>>> develop

# ======================================================
# CORE
# ======================================================

DEBUG = False

# ======================================================
# HOSTS
# ======================================================
<<<<<<< HEAD
=======

>>>>>>> develop
ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")
    if host.strip()
]

if not ALLOWED_HOSTS:
<<<<<<< HEAD
    raise RuntimeError("DJANGO_ALLOWED_HOSTS não configurado")
=======
    raise RuntimeError(
        "DJANGO_ALLOWED_HOSTS não configurado corretamente"
    )
>>>>>>> develop

# ======================================================
# SECURITY
# ======================================================
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https",
)

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

<<<<<<< HEAD
SECURE_HSTS_SECONDS = 31536000  # 1 ano
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
REFERRER_POLICY = "strict-origin-when-cross-origin"

CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.environ.get("DJANGO_CSRF_TRUSTED_ORIGINS", "").split(",")
    if origin.strip()
]

if not CSRF_TRUSTED_ORIGINS:
    raise RuntimeError("DJANGO_CSRF_TRUSTED_ORIGINS não configurado")

# ======================================================
# DATABASE (PostgreSQL - Render)
# ======================================================
=======
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

>>>>>>> develop
DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL não configurada")

DATABASES = {
<<<<<<< HEAD
    "default": dj_database_url.parse(
        DATABASE_URL,
        conn_max_age=600,
        ssl_require=True,
=======
    "default": dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=600,
        ssl_require=False,
>>>>>>> develop
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
    # Fallback seguro para Render Free
    CACHES = {
        "default": {
            "BACKEND": (
                "django.core.cache.backends.locmem.LocMemCache"
            ),
            "LOCATION": "fallback-cache",
        }
    }

# ======================================================
<<<<<<< HEAD
# LOGGING (PRODUÇÃO)
# ======================================================
=======
# CLOUDINARY
# ======================================================

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": os.getenv("CLOUDINARY_API_KEY"),
    "API_SECRET": os.getenv("CLOUDINARY_API_SECRET"),
    "SECURE": True,
}

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

>>>>>>> develop
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
<<<<<<< HEAD
        "level": "ERROR",
=======
        "level": "INFO",
>>>>>>> develop
    },
}
