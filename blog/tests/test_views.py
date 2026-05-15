from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model

from blog.models import Post, Category


class BlogViewsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Web")

        self.post = Post.objects.create(
            title="Post Público",
            content="Conteúdo",
            category=self.category,
            status=Post.Status.PUBLISHED,
            published_at=timezone.now(),
        )

    def test_home_page_returns_200(self):
        response = self.client.get(reverse("blog:home"))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_page_returns_200(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_draft_post_returns_404(self):
        draft = Post.objects.create(
            title="Rascunho",
            content="Conteúdo",
            category=self.category,
            status=Post.Status.DRAFT,
        )

        response = self.client.get(draft.get_absolute_url())
        self.assertEqual(response.status_code, 404)


User = get_user_model()


class PostDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="viewer",
            password="123456",
        )
        self.category = Category.objects.create(name="Web")

        self.post = Post.objects.create(
            title="Post com vídeo",
            author=self.user,
            category=self.category,
            content="<p>Conteúdo</p>",
            youtube_video_id="dQw4w9WgXcQ",
            status=Post.Status.PUBLISHED,
            published_at=timezone.now(),
        )

    def test_post_detail_renders_successfully(self):
        url = reverse("blog:post_detail", args=[self.post.slug])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_related_videos_in_context(self):
        url = reverse("blog:post_detail", args=[self.post.slug])
        response = self.client.get(url)

        self.assertIn("related_videos", response.context)


