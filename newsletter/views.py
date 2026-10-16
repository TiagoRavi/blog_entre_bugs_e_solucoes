
from django.contrib import messages
from django.db import IntegrityError, transaction
from django.shortcuts import redirect
from django.utils import timezone
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from .forms import SubscriptionForm
from .models import Subscriber


@require_POST
def subscribe(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        messages.error(
            request,
            "Informe um e-mail válido e aceite receber a newsletter.",
        )
        return redirect("pages:about")

    email = form.cleaned_data["email"]

    try:
        with transaction.atomic():
            subscriber, created = Subscriber.objects.get_or_create(
                email=email,
                defaults={
                    "consent_at": timezone.now(),
                    "consent_text_version": "v1",
                    "status": Subscriber.Status.PENDING,
                },
            )
    except IntegrityError:
        subscriber = Subscriber.objects.filter(email=email).first()
        created = False

    if created:
        messages.success(
            request,
            "Cadastro recebido! A confirmação por e-mail ainda precisa ser implementada.",
        )
    elif subscriber and subscriber.status == Subscriber.Status.ACTIVE:
        messages.info(
            request,
            "Este e-mail já está inscrito na newsletter.",
        )
    elif subscriber:
        messages.info(
            request,
            "Este e-mail já possui um cadastro pendente de confirmação.",
        )
    else:
        messages.error(
            request,
            "Não foi possível concluir o cadastro. Tente novamente.",
        )

    next_url = request.POST.get("next", "")
    if not next_url or not url_has_allowed_host_and_scheme(
        next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        next_url = "/"

    return redirect(next_url)
