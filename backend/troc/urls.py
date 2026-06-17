from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# Main URL configuration for the Troc project.
urlpatterns = [
    path("", include("apps.core.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.accounts.urls")),
    path("items/", include("apps.items.urls")),
    path("exchanges/", include("apps.exchanges.urls")),
    path("messages/", include("apps.messaging.urls")),
]

# Serve uploaded media files during development.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# END OF FILE
