from django.http import Http404
from django.shortcuts import redirect, render

from .selectors import (
    get_active_categories,
    get_active_category_by_slug,
    get_published_ebook_by_slugs,
    get_published_ebooks,
    get_published_ebooks_by_category,
)


def ebook_index(request):
    categories = get_active_categories()
    ebooks = get_published_ebooks()

    context = {
        "categories": categories,
        "ebooks": ebooks,
    }

    return render(
        request,
        "ebooks/index.html",
        context,
    )


def ebook_category(request, slug):
    category = get_active_category_by_slug(slug)

    if category is None:
        raise Http404("Categoria de ebook não encontrada.")

    ebooks = get_published_ebooks_by_category(slug)

    context = {
        "category": category,
        "ebooks": ebooks,
    }

    return render(
        request,
        "ebooks/category.html",
        context,
    )


def ebook_detail(request, category_slug, slug):
    ebook = get_published_ebook_by_slugs(
        category_slug=category_slug,
        ebook_slug=slug,
    )

    if ebook is None:
        raise Http404("Ebook não encontrado.")

    context = {
        "ebook": ebook,
    }

    return render(
        request,
        "ebooks/detail.html",
        context,
    )


def ebook_download(request, category_slug, slug):
    ebook = get_published_ebook_by_slugs(
        category_slug=category_slug,
        ebook_slug=slug,
    )

    if ebook is None:
        raise Http404("Ebook não encontrado.")

    if not ebook.google_drive_url:
        return redirect(ebook.get_absolute_url())

    return redirect(ebook.google_drive_url)