from django.contrib import admin

from .models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "status",
        "subscribed_at",
        "confirmed_at",
        "automation_processed_at",
    )
    list_filter = ("status", "subscribed_at")
    search_fields = ("email",)
    readonly_fields = (
        "subscribed_at",
        "consent_at",
        "confirmed_at",
        "unsubscribed_at",
        "automation_processed_at",
    )
