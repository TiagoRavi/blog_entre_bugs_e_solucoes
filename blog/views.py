from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView

from .models import Category, Post
from .selectors import (
    get_latest_published_posts,
    get_posts_by_category,
    get_published_posts,
    get_related_posts,
    get_related_video_posts,
)

# ======================================================
# HOME
# ======================================================
@method_decorator(cache_page(60 * 15), name="dispatch")
class HomeView(ListView):
    """
    Página inicial do blog.

    Responsabilidade:
    - Exibir os últimos posts publicados
    - NÃO definir regras de query complexas
    """

    template_name = "blog/home.html"
    context_object_name = "posts"

    def get_queryset(self):
        """
        Retorna os 6 posts mais recentes.

        A regra de consulta fica centralizada
        no selector.
        """
        return get_latest_published_posts(limit=6)


# ======================================================
# LISTAGEM DO BLOG + BUSCA
# ======================================================
@method_decorator(cache_page(60 * 10), name="dispatch")
class BlogListView(ListView):
    """
    Página principal do blog com paginação e busca.
    """

    template_name = "blog/blog_list.html"
    context_object_name = "posts"
    paginate_by = 9

    def get_queryset(self):
        queryset = get_published_posts()

        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q)
                | Q(content__icontains=q)
                | Q(excerpt__icontains=q)
            )

        return queryset

# ======================================================
# DETALHE DO POST
# ======================================================
@method_decorator(cache_page(60 * 15), name="dispatch")
class PostDetailView(DetailView):
    """
    Página de detalhe do post.

    Responsabilidades:
    - Exibir apenas posts publicados
    - Injetar posts relacionados
    - Injetar playlist de vídeos (quando existir)
    """

    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        """
        Retorna apenas posts publicados
        com relações otimizadas.
        """
        return (
            get_published_posts()
            .select_related("category", "author")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = self.object

        # Posts relacionados (texto)
        context["related_posts"] = get_related_posts(
            post=post,
            limit=3,
        )

        # Playlist de vídeos (somente se o post tiver vídeo)
        context["related_videos"] = []

        if post.youtube_video_id:
            context["related_videos"] = get_related_video_posts(
                post=post,
                limit=3,
            )

        # Flag de layout
        context["is_post_detail"] = True

        return context

# ======================================================
# LISTAGEM POR CATEGORIA
# ======================================================
@method_decorator(cache_page(60 * 10), name="dispatch")
class CategoryPostListView(ListView):
    """
    Página de listagem de posts por categoria.
    """

    template_name = "blog/blog_list.html"
    context_object_name = "posts"
    paginate_by = 9

    def get_queryset(self):
        return get_posts_by_category(self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["category"] = get_object_or_404(
            Category,
            slug=self.kwargs["slug"],
        )

        return context

