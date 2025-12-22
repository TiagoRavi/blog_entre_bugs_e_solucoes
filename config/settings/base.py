from pathlib import Path
import os

# ======================================================
# BASE DIR
# ======================================================
# BASE_DIR aponta para a raiz do projeto
# Ex: entre_bugs_e_solucoes/
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# ======================================================
# CORE
# ======================================================
# SECRET_KEY NÃO deve ter fallback aqui.
# - Em produção: deve vir obrigatoriamente do ambiente
# - Em desenvolvimento: será definido no dev.py
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# DEBUG deve ser controlado por ambiente
# Nunca habilitar DEBUG=True no base.py
DEBUG = False

# ALLOWED_HOSTS será definido por ambiente (dev / prod)
ALLOWED_HOSTS: list[str] = []


# ======================================================
# APPLICATIONS
# ======================================================
INSTALLED_APPS = [
    # Django core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",

    # Apps locais
    "blog",
    "pages",
]

# django.contrib.sites
SITE_ID = 1


# ======================================================
# MIDDLEWARE
# ======================================================
MIDDLEWARE = [
    # Segurança básica (headers, HTTPS, etc.)
    "django.middleware.security.SecurityMiddleware",

    # WhiteNoise DEVE vir logo após SecurityMiddleware
    # Responsável por servir arquivos estáticos em produção
    "whitenoise.middleware.WhiteNoiseMiddleware",

    # Sessões e middlewares padrão
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ======================================================
# URLS / WSGI
# ======================================================
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"


# ======================================================
# DATABASE
# ======================================================
# Banco de dados é definido por ambiente:
# - dev.py → sqlite
# - prod.py → Postgres / Render
DATABASES = {}


# ======================================================
# TEMPLATES
# ======================================================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        # Templates globais do projeto
        "DIRS": [BASE_DIR / "templates"],

        # Templates dentro dos apps
        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# ======================================================
# PASSWORD VALIDATORS
# ======================================================
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
    },
]


# ======================================================
# I18N / TIMEZONE
# ======================================================
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True


# ======================================================
# STATIC FILES
# ======================================================
STATIC_URL = "/static/"

# Diretório final coletado pelo collectstatic
STATIC_ROOT = BASE_DIR / "staticfiles"

# Diretórios locais de desenvolvimento
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# WhiteNoise: compressão + cache com hash
STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)


# ======================================================
# MEDIA FILES
# ======================================================
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# ======================================================
# DEFAULTS
# ======================================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
