from django.contrib.sitemaps import Sitemap

from .models import Post, Category
from ebooks.models import Ebook, EbookCategory


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Post.objects.published()

    def lastmod(self, obj):
        return obj.updated_at


class CategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Category.objects.all()


class EbookCategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return EbookCategory.objects.filter(
            is_active=True,
        )

    def lastmod(self, obj):
        return None


class EbookSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Ebook.objects.filter(
            is_published=True,
            category__is_active=True,
        ).select_related("category")

    def lastmod(self, obj):
        return obj.updated_at