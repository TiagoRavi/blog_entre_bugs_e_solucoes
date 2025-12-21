from django.urls import path

# Views públicas do blog
from .views import (
    HomeView,
    BlogListView,
    PostDetailView,
    CategoryPostListView,  # 👈 NOVA VIEW IMPORTADA
)

# Namespace do app (obrigatório para reverse("blog:..."))
app_name = "blog"

urlpatterns = [
    # =====================================
    # HOME
    # /
    # =====================================
    path(
        "",
        HomeView.as_view(),
        name="home",
    ),

    # =====================================
    # LISTAGEM DE POSTS
    # /blog/
    # =====================================
    path(
        "blog/",
        BlogListView.as_view(),
        name="post_list",
    ),

    # =====================================
    # DETALHE DO POST
    # /posts/<slug>/
    # =====================================
    path(
        "posts/<slug:slug>/",
        PostDetailView.as_view(),
        name="post_detail",
    ),

    # =====================================
    # LISTAGEM POR CATEGORIA
    # /categoria/<slug>/
    # =====================================
    path(
        "categoria/<slug:slug>/",
        CategoryPostListView.as_view(),
        name="category_posts",  # 👈 ESSE NOME É CRÍTICO
    ),
]
