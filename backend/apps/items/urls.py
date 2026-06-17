from django.urls import path

from .views import (
    ItemCreateView,
    ItemDeleteView,
    ItemDetailView,
    ItemListView,
    ItemUpdateView,
)

app_name = "items"

urlpatterns = [
    path("", ItemListView.as_view(), name="list"),
    path("create/", ItemCreateView.as_view(), name="create"),
    path("<int:pk>/", ItemDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", ItemUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", ItemDeleteView.as_view(), name="delete"),
]
