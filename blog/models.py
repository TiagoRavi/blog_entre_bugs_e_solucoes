from html import unescape

from cloudinary.models import CloudinaryField
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags
from django.utils.text import Truncator, slugify
from tinymce.models import HTMLField

from .utils.youtube import extract_youtube_id


# ======================================================
# CATEGORY
# ======================================================
class Category(models.Model):
    """
    Representa uma categoria de posts do blog.
    """

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nome",
        help_text="Nome público da categoria.",
    )

    slug = models.SlugField(
        max_length=120,
        unique=True,
        verbose_name="Slug",
        help_text="URL da categoria. Gerada automaticamente a partir do nome.",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em",
    )

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("blog:category_posts", args=[self.slug])

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

# ======================================================
# CTA (SEO)
# ======================================================
class CTA(models.Model):
    """
    Call To Action reutilizável para SEO interno.
    """

    title = models.CharField(
        max_length=150,
        verbose_name="Título do CTA",
        help_text="Título exibido no box."
    )

    description = models.TextField(
        blank=True,
        verbose_name="Descrição",
        help_text="Texto opcional para reforçar o CTA."
    )

    url = models.URLField(
        verbose_name="Link"
    )

    anchor_text = models.CharField(
        max_length=150,
        verbose_name="Texto âncora (SEO)",
        help_text="Texto do link para SEO interno."
    )

    open_in_new_tab = models.BooleanField(
        default=True,
        verbose_name="Abrir em nova aba"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Ativo"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "CTA (SEO)"
        verbose_name_plural = "CTAs (SEO)"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title

# ======================================================
# QUERYSET
# ======================================================
class PostQuerySet(models.QuerySet):
    def published(self) -> models.QuerySet:
        return self.filter(
            status=Post.Status.PUBLISHED,
            published_at__lte=timezone.now(),
        )

# ======================================================
# POST
# ======================================================
class Post(models.Model):
    """
    Modelo principal do Blog.
    """

    # --------------------------
    # Status
    # --------------------------
    class Status(models.TextChoices):
        DRAFT = "draft", "Rascunho"
        PUBLISHED = "published", "Publicado"

    # --------------------------
    # Conteúdo
    # --------------------------
    title = models.CharField(
        max_length=200,
        verbose_name="Título",
    )

    slug = models.SlugField(
        max_length=220,
        unique=True,
        verbose_name="Slug",
        help_text="URL do post. Gerada automaticamente se deixada em branco.",
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts",
        verbose_name="Autor",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="posts",
        verbose_name="Categoria",
    )

    excerpt = models.CharField(
        max_length=160,
        blank=True,
        verbose_name="Resumo (SEO)",
        help_text="Gerado automaticamente se deixado em branco.",
    )

    content = HTMLField(
        verbose_name="Conteúdo",
        help_text="Conteúdo HTML gerado pelo editor.",
    )

    ctas = models.ManyToManyField(
        CTA,
        blank=True,
        related_name="posts",
        verbose_name="CTAs de SEO"
    )

    featured_image = CloudinaryField(
        verbose_name="Imagem de destaque",
        blank=True,
        null=True,
    )

    # 🎥 YouTube
    youtube_video_id = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Vídeo do YouTube",
        help_text="Informe apenas o ID do vídeo (ex: dQw4w9WgXcQ)",
    )

    # --------------------------
    # Publicação
    # --------------------------
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT,
        db_index=True,
        verbose_name="Status",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em",
    )

    published_at = models.DateTimeField(
        blank=True,
        null=True,
        db_index=True,
        verbose_name="Publicado em",
    )


    # --------------------------
    # Manager
    # --------------------------
    objects = PostQuerySet.as_manager()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-published_at"]
        indexes = [
            models.Index(fields=["status", "published_at"]),
        ]

    def __str__(self) -> str:
        return self.title

    # ==================================================
    # DOMÍNIO
    # ==================================================
    def publish(self) -> None:
        self.status = self.Status.PUBLISHED
        self.published_at = timezone.now()
        self.save(update_fields=["status", "published_at"])

    def unpublish(self) -> None:
        self.status = self.Status.DRAFT
        self.published_at = None
        self.save(update_fields=["status", "published_at"])

    def _generate_slug(self) -> None:
        if self.slug:
            return

        base_slug = slugify(self.title)
        slug = base_slug
        counter = 1

        while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        self.slug = slug

    def _generate_excerpt(self) -> None:
        if self.excerpt or not self.content:
            return
        
        self.excerpt = Truncator(
            unescape(strip_tags(self.content))
        ).chars(155)

    def _sync_publication(self) -> None:
        if self.status == self.Status.PUBLISHED and not self.published_at:
            self.published_at = timezone.now()

        elif self.status == self.Status.DRAFT:
            self.published_at = None

    def _normalize_youtube(self) -> None:
        if not self.youtube_video_id:   
            self.youtube_video_id = None
            return

        self.youtube_video_id = extract_youtube_id(self.youtube_video_id)

    # ==================================================
    # SAVE CENTRAL
    # ==================================================
    def save(self, *args, **kwargs) -> None:
        self._generate_slug()
        self._generate_excerpt()
        self._sync_publication()
        self._normalize_youtube()

        super().save(*args, **kwargs)

    
    # ==================================================
    # URL CANÔNICA
    # ==================================================
    def get_absolute_url(self) -> str:
        return reverse("blog:post_detail", args=[self.slug])
    
    
# ======================================================
# FAQ
# ======================================================
class FAQ(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="faqs",
    )
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.question
