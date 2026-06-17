from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import Message


class MessageListView(LoginRequiredMixin, ListView):
    """
    Displays messages related to the logged-in user.

    The user can see both received and sent messages.
    """

    model = Message
    template_name = "messaging/message_list.html"
    context_object_name = "messages"

    def get_queryset(self):
        """
        Return sent and received messages for the current user.
        """

        user = self.request.user

        return Message.objects.filter(
            Q(sender=user) | Q(receiver=user)
        ).order_by("-created_at")


class MessageCreateView(LoginRequiredMixin, CreateView):
    """
    Allows a logged-in user to send a message.
    """

    model = Message
    fields = [
        "exchange_offer",
        "receiver",
        "content",
    ]
    template_name = "messaging/message_form.html"
    success_url = reverse_lazy("messaging:list")

    def form_valid(self, form):
        """
        Assign the logged-in user as message sender.
        """

        form.instance.sender = self.request.user
        return super().form_valid(form)


# END OF FILE
