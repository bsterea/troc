from django.urls import path

from .views import (
    MessageCreateView,
    MessageListView,
)

app_name = "messaging"

urlpatterns = [
    path("", MessageListView.as_view(), name="list"),
    path("send/", MessageCreateView.as_view(), name="send"),
]
