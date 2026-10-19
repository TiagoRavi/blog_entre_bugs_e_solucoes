from django.urls import path

from .views import (
    AboutView,
    AboutAuthorView,
    ContactView,
    PrivacyView,
    TermsView,
    DisclaimerView,
)

app_name = "pages"

urlpatterns = [
    # =====================================================
    # PORTUGUÊS — URLs existentes, sem prefixo
    # =====================================================
    path("sobre/", AboutView.as_view(), name="about"),
    path(
        "about-author/",
        AboutAuthorView.as_view(),
        name="about_author",
    ),
    path("contato/", ContactView.as_view(), name="contact"),
    path(
        "politica-de-privacidade/",
        PrivacyView.as_view(),
        name="privacy",
    ),
    path("termos-de-uso/", TermsView.as_view(), name="terms"),
    path("disclaimer/", DisclaimerView.as_view(), name="disclaimer"),

    # =====================================================
    # INGLÊS — URLs com prefixo /en/
    # =====================================================
    path("en/about/", AboutView.as_view(), name="about_en"),
    path(
        "en/about-author/",
        AboutAuthorView.as_view(),
        name="about_author_en",
    ),
    path("en/contact/", ContactView.as_view(), name="contact_en"),
    path(
        "en/privacy-policy/",
        PrivacyView.as_view(),
        name="privacy_en",
    ),
    path("en/terms-of-use/", TermsView.as_view(), name="terms_en"),
    path("en/disclaimer/", DisclaimerView.as_view(), name="disclaimer_en"),

    # =====================================================
    # ESPANHOL — URLs com prefixo /es/
    # =====================================================
    path("es/acerca-de/", AboutView.as_view(), name="about_es"),
    path(
        "es/sobre-el-autor/",
        AboutAuthorView.as_view(),
        name="about_author_es",
    ),
    path("es/contacto/", ContactView.as_view(), name="contact_es"),
    path(
        "es/politica-de-privacidad/",
        PrivacyView.as_view(),
        name="privacy_es",
    ),
    path("es/terminos-de-uso/", TermsView.as_view(), name="terms_es"),
    path(
        "es/descargo-de-responsabilidad/",
        DisclaimerView.as_view(),
        name="disclaimer_es",
    ),
]
