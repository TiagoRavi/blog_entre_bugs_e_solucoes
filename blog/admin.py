from django.contrib import admin
from .models import Post, Category


# ======================================================
# CATEGORY ADMIN
# ======================================================
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin simples e objetivo para categorias.
    """

    fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)
    list_display = ("name", "slug")


# ======================================================
# POST ADMIN (WordPress-like)
# ======================================================
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Admin do Post inspirado no WordPress.

    Objetivos:
    - UX editorial clara
    - Imagem de destaque separada
    - SEO explícito
    - Zero upload local
    """

    # --------------------------
    # LISTAGEM
    # --------------------------
    list_display = ("title", "category", "status", "published_at")
    list_filter = ("status", "category")
    search_fields = ("title", "excerpt", "content")
    ordering = ("-published_at",)

    # Slug automático
    prepopulated_fields = {"slug": ("title",)}

    # --------------------------
    # FIELDSETS (UX EDITORIAL)
    # --------------------------
    fieldsets = (
        (
            "Conteúdo",
            {
                "fields": (
                    "title",
                    "slug",
                    "content",
                )
            },
        ),
        (
            "Imagem de destaque",
            {
                "fields": (
                    "featured_image",
                ),
                "description": (
                    "Cole aqui a URL da imagem de destaque "
                    "(Cloudinary/CDN). Não utilize upload local."
                ),
            },
        ),
        (
            "SEO",
            {
                "fields": (
                    "excerpt",
                ),
            },
        ),
        (
            "Publicação",
            {
                "fields": (
                    "status",
                    "category",
                    "author",
                    "published_at",
                ),
            },
        ),
    )

    # --------------------------
    # COMPORTAMENTO
    # --------------------------
    readonly_fields = ("published_at",)
