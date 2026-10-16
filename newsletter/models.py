from django.db import models
from django.utils import timezone


class Subscriber(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pendente"
        ACTIVE = "active", "Ativo"
        UNSUBSCRIBED = "unsubscribed", "Cancelado"

    email = models.EmailField(max_length=254, unique=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        db_index=True,
    )
    consent_at = models.DateTimeField()
    consent_text_version = models.CharField(
        max_length=20,
        default="v1",
    )
    subscribed_at = models.DateTimeField(default=timezone.now)
    confirmed_at = models.DateTimeField(null=True, blank=True)
    unsubscribed_at = models.DateTimeField(null=True, blank=True)
    automation_processed_at = models.DateTimeField(
        null=True,
        blank=True,
        db_index=True,
    )

    class Meta:
        ordering = ["-subscribed_at"]
        verbose_name = "Inscrito na newsletter"
        verbose_name_plural = "Inscritos na newsletter"

    def __str__(self):
        return self.email