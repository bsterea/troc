from django.contrib import admin

from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """
    Admin configuration for user notifications.
    """

    list_display = (
        "id",
        "user",
        "notification_type",
        "title",
        "is_read",
        "created_at",
    )

    list_filter = (
        "notification_type",
        "is_read",
        "created_at",
    )

    search_fields = (
        "user__phone_number",
        "user__first_name",
        "user__last_name",
        "title",
        "message",
    )

    readonly_fields = (
        "created_at",
    )
