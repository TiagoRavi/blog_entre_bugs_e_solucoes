from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import Truncator, slugify
from django.urls import reverse



# ======================================================
# CATEGORY
# ======================================================
class Category(models.Model):
    """
    Representa uma categoria de posts do blog.

    Responsabilidade:
    - Apenas armazenar dados da categoria
    - Garantir unicidade e consistência do slug
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

    # ==========================
    # URL CANÔNICA
    # ==========================
    def get_absolute_url(self):
        return reverse(
            "blog:category_posts",
            args=[self.slug],
        )

    # --------------------------
    # Hooks internos
    # --------------------------
    def save(self, *args, **kwargs):
        """
        Garante que o slug seja gerado automaticamente
        caso não seja informado manualmente.
        """
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)


# ======================================================
# QUERYSET / MANAGER
# ======================================================
class PostQuerySet(models.QuerySet):
    """
    QuerySet customizado para encapsular
    queries reutilizáveis do Post.
    """

    def published(self):
        """
        Retorna apenas posts publicados
        e com data válida.
        """
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

    Responsabilidades:
    - Representar um artigo/post
    - Conter regras essenciais do domínio
    - NÃO conter lógica de apresentação
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

    content = models.TextField(
        verbose_name="Conteúdo",
    )

    image = models.ImageField(
        upload_to="posts/",
        blank=True,
        null=True,
        verbose_name="Imagem de destaque",
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
    # REGRAS DE DOMÍNIO (explícitas)
    # ==================================================
    def publish(self):
        """
        Publica o post de forma explícita.

        Importante:
        - Não depender apenas do save automático
        - Facilita uso futuro em services ou admin
        """
        self.status = self.Status.PUBLISHED
        self.published_at = timezone.now()
        self.save(update_fields=["status", "published_at"])

    def unpublish(self):
        """
        Retorna o post para rascunho.
        """
        self.status = self.Status.DRAFT
        self.published_at = None
        self.save(update_fields=["status", "published_at"])

    # ==================================================
    # HOOKS INTERNOS
    # ==================================================
    def save(self, *args, **kwargs):
        """
        Hook central de consistência do modelo.

        Responsabilidades:
        - Gerar slug
        - Gerar excerpt
        - Garantir coerência entre status e published_at
        """

        # Gera slug automaticamente
        if not self.slug:
            self.slug = slugify(self.title)

        # Gera excerpt automático (SEO)
        if not self.excerpt:
            self.excerpt = Truncator(self.content).chars(155)

        # Consistência de publicação
        if self.status == self.Status.PUBLISHED and not self.published_at:
            self.published_at = timezone.now()

        if self.status == self.Status.DRAFT:
            self.published_at = None

        super().save(*args, **kwargs)

    # ==================================================
    # URL
    # ==================================================
    def get_absolute_url(self):
        """
        Retorna a URL canônica do post.
        """
        return f"/posts/{self.slug}/"
