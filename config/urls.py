from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap, CategorySitemap
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("blog.urls")),
    path("", include("pages.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )

sitemaps = {
    "posts": PostSitemap,
    "categories": CategorySitemap,
}

urlpatterns += [
    path(
        "sitemap.xml",
        cache_page(60 * 60 * 12)(sitemap),
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

urlpatterns += [
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain",
        ),
    ),
]