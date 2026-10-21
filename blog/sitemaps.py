
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import override

from .models import Post, PostTranslation, Category
from ebooks.models import Ebook, EbookCategory


class PostSitemap(Sitemap):
    protocol = "https"
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Post.objects.published()

    def lastmod(self, obj):
        return obj.updated_at


class PostTranslationSitemap(Sitemap):
    protocol = "https"
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return PostTranslation.objects.filter(
            post__status=Post.Status.PUBLISHED,
            post__published_at__lte=timezone.now(),
        ).select_related("post")

    def location(self, obj):
        with override(obj.language):
            return reverse(
                "blog:post_detail",
                kwargs={"slug": obj.slug},
            )

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
