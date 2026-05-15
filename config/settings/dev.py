from .base import *

# =========================================================
# DEBUG
# =========================================================

DEBUG = True

# =========================================================
# SECRET KEY
# =========================================================

SECRET_KEY = "dev-secret-key-insegura-apenas-local"

# =========================================================
# HOSTS
# =========================================================

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

# =========================================================
# SEGURANÇA (RELAXADA EM DEV)
# =========================================================

SECURE_SSL_REDIRECT = False

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# =========================================================
# DATABASE (SQLITE LOCAL)
# =========================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# =========================================================
# CACHE LOCAL
# =========================================================

CACHES = {
    "default": {
        "BACKEND": (
            "django.core.cache.backends.locmem.LocMemCache"
        ),
        "LOCATION": "blog-cache-dev",
    }
}

# =========================================================
# EMAIL BACKEND (DEV)
# =========================================================

EMAIL_BACKEND = (
    "django.core.mail.backends.console.EmailBackend"
)

# =========================================================
# STATIC / MEDIA LOCAL
# =========================================================

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# =========================================================
# LOGGING DEV
# =========================================================

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
        "level": "DEBUG",
    },
}

# =========================================================
# DJANGO DEBUG TOOLBAR (FUTURO)
# =========================================================

INTERNAL_IPS = [
    "127.0.0.1",
]

# =========================================================
# DEVELOPMENT FLAGS
# =========================================================

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]