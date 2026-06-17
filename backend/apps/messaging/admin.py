from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """
    Admin configuration for user messages.
    """

    list_display = (
        "id",
        "exchange_offer",
        "sender",
        "receiver",
        "created_at",
        "read_at",
    )

    list_filter = (
        "created_at",
        "read_at",
    )

    search_fields = (
        "sender__phone_number",
        "sender__first_name",
        "sender__last_name",
        "receiver__phone_number",
        "receiver__first_name",
        "receiver__last_name",
        "content",
    )

    readonly_fields = (
        "created_at",
        "read_at",
    )
