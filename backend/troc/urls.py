from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("apps.core.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.accounts.urls")),
    path("items/", include("apps.items.urls")),
    path("exchanges/", include("apps.exchanges.urls")),
    path("messages/", include("apps.messaging.urls")),
]
