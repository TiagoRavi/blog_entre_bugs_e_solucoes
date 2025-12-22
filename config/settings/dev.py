from .base import *

# =========================================================
# DEBUG
# =========================================================
DEBUG = True


# =========================================================
# SECRET KEY (APENAS PARA DESENVOLVIMENTO)
# =========================================================
SECRET_KEY = "dev-secret-key-insegura-apenas-local"


# =========================================================
# HOSTS
# =========================================================
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


# =========================================================
# SEGURANÇA (RELAXADA EM DEV)
# =========================================================
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False


# =========================================================
# CACHE (LOCAL)
# =========================================================
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "blog-cache-dev",
    }
}


# =========================================================
# DATABASE (SQLITE LOCAL)
# =========================================================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
