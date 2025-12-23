from typing import Optional

from django.db.models import QuerySet

from .models import Category, Post


# ======================================================
# CATEGORY SELECTORS
# ======================================================
def get_all_categories() -> QuerySet[Category]:
    """
    Retorna todas as categorias ordenadas pelo nome.

    Uso típico:
    - Menu
    - Sidebar
    - Filtro de posts
    """
    return Category.objects.all().order_by("name")


def get_category_by_slug(slug: str) -> Optional[Category]:
    """
    Retorna uma categoria pelo slug.

    Retorna None caso não exista.
    """
    return Category.objects.filter(slug=slug).first()


# ======================================================
# POST SELECTORS
# ======================================================
def get_published_posts() -> QuerySet[Post]:
    """
    Retorna todos os posts publicados,
    já otimizados para exibição em listas.

    Otimizações aplicadas:
    - select_related para author e category
    """
    return (
        Post.objects.published()
        .select_related("author", "category")
        .order_by("-published_at")
    )


def get_latest_published_posts(limit: int = 5) -> QuerySet[Post]:
    """
    Retorna os últimos posts publicados.

    Ideal para:
    - Home
    - Sidebar
    - Widgets
    """
    return get_published_posts()[:limit]


def get_post_by_slug(slug: str) -> Optional[Post]:
    """
    Retorna um post publicado pelo slug.

    Importante:
    - Apenas posts publicados
    - Garante segurança (não expõe rascunhos)
    """
    return (
        Post.objects.published()
        .select_related("author", "category")
        .filter(slug=slug)
        .first()
    )


def get_posts_by_category(category: Category) -> QuerySet[Post]:
    """
    Retorna posts publicados de uma categoria específica.
    """
    return (
        Post.objects.published()
        .select_related("author", "category")
        .filter(category=category)
        .order_by("-published_at")
    )

def get_related_posts(post, limit=3):
    if not post.category:
        return Post.objects.none()

    return (
        Post.objects
        .filter(
            category=post.category,
            status=Post.Status.PUBLISHED,
        )
        .exclude(pk=post.pk)
        .order_by('-published_at')[:limit]
    )
