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
        "date_joined",
    )

    list_filter = (
        "account_status",
        "country",
        "region",
        "city",
        "date_joined",
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
        "date_joined",
        "last_login",
        "deleted_at",
    )


# END OF FILE
