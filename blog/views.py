
from copy import copy

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.utils.translation import get_language
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView

from .models import Category, Post
from .selectors import (
    get_latest_published_posts,
    get_posts_by_category,
    get_published_posts,
    get_related_posts,
    get_related_video_posts,
    get_post_translation_by_slug,
)

# ======================================================
# HOME
# ======================================================

@method_decorator(cache_page(60 * 15), name="dispatch")
class HomeView(ListView):
    """
    Página inicial do blog.
    Exibe os últimos posts publicados.
    """

    template_name = "blog/home.html"
    context_object_name = "posts"

    def get_queryset(self):
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
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return (
            get_published_posts()
            .select_related("category", "author")
        )

    def get_object(self, queryset=None):
        language = (get_language() or "pt-br").lower()
        slug = self.kwargs["slug"]

        self.translation = None
        self.original_post = None

        if language == "pt-br":
            post = get_object_or_404(
                self.get_queryset(),
                slug=slug,
            )
            self.original_post = post
            return post

        if language not in {"en", "es"}:
            raise Http404("Idioma não suportado.")

        translation = get_post_translation_by_slug(
            slug=slug,
            language=language,
        )

        if translation is None:
            raise Http404("Artigo traduzido não encontrado.")

        original_post = translation.post
        self.original_post = original_post

        # Copia o objeto para não sobrescrever os campos originais.
        post = copy(original_post)
        post.title = translation.title
        post.slug = translation.slug
        post.excerpt = translation.excerpt
        post.content = translation.content

        self.translation = translation
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = self.object
        original_post = self.original_post or post

        # Usa o artigo original para buscar conteúdo relacionado.
        context["related_posts"] = get_related_posts(
            post=original_post,
            limit=3,
        )

        context["related_videos"] = []

        if original_post.youtube_video_id:
            context["related_videos"] = get_related_video_posts(
                post=original_post,
                limit=3,
            )

        context["is_post_detail"] = True
        context["translation"] = self.translation
        context["original_post"] = original_post

        site_url = getattr(
            settings,
            "SITE_URL",
            "https://entrebugsesolucoes.com.br",
        ).rstrip("/")

        language_alternates = [
            {
                "language": "pt-br",
                "url": f"{site_url}/posts/{original_post.slug}/",
            }
        ]

        for item in original_post.translations.all():
            if item.language not in {"en", "es"}:
                continue

            language_alternates.append({
                "language": item.language,
                "url": (
                    f"{site_url}/{item.language}/posts/"
                    f"{item.slug}/"
                ),
            })

        context["language_alternates"] = language_alternates
        context["site_url"] = site_url

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


# ======================================================
# PÁGINA DO AUTOR
# ======================================================

@method_decorator(cache_page(60 * 10), name="dispatch")
class AuthorDetailView(ListView):
    """
    Página pública do autor.
    Exibe artigos publicados, perfil público e paginação.
    """

    template_name = "blog/author_detail.html"
    context_object_name = "posts"
    paginate_by = 9

    def get_author(self):
        User = get_user_model()

        return get_object_or_404(
            User.objects.select_related("profile"),
            username=self.kwargs["username"],
        )

    def get_queryset(self):
        author = self.get_author()

        return (
            get_published_posts()
            .filter(author=author)
            .select_related("category", "author")
            .order_by("-published_at", "-pk")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = self.get_author()
        return context
