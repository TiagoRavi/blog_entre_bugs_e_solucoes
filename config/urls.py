from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView, RedirectView
from django.http import JsonResponse, HttpResponse
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.storage import staticfiles_storage
from pages.language import switch_language

from blog.sitemaps import (
    PostSitemap,
    CategorySitemap,
    EbookCategorySitemap,
    EbookSitemap,
    StaticPagesSitemap,
)

from config.tinymce_upload import tinymce_upload


# =========================================================
# HEALTHCHECK
# =========================================================

def healthcheck(_request):
    return JsonResponse({"status": "ok"})


# =========================================================
# INDEXNOW
# =========================================================

def indexnow_key(_request):
    return HttpResponse(
        "b7360389d77240f3940b63ae081517d9",
        content_type="text/plain",
    )


def ads_txt(_request):
    return HttpResponse(
        "google.com, pub-5960956644380983, DIRECT, f08c47fec0942fa0",
        content_type="text/plain",
    )


# =========================================================
# SITEMAPS
# =========================================================

sitemaps = {
    "posts": PostSitemap,
    "categories": CategorySitemap,
    "ebook_categories": EbookCategorySitemap,
    "ebooks": EbookSitemap,
    "static_pages": StaticPagesSitemap,
}


# =========================================================
# URLS SEM PREFIXO DE IDIOMA
# =========================================================

urlpatterns = [
    # ADMIN
    path("admin/", admin.site.urls),

    # INTERNACIONALIZAÇÃO
    path("i18n/switch/", switch_language, name="switch_language"),
    path("i18n/", include("django.conf.urls.i18n")),

    # HEALTHCHECK
    path("health/", healthcheck, name="healthcheck"),

    # INDEXNOW
    path(
        "b7360389d77240f3940b63ae081517d9.txt",
        indexnow_key,
        name="indexnow-key",
    ),

    # ADS.TXT
    path("ads.txt", ads_txt, name="ads-txt"),

    # ROBOTS
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain",
        ),
        name="robots-txt",
    ),

    # SITEMAP
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="sitemap",
    ),

    # TINYMCE
    path("tinymce/upload/", tinymce_upload, name="tinymce-upload"),
    path("tinymce/", include("tinymce.urls")),

    # EBOOKS E NEWSLETTER MANTIDOS SEM PREFIXO DE IDIOMA
    path("ebooks/", include("ebooks.urls")),
    path("newsletter/", include("newsletter.urls")),

    # FAVICON
    path(
        "favicon.ico",
        RedirectView.as_view(
            url=staticfiles_storage.url("favicon.ico"),
            permanent=True,
        ),
    ),
]


# =========================================================
# ROTAS PÚBLICAS
# =========================================================

# Páginas institucionais com caminhos explícitos por idioma
urlpatterns += [
    path("", include("pages.urls")),
]

# Blog internacionalizado:
# Português sem prefixo; inglês com /en/; espanhol com /es/
urlpatterns += i18n_patterns(
    path("", include("blog.urls")),
    prefix_default_language=False,
)


# =========================================================
# MEDIA FILES (DEV ONLY)
# =========================================================

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )


# =========================================================
# CUSTOM ERROR HANDLERS
# =========================================================

handler404 = "pages.views.handler404"
handler500 = "pages.views.handler500"
