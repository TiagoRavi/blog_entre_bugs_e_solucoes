from decimal import Decimal

from django.db import models
from django.urls import reverse


class EbookCategory(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Nome",
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Slug",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Descrição",
    )
    image = models.ImageField(
        upload_to="ebooks/categories/",
        blank=True,
        null=True,
        verbose_name="Imagem",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Ativa",
    )

    class Meta:
        verbose_name = "Categoria de ebook"
        verbose_name_plural = "Categorias de ebooks"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "ebooks:category",
            kwargs={"slug": self.slug},
        )


class Ebook(models.Model):
    category = models.ForeignKey(
        EbookCategory,
        on_delete=models.PROTECT,
        related_name="ebooks",
        verbose_name="Categoria",
    )

    title = models.CharField(
        max_length=200,
        verbose_name="Título",
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Slug",
    )
    short_description = models.TextField(
        verbose_name="Descrição curta",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Descrição",
    )
    cover = models.ImageField(
        upload_to="ebooks/covers/",
        verbose_name="Capa",
    )
    author = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Autor",
    )

    # Download gratuito
    google_drive_url = models.URLField(
        blank=True,
        verbose_name="URL do Google Drive",
    )

    # Venda
    original_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Preço original",
    )
    sale_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Preço promocional",
    )
    purchase_url = models.URLField(
        blank=True,
        verbose_name="URL de compra",
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name="Publicado",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em",
    )

    class Meta:
        verbose_name = "Ebook"
        verbose_name_plural = "Ebooks"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "ebooks:detail",
            kwargs={
                "category_slug": self.category.slug,
                "slug": self.slug,
            },
        )

    @property
    def has_discount(self):
        if (
            self.original_price is None
            or self.sale_price is None
        ):
            return False

        return self.sale_price < self.original_price

    @property
    def discount_percentage(self):
        if not self.has_discount:
            return 0

        discount = (
            (self.original_price - self.sale_price)
            / self.original_price
        ) * Decimal("100")

        return round(discount)