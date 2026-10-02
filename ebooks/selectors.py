from django.db.models import Prefetch

from .models import Ebook, EbookCategory


def get_active_categories():
    return (
        EbookCategory.objects
        .filter(is_active=True)
        .prefetch_related(
            Prefetch(
                "ebooks",
                queryset=Ebook.objects.filter(
                    is_published=True
                ).order_by("-created_at"),
            )
        )
    )


def get_published_ebooks():
    return (
        Ebook.objects
        .filter(
            is_published=True,
            category__is_active=True,
        )
        .select_related("category")
        .order_by("-created_at")
    )


def get_published_ebooks_by_category(category_slug):
    return (
        Ebook.objects
        .filter(
            is_published=True,
            category__slug=category_slug,
            category__is_active=True,
        )
        .select_related("category")
        .order_by("-created_at")
    )


def get_active_category_by_slug(slug):
    return (
        EbookCategory.objects
        .filter(
            slug=slug,
            is_active=True,
        )
        .first()
    )


def get_published_ebook_by_slugs(category_slug, ebook_slug):
    return (
        Ebook.objects
        .filter(
            slug=ebook_slug,
            category__slug=category_slug,
            category__is_active=True,
            is_published=True,
        )
        .select_related("category")
        .first()
    )