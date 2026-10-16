from django.contrib.sitemaps import Sitemap

from .models import Post, Category
from ebooks.models import Ebook, EbookCategory
from django.urls import reverse

class PostSitemap(Sitemap):
    protocol = "https"
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Post.objects.published()

    def lastmod(self, obj):
        return obj.updated_at


class CategorySitemap(Sitemap):
    protocol = "https"
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Category.objects.all()


class EbookCategorySitemap(Sitemap):
    protocol = "https"
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return EbookCategory.objects.filter(
            is_active=True,
        )

    def lastmod(self, obj):
        return None


class EbookSitemap(Sitemap):
    protocol = "https"
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Ebook.objects.filter(
            is_published=True,
            category__is_active=True,
        ).select_related("category")

    def lastmod(self, obj):
        return obj.updated_at
class StaticPagesSitemap(Sitemap):
    protocol = "https"
    changefreq = "yearly"
    priority = 0.3

    def items(self):
        return [
            "pages:about",
            "pages:about_author",
            "pages:contact",
            "pages:privacy",
            "pages:terms",
            "pages:disclaimer",
        ]

    def location(self, item):
        return reverse(item)