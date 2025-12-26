from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import Truncator, slugify
from django.utils.html import strip_tags
from django.urls import reverse

from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField


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

    def get_absolute_url(self):
        """URL canônica da categoria."""
        return reverse("blog:category_posts", args=[self.slug])

    def save(self, *args, **kwargs):
        """
        Gera o slug automaticamente se não informado.
        """
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)


# ======================================================
# QUERYSET / MANAGER
# ======================================================
from django.db import models
from django.utils import timezone

class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(
            status=Post.Status.PUBLISHED,
            published_at__lte=timezone.now(),
        )


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Rascunho"
        PUBLISHED = "published", "Publicado"

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    published_at = models.DateTimeField(null=True, blank=True)

    # ✅ MANAGER CORRETO
    objects = PostQuerySet.as_manager()



# ======================================================
# POST
# ======================================================
class Post(models.Model):
    """
    Modelo principal do Blog.
    """

    # --------------------------
    # Status do Post
    # --------------------------
    class Status(models.TextChoices):
        DRAFT = "draft", "Rascunho"
        PUBLISHED = "published", "Publicado"

    # --------------------------
    # Campos principais
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

    featured_image = CloudinaryField(
        verbose_name="Imagem de destaque",
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT,
        db_index=True,
        verbose_name="Status",
    )

    # --------------------------
    # Datas
    # --------------------------
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
            models.Index(fields=["slug"]),
            models.Index(fields=["status", "published_at"]),
        ]

    def __str__(self) -> str:
        return self.title

    # ==================================================
    # REGRAS DE DOMÍNIO
    # ==================================================
    def publish(self):
        """Publica o post explicitamente."""
        self.status = self.Status.PUBLISHED
        self.published_at = timezone.now()
        self.save(update_fields=["status", "published_at"])

    def unpublish(self):
        """Retorna o post para rascunho."""
        self.status = self.Status.DRAFT
        self.published_at = None
        self.save(update_fields=["status", "published_at"])

    # ==================================================
    # SAVE — CONSISTÊNCIA CENTRAL
    # ==================================================
    def save(self, *args, **kwargs):
        """
        Responsabilidades:
        - Gerar slug automaticamente (com fallback seguro)
        - Gerar excerpt limpo para SEO
        - Garantir coerência entre status e published_at
        """

        # Slug automático
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        # Excerpt automático (remove HTML)
        if not self.excerpt and self.content:
            texto_limpo = strip_tags(self.content)
            self.excerpt = Truncator(texto_limpo).chars(155)

        # Coerência de publicação
        if self.status == self.Status.PUBLISHED and not self.published_at:
            self.published_at = timezone.now()

        if self.status == self.Status.DRAFT:
            self.published_at = None

        super().save(*args, **kwargs)

    # ==================================================
    # URL CANÔNICA
    # ==================================================
    def get_absolute_url(self):
        """URL canônica do post."""
        return reverse("blog:post_detail", args=[self.slug])
