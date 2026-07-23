from django.test import TestCase, override_settings
from django.utils import timezone
from django.contrib.sites.models import Site, SITE_CACHE

from blog.models import Post, Category


@override_settings(SITE_ID=1)
class SitemapTest(TestCase):
    def setUp(self):
        # ==================================================
        # LIMPA CACHE INTERNO DO DJANGO SITES
        # ==================================================
        SITE_CACHE.clear()

        # ==================================================
        # GARANTE ESTADO LIMPO NO BANCO
        # ==================================================
        Site.objects.all().delete()
        Site.objects.create(
            id=1,
            domain="example.com",
            name="Example Site",
        )

        self.category = Category.objects.create(name="SEO")

        self.post = Post.objects.create(
            title="Post Indexado",
            content="Conteúdo",
            category=self.category,
            status=Post.Status.PUBLISHED,
            published_at=timezone.now(),
        )

    def test_sitemap_returns_200(self):
        response = self.client.get("/sitemap.xml")
        self.assertEqual(response.status_code, 200)

    def test_sitemap_contains_post_and_category_urls(self):
        response = self.client.get("/sitemap.xml")

        # URL CANÔNICA DO POST
        self.assertContains(
            response,
            f"/posts/{self.post.slug}/",
        )

        # URL CANÔNICA DA CATEGORIA
        self.assertContains(
            response,
            f"/categoria/{self.category.slug}/",
        )
