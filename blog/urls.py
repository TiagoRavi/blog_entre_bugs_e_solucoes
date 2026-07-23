from django.urls import path

from .views import (
    HomeView,
    BlogListView,
    PostDetailView,
    CategoryPostListView,
)

# Namespace do app (obrigatório para reverse e templates)
app_name = "blog"


urlpatterns = [
    # --------------------------------------------------
    # Home do site
    # URL: /
    # --------------------------------------------------
    path(
        "",
        HomeView.as_view(),
        name="home",
    ),

    # --------------------------------------------------
    # Listagem principal do blog
    # URL: /blog/
    # --------------------------------------------------
    path(
        "blog/",
        BlogListView.as_view(),
        name="post_list",
    ),

    # --------------------------------------------------
    # Detalhe do post
    # URL: /posts/<slug>/
    # --------------------------------------------------
    path(
        "posts/<slug:slug>/",
        PostDetailView.as_view(),
        name="post_detail",
    ),

    # --------------------------------------------------
    # Listagem de posts por categoria
    # URL: /categoria/<slug>/
    # --------------------------------------------------
    path(
        "categoria/<slug:slug>/",
        CategoryPostListView.as_view(),
        name="category_posts",
    ),
]
