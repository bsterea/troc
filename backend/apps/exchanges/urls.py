from django.urls import path

from .views import (
    ExchangeOfferCreateView,
    ExchangeOfferDetailView,
    ExchangeOfferItemCreateView,
    ExchangeOfferListView,
    ExchangeOfferUpdateView,
)

app_name = "exchanges"

urlpatterns = [
    path("", ExchangeOfferListView.as_view(), name="list"),
    path("create/", ExchangeOfferCreateView.as_view(), name="create"),
    path("<int:pk>/", ExchangeOfferDetailView.as_view(), name="detail"),
    path("<int:pk>/status/", ExchangeOfferUpdateView.as_view(), name="update_status"),
    path("items/add/", ExchangeOfferItemCreateView.as_view(), name="add_item"),
]
