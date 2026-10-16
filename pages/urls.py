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
    path("sobre/", AboutView.as_view(), name="about"),
    path("about-author/", AboutAuthorView.as_view(), name="about_author"),
    path("contato/", ContactView.as_view(), name="contact"),
    path("politica-de-privacidade/", PrivacyView.as_view(), name="privacy"),
    path("termos-de-uso/", TermsView.as_view(), name="terms"),
    path("disclaimer/", DisclaimerView.as_view(), name="disclaimer"),
    
]
