from django.contrib import admin

from .models import ExchangeOffer, ExchangeOfferItem


class ExchangeOfferItemInline(admin.TabularInline):
    """
    Allows exchange offer items to be managed inside an exchange offer.
    """

    model = ExchangeOfferItem
    extra = 1


@admin.register(ExchangeOffer)
class ExchangeOfferAdmin(admin.ModelAdmin):
    """
    Admin configuration for exchange offers.
    """

    list_display = (
        "id",
        "sender",
        "receiver",
        "status",
        "created_at",
        "completed_at",
    )

    list_filter = (
        "status",
        "created_at",
        "completed_at",
    )

    search_fields = (
        "sender__phone_number",
        "sender__first_name",
        "sender__last_name",
        "receiver__phone_number",
        "receiver__first_name",
        "receiver__last_name",
        "message",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "completed_at",
    )

    inlines = [ExchangeOfferItemInline]


@admin.register(ExchangeOfferItem)
class ExchangeOfferItemAdmin(admin.ModelAdmin):
    """
    Admin configuration for items included in exchange offers.
    """

    list_display = (
        "id",
        "exchange_offer",
        "item",
        "side",
        "created_at",
    )

    list_filter = (
        "side",
        "created_at",
    )

    search_fields = (
        "item__title",
        "exchange_offer__sender__phone_number",
        "exchange_offer__receiver__phone_number",
    )

    readonly_fields = (
        "created_at",
    )
