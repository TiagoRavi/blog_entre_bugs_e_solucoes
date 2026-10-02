from django.contrib import admin

from .models import Ebook, EbookCategory


@admin.register(EbookCategory)
class EbookCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "slug",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(Ebook)
class EbookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "is_published",
        "created_at",
    )

    list_filter = (
        "category",
        "is_published",
        "created_at",
    )

    search_fields = (
        "title",
        "slug",
        "short_description",
        "description",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    autocomplete_fields = (
        "category",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )