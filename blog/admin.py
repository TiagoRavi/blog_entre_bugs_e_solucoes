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
    """

    list_display = ("title", "status", "created_at")
    list_filter = ("status", "category")
    search_fields = ("title", "excerpt")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-created_at",)

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
                "fields": ("featured_image",),
                "description": (
                    "Cole aqui a URL da imagem de destaque "
                    "(Cloudinary/CDN). Não utilize upload local."
                ),
            },
        ),
        (
            "Vídeo do YouTube",
            {
                "fields": ("youtube_video_id",),
                "description": (
                    "Informe apenas o ID do vídeo "
                    "(ex: dQw4w9WgXcQ). O vídeo aparecerá no post automaticamente."
                ),
            },
        ),
        (
            "SEO",
            {
                "fields": ("excerpt",),
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

    readonly_fields = ("published_at",)

