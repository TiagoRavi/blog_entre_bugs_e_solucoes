from pathlib import Path
from os import getenv

# ======================================================
# BASE DIR
# ======================================================
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ======================================================
# CORE
# ======================================================
SECRET_KEY = getenv("DJANGO_SECRET_KEY")

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

    # Third-party
    "cloudinary",
    "cloudinary_storage",

    # Terceiros
    "tinymce",

    # Apps locais
    "blog.apps.BlogConfig",
    "pages",
]

SITE_ID = 2

SITE_URL = "https://entrebugsesolucoes.com.br"

# ======================================================
# MIDDLEWARE
# ======================================================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # WhiteNoise deve vir logo após SecurityMiddleware
    "whitenoise.middleware.WhiteNoiseMiddleware",

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
# TEMPLATES
# ======================================================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",

                "blog.context_processors.categories_menu",
                "blog.context_processors.seo",
            ],
        },
    },
]

# ======================================================
# PASSWORD VALIDATORS
# ======================================================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ======================================================
# I18N / TIMEZONE
# ======================================================
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# ======================================================
# STATIC FILES (WhiteNoise)
# ======================================================

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# ======================================================
# MEDIA / CLOUDINARY
# ======================================================

CLOUDINARY_URL = getenv("CLOUDINARY_URL")

STORAGES = {
    "default": {
        "BACKEND": (
            "cloudinary_storage.storage.MediaCloudinaryStorage"
            if CLOUDINARY_URL
            else "django.core.files.storage.FileSystemStorage"
        ),
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

if not CLOUDINARY_URL:
    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "media"

# ======================================================
# TinyMCE
# ======================================================

TINYMCE_DEFAULT_CONFIG = {
    "height": 550,
    "menubar": False,
    "branding": False,

    "plugins": (
        "advlist autolink lists link image charmap preview "
        "searchreplace visualblocks code fullscreen "
        "insertdatetime media table help wordcount"
    ),

    "toolbar": (
        "undo redo | formatselect | "
        "bold italic underline | "
        "alignleft aligncenter alignright | "
        "bullist numlist outdent indent | "
        "link image | code | removeformat"
    ),

    # Endpoint padrão do django-tinymce
    "images_upload_url": "/tinymce/upload/",

    # 🔐 Handler com CSRF
    "images_upload_handler": """
        function (blobInfo, progress) {
            return new Promise(function (resolve, reject) {
                const xhr = new XMLHttpRequest();
                xhr.withCredentials = true;
                xhr.open('POST', '/tinymce/upload/');

                // CSRF token do cookie
                const csrftoken = document.cookie
                    .split('; ')
                    .find(row => row.startsWith('csrftoken='))
                    ?.split('=')[1];

                xhr.setRequestHeader('X-CSRFToken', csrftoken);

                xhr.onload = function () {
                    if (xhr.status !== 200) {
                        reject('HTTP Error: ' + xhr.status);
                        return;
                    }

                    const json = JSON.parse(xhr.responseText);
                    if (!json || typeof json.location !== 'string') {
                        reject('Resposta inválida do servidor');
                        return;
                    }

                    resolve(json.location);
                };

                xhr.onerror = function () {
                    reject('Erro de rede');
                };

                const formData = new FormData();
                formData.append('file', blobInfo.blob(), blobInfo.filename());

                xhr.send(formData);
            });
        }
    """,

    "content_style": """
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto;
            font-size: 16px;
        }
        img { max-width: 100%; height: auto; }
    """,
}

MAX_UPLOAD_SIZE = 5 * 1024 * 1024

FILE_UPLOAD_MAX_MEMORY_SIZE = MAX_UPLOAD_SIZE
DATA_UPLOAD_MAX_MEMORY_SIZE = MAX_UPLOAD_SIZE

# ======================================================
# DEFAULTS
# ======================================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CSRF_COOKIE_HTTPONLY = True

SESSION_COOKIE_HTTPONLY = True

SECURE_CONTENT_TYPE_NOSNIFF = True


