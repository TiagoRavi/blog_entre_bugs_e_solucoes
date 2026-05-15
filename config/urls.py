from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import (
    TemplateView,
    RedirectView,
)
from django.http import (
    JsonResponse,
    HttpResponse,
)
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.storage import (
    staticfiles_storage,
)

from blog.sitemaps import (
    PostSitemap,
    CategorySitemap,
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


# =========================================================
# SITEMAPS
# =========================================================

sitemaps = {
    "posts": PostSitemap,
    "categories": CategorySitemap,
}

# =========================================================
# URLS
# =========================================================

urlpatterns = [
    # -----------------------------------------------------
    # ADMIN
    # -----------------------------------------------------
    path("admin/", admin.site.urls),

    # -----------------------------------------------------
    # HEALTHCHECK
    # -----------------------------------------------------
    path(
        "health/",
        healthcheck,
        name="healthcheck",
    ),

    # -----------------------------------------------------
    # INDEXNOW
    # -----------------------------------------------------
    path(
        "b7360389d77240f3940b63ae081517d9.txt",
        indexnow_key,
        name="indexnow-key",
    ),

    # -----------------------------------------------------
    # ROBOTS
    # -----------------------------------------------------
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain",
        ),
        name="robots-txt",
    ),

    # -----------------------------------------------------
    # SITEMAP
    # -----------------------------------------------------
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="sitemap",
    ),

    # -----------------------------------------------------
    # TINYMCE
    # -----------------------------------------------------
    path(
        "tinymce/upload/",
        tinymce_upload,
        name="tinymce-upload",
    ),

    path(
        "tinymce/",
        include("tinymce.urls"),
    ),

    # -----------------------------------------------------
    # APPS
    # -----------------------------------------------------
    path(
        "",
        include("blog.urls"),
    ),

    path(
        "",
        include("pages.urls"),
    ),

    # -----------------------------------------------------
    # FAVICON
    # -----------------------------------------------------
    path(
        "favicon.ico",
        RedirectView.as_view(
            url=staticfiles_storage.url("favicon.ico"),
            permanent=True,
        ),
    ),
]

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