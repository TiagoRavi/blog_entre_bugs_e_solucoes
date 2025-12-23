from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .selectors import get_published_posts, get_related_posts


from .models import Post, Category
from .selectors import (
    get_latest_published_posts,
    get_published_posts,
)


# ======================================================
# HOME
# ======================================================
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
class BlogListView(ListView):
    """
    Página principal do blog com paginação e busca.
    """

    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 9

    def get_queryset(self):
        """
        Retorna posts publicados com suporte a busca.
        """
        queryset = get_published_posts()

        # Busca simples por query string (?q=...)
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
class PostDetailView(DetailView):
    """
    Página de detalhe do post.

    Responsabilidades:
    - Exibir apenas posts publicados
    - Injetar posts relacionados no contexto
    """

    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        """
        Retorna apenas posts publicados.
        """
        return get_published_posts().select_related(
            "category",
            "author",
        )

    def get_context_data(self, **kwargs):
        """
        Adiciona posts relacionados ao contexto do template.
        """
        context = super().get_context_data(**kwargs)

        post = self.object  # post atual

        context["related_posts"] = get_related_posts(
            post=post,
            limit=3,
        )

        return context



# ======================================================
# LISTAGEM POR CATEGORIA
# ======================================================
class CategoryPostListView(ListView):
    """
    Página de listagem de posts por categoria.

    Responsabilidade:
    - Exibir apenas posts publicados
    - Filtrar pelo slug da categoria
    - Reutilizar o template de listagem
    """

    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 9

    def get_queryset(self):
        """
        Retorna posts publicados filtrados pela categoria.
        """
        return (
            get_published_posts()
            .filter(category__slug=self.kwargs["slug"])
            .select_related("category")
            .order_by("-published_at")
        )

    def get_context_data(self, **kwargs):
        """
        Adiciona a categoria atual ao contexto do template.

        Segurança:
        - Retorna 404 se a categoria não existir
        """
        context = super().get_context_data(**kwargs)
        context["category"] = get_object_or_404(
            Category,
            slug=self.kwargs["slug"],
        )
        return context

