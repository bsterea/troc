from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for Troc user profiles.
    """

    list_display = (
        "id",
        "phone_number",
        "email",
        "first_name",
        "last_name",
        "country",
        "region",
        "city",
        "account_status",
        "created_at",
    )

    list_filter = (
        "account_status",
        "country",
        "region",
        "city",
        "created_at",
    )

    search_fields = (
        "phone_number",
        "email",
        "first_name",
        "last_name",
        "country",
        "region",
        "city",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "deleted_at",
    )
