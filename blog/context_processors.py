from .models import Category


def categories_menu(request):
    return {
        "menu_categories": Category.objects.all()
    }
