from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView

from .models import Notification


class HomeView(TemplateView):
    """
    Displays the public home page.
    """

    template_name = "core/home.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    """
    Displays the logged-in user's dashboard.
    """

    template_name = "core/dashboard.html"


class NotificationListView(LoginRequiredMixin, ListView):
    """
    Displays notifications for the logged-in user.
    """

    model = Notification
    template_name = "core/notification_list.html"
    context_object_name = "notifications"

    def get_queryset(self):
        return Notification.objects.filter(
            user=self.request.user
        ).order_by("-created_at")
