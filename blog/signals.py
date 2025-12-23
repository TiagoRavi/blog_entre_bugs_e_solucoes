from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache

from .models import Post


# ======================================================
# CACHE INVALIDATION — POSTS
# ======================================================
@receiver(post_save, sender=Post)
def invalidate_cache_on_post_save(sender, instance: Post, **kwargs):
    """
    Invalida caches públicos quando um post é criado ou atualizado.

    Páginas afetadas:
    - Home
    - Listagem do blog
    - Página do próprio post
    - Página da categoria
    """

    # Home
    cache.delete_pattern("*home*")

    # Listagem principal
    cache.delete_pattern("*blog*")

    # Página do post
    if instance.slug:
        cache.delete_pattern(f"*posts/{instance.slug}*")

    # Página da categoria
    if instance.category:
        cache.delete_pattern(f"*categoria/{instance.category.slug}*")


@receiver(post_delete, sender=Post)
def invalidate_cache_on_post_delete(sender, instance: Post, **kwargs):
    """
    Invalida caches públicos quando um post é removido.
    """

    cache.delete_pattern("*home*")
    cache.delete_pattern("*blog*")

    if instance.slug:
        cache.delete_pattern(f"*posts/{instance.slug}*")

    if instance.category:
        cache.delete_pattern(f"*categoria/{instance.category.slug}*")
