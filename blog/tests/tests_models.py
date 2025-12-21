from django.test import TestCase
from django.contrib.auth import get_user_model

from blog.models import Post, Category


User = get_user_model()


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="123456",
        )
        self.category = Category.objects.create(name="Django")

    def test_publish_sets_status_and_date(self):
        post = Post.objects.create(
            title="Meu Post",
            content="Conteúdo",
            author=self.user,
            category=self.category,
        )

        post.publish()

        self.assertEqual(post.status, Post.Status.PUBLISHED)
        self.assertIsNotNone(post.published_at)

    def test_unpublish_resets_status_and_date(self):
        post = Post.objects.create(
            title="Outro Post",
            content="Conteúdo",
            author=self.user,
            category=self.category,
            status=Post.Status.PUBLISHED,
        )

        post.unpublish()

        self.assertEqual(post.status, Post.Status.DRAFT)
        self.assertIsNone(post.published_at)
