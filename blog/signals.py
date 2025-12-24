from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache

from .models import Post


# ======================================================
# CACHE INVALIDATION — POSTS (SAFE)
# ======================================================
def safe_delete_pattern(pattern: str) -> None:
    """
    Remove chaves de cache por padrão, se suportado.

    Compatível com:
    - django-redis (Redis)
    - LocMemCache (fallback seguro)
    """
    if hasattr(cache, "delete_pattern"):
        cache.delete_pattern(pattern)
    else:
        # Fallback: limpa todo o cache para evitar erro 500
        cache.clear()


@receiver(post_save, sender=Post)
def invalidate_cache_on_post_save(sender, instance: Post, **kwargs):
    """
    Invalida caches públicos quando um post é criado ou atualizado.
    """

    # Home
    safe_delete_pattern("*home*")

    # Listagem principal
    safe_delete_pattern("*blog*")

    # Página do post
    if instance.slug:
        safe_delete_pattern(f"*posts/{instance.slug}*")

    # Página da categoria
    if instance.category_id:
        safe_delete_pattern(f"*categoria/{instance.category.slug}*")


@receiver(post_delete, sender=Post)
def invalidate_cache_on_post_delete(sender, instance: Post, **kwargs):
    """
    Invalida caches públicos quando um post é removido.
    """

    # Home
    safe_delete_pattern("*home*")

    # Listagem principal
    safe_delete_pattern("*blog*")

    # Página do post
    if instance.slug:
        safe_delete_pattern(f"*posts/{instance.slug}*")

    # Página da categoria
    if instance.category_id:
        safe_delete_pattern(f"*categoria/{instance.category.slug}*")
