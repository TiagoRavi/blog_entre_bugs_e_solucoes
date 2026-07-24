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
    - ordenação padrão por data de publicação
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

    Segurança:
    - Apenas posts publicados
    - Não expõe rascunhos
    """
    return (
        get_published_posts()
        .filter(slug=slug)
        .first()
    )


def get_posts_by_category(category: Category) -> QuerySet[Post]:
    """
    Retorna posts publicados de uma categoria específica.
    """
    return (
        get_published_posts()
        .filter(category=category)
    )


def get_related_posts(
    post: Post,
    limit: int = 3,
) -> QuerySet[Post]:
    """
    Retorna posts relacionados ao post atual.

    Regra:
    - Mesma categoria
    - Apenas posts publicados
    - Exclui o próprio post
    """
    if not post.category:
        return Post.objects.none()

    return (
        get_published_posts()
        .filter(category=post.category)
        .exclude(pk=post.pk)[:limit]
    )


def get_related_video_posts(post: Post, limit:int=3) -> QuerySet[Post]:
    """
    Retorna posts da mesma categoria que:
    - estejam publicados
    - tenham vídeo do YouTube
    - não sejam o post atual
    """
    return (
        get_published_posts()
        .filter(
            category=post.category,
            youtube_video_id__isnull=False
        )
        .exclude(pk=post.pk)[:limit]
    )
