from .base import *

# ======================================================
# DEBUG
# ======================================================
DEBUG = True

# ======================================================
# HOSTS
# ======================================================
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

# ======================================================
# SEGURANÇA (RELAXADA APENAS EM DEV)
# ======================================================
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# ======================================================
# DATABASE (DEV)
# ======================================================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ======================================================
# CACHE (DEV)
# ======================================================
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "blog-cache-dev",
    }
}

# ======================================================
# LOGGING (DEV)
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
        "level": "DEBUG",
    },
}
