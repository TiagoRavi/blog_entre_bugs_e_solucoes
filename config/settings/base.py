from pathlib import Path
import os

# ======================================================
# BASE DIR
# ======================================================
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# ======================================================
# CORE
# ======================================================
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

DEBUG = False

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
# DATABASE
# ======================================================
DATABASES = {}


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

STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

# ======================================================
# MEDIA / CLOUDINARY (com fallback seguro)
# ======================================================

CLOUDINARY_URL = os.getenv("CLOUDINARY_URL")

if CLOUDINARY_URL:
    DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
else:
    # Fallback seguro para ambiente local / erro de config
    DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "media"


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

# ======================================================
# DEFAULTS
# ======================================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

