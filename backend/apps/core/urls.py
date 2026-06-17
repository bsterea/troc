from django.urls import path

from .views import (
    DashboardView,
    HomeView,
    NotificationListView,
)

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("notifications/", NotificationListView.as_view(), name="notifications"),
]
