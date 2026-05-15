from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone

from blog.models import Post, Category
from blog.selectors import get_related_video_posts


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


User = get_user_model()


class PostYouTubeTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="tiago",
            password="123456",
        )
        self.category = Category.objects.create(
            name="Python",
        )

    def test_youtube_url_is_normalized_to_id(self):
        post = Post.objects.create(
            title="Post com vídeo",
            author=self.user,
            category=self.category,
            content="<p>Conteúdo</p>",
            youtube_video_id="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            status=Post.Status.PUBLISHED,
            published_at=timezone.now(),
        )

        post.refresh_from_db()

        self.assertEqual(post.youtube_video_id, "dQw4w9WgXcQ")

    def test_invalid_youtube_url_results_in_null(self):
        post = Post.objects.create(
            title="Post inválido",
            author=self.user,
            category=self.category,
            content="<p>Conteúdo</p>",
            youtube_video_id="https://google.com",
        )

        post.refresh_from_db()

        self.assertIsNone(post.youtube_video_id)


User = get_user_model()


class RelatedVideoPostsSelectorTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="editor",
            password="123456",
        )
        self.category = Category.objects.create(name="Django")

        self.main_post = Post.objects.create(
            title="Post principal",
            author=self.user,
            category=self.category,
            content="<p>Main</p>",
            youtube_video_id="dQw4w9WgXcQ",
            status=Post.Status.PUBLISHED,
            published_at=timezone.now(),
        )

        self.related_post = Post.objects.create(
            title="Post relacionado",
            author=self.user,
            category=self.category,
            content="<p>Relacionado</p>",
            youtube_video_id="abc123xyz00",
            status=Post.Status.PUBLISHED,
            published_at=timezone.now(),
        )

        self.draft_post = Post.objects.create(
            title="Rascunho",
            author=self.user,
            category=self.category,
            content="<p>Draft</p>",
            youtube_video_id="draftvideo1",
            status=Post.Status.DRAFT,
        )

    def test_returns_only_published_posts_with_video(self):
        result = get_related_video_posts(self.main_post)

        self.assertIn(self.related_post, result)
        self.assertNotIn(self.main_post, result)
        self.assertNotIn(self.draft_post, result)