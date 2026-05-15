from django.test import TestCase
from django.utils import timezone

from blog.models import Post, Category
from blog.selectors import get_published_posts


class PostSelectorsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Python")

        Post.objects.create(
            title="Rascunho",
            content="Conteúdo",
            category=self.category,
            status=Post.Status.DRAFT,
        )

        Post.objects.create(
            title="Publicado",
            content="Conteúdo",
            category=self.category,
            status=Post.Status.PUBLISHED,
            published_at=timezone.now(),
        )

    def test_get_published_posts_returns_only_published(self):
        posts = get_published_posts()

        self.assertEqual(posts.count(), 1)
        self.assertEqual(posts.first().title, "Publicado")
