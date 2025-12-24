from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.contrib.sitemaps.views import sitemap
from django.views.generic import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

from blog.sitemaps import PostSitemap, CategorySitemap
from config.tinymce_upload import tinymce_upload


# ---------------------------------------------------------------------
# Healthcheck simples para monitoramento (uptime / load balancer)
# ---------------------------------------------------------------------
def healthcheck(_request):
    return JsonResponse({"status": "ok"})


# ---------------------------------------------------------------------
# Sitemap configuration
# ---------------------------------------------------------------------
sitemaps = {
    "posts": PostSitemap,
    "categories": CategorySitemap,
}


# ---------------------------------------------------------------------
# URL patterns
# ---------------------------------------------------------------------
urlpatterns = [
    # Admin Django
    path("admin/", admin.site.urls),

    # Robots.txt (SEO crítico)
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain",
        ),
    ),

    # Sitemap XML
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="sitemap",
    ),

    # Healthcheck (monitoramento)
    path("health/", healthcheck),

    # Upload do TinyMCE (Cloudinary)
    path("tinymce/upload/", tinymce_upload),

    # URLs internas do TinyMCE
    path("tinymce/", include("tinymce.urls")),

    # Apps principais
    path("", include("blog.urls")),
    path("", include("pages.urls")),

    # Fivicon
    path(
    "favicon.ico",
    RedirectView.as_view(
        url=staticfiles_storage.url("favicon.ico"),
        permanent=True,
    ),
),
]


# ---------------------------------------------------------------------
# Media files apenas em ambiente de desenvolvimento
# ---------------------------------------------------------------------
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
