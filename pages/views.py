from django.views.generic import TemplateView
from django.shortcuts import render


class AboutView(TemplateView):
    template_name = "pages/about.html"


class ContactView(TemplateView):
    template_name = "pages/contact.html"


class PrivacyView(TemplateView):
    template_name = "pages/privacy.html"


class TermsView(TemplateView):
    template_name = "pages/terms.html"


class DisclaimerView(TemplateView):
    template_name = "pages/disclaimer.html"


def handler404(request, exception):
    return render(
        request,
        "errors/404.html",
        status=404,
    )


def handler500(request):
    return render(
        request,
        "errors/500.html",
        status=500,
    )