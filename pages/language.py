
import re

from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import check_for_language

from blog.models import Post, PostTranslation


PAGE_ROUTES = {
    "pages:about": {
        "pt-br": "pages:about",
        "en": "pages:about_en",
        "es": "pages:about_es",
    },
    "pages:about_author": {
        "pt-br": "pages:about_author",
        "en": "pages:about_author_en",
        "es": "pages:about_author_es",
    },
    "pages:contact": {
        "pt-br": "pages:contact",
        "en": "pages:contact_en",
        "es": "pages:contact_es",
    },
    "pages:privacy": {
        "pt-br": "pages:privacy",
        "en": "pages:privacy_en",
        "es": "pages:privacy_es",
    },
    "pages:terms": {
        "pt-br": "pages:terms",
        "en": "pages:terms_en",
        "es": "pages:terms_es",
    },
    "pages:disclaimer": {
        "pt-br": "pages:disclaimer",
        "en": "pages:disclaimer_en",
        "es": "pages:disclaimer_es",
    },
}


def switch_language(request):
    if request.method != "POST":
        return redirect("blog:home")

    language = request.POST.get("language", "pt-br").lower()

    if not check_for_language(language):
        language = "pt-br"

    current_path = request.POST.get("current_path", "/").split("?")[0]
    current_path = "/" + current_path.lstrip("/")

    now = timezone.now()

    # Reconhece artigos traduzidos: /en/posts/slug/ ou /es/posts/slug/
    translated_match = re.fullmatch(
        r"/(en|es)/posts/(?P<slug>[-\w]+)/?",
        current_path,
    )

    # Reconhece artigos originais em português: /posts/slug/
    original_match = re.fullmatch(
        r"/posts/(?P<slug>[-\w]+)/?",
        current_path,
    )

    original = None

    if translated_match:
        current_language = translated_match.group(1)
        slug = translated_match.group("slug")

        translation = (
            PostTranslation.objects.filter(
                slug=slug,
                language=current_language,
                post__status=Post.Status.PUBLISHED,
                post__published_at__lte=now,
            )
            .select_related("post")
            .first()
        )

        if translation:
            original = translation.post

    elif original_match:
        slug = original_match.group("slug")

        original = Post.objects.filter(
            slug=slug,
            status=Post.Status.PUBLISHED,
            published_at__lte=now,
        ).first()

    # Troca de idioma de um artigo.
    if translated_match or original_match:
        if original:
            if language == "pt-br":
                return redirect(
                    reverse(
                        "blog:post_detail",
                        kwargs={"slug": original.slug},
                    )
                )

            translation = PostTranslation.objects.filter(
                post=original,
                language=language,
            ).first()

            if translation:
                return redirect(
                    f"/{language}/posts/{translation.slug}/"
                )

        # Sem artigo equivalente no idioma selecionado.
        if language == "pt-br":
            return redirect("/blog/")

        return redirect(f"/{language}/blog/")

    # Troca de idioma das páginas institucionais.
    for translations in PAGE_ROUTES.values():
        for source_language, route_name in translations.items():
            if current_path == reverse(route_name):
                target_route = translations.get(language)

                if target_route:
                    return redirect(reverse(target_route))

                break

    # Fallback para páginas sem correspondência.
    if language == "pt-br":
        return redirect("/blog/")

    return redirect(f"/{language}/blog/")
