from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap, CategorySitemap
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView
from config.tinymce_upload import tinymce_upload


urlpatterns = [
    path("admin/", admin.site.urls),

    # ✅ UPLOAD DO TINYMCE (CLOUDINARY)
    path("tinymce/upload/", tinymce_upload),

    path("", include("blog.urls")),
    path("", include("pages.urls")),

    # URLs internas do TinyMCE
    path("tinymce/", include("tinymce.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
