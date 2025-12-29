from .models import Category
from django.conf import settings
from django.core.cache import cache

def categories_menu(request):
    categories = cache.get("menu_categories")
    if not categories:
        categories = Category.objects.only("id", "name", "slug")
        cache.set("menu_categories", categories, 60 * 60)

    return {"menu_categories": categories}


def seo(request):
    path = request.path
    if not path.endswith("/"):
        path = f"{path}/"

    return {
        "SITE_URL": settings.SITE_URL,
        "CANONICAL_URL": f"{settings.SITE_URL}{path}",
    }

