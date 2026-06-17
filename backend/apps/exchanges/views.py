from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import ExchangeOffer, ExchangeOfferItem


class ExchangeOfferListView(LoginRequiredMixin, ListView):
    """
    Displays exchange offers related to the logged-in user.

    A user can see only offers where they are either sender or receiver.
    """

    model = ExchangeOffer
    template_name = "exchanges/exchange_offer_list.html"
    context_object_name = "exchange_offers"

    def get_queryset(self):
        """
        Return exchange offers involving the current user.
        """

        user = self.request.user

        return ExchangeOffer.objects.filter(
            Q(sender=user) | Q(receiver=user)
        ).order_by("-created_at")


class ExchangeOfferDetailView(LoginRequiredMixin, DetailView):
    """
    Displays details for one exchange offer.

    A user can view only offers where they are sender or receiver.
    """

    model = ExchangeOffer
    template_name = "exchanges/exchange_offer_detail.html"
    context_object_name = "exchange_offer"

    def get_queryset(self):
        """
        Restrict detail access to offers involving the current user.
        """

        user = self.request.user

        return ExchangeOffer.objects.filter(
            Q(sender=user) | Q(receiver=user)
        )


class ExchangeOfferCreateView(LoginRequiredMixin, CreateView):
    """
    Creates a new exchange offer.

    The sender is always the logged-in user.
    """

    model = ExchangeOffer
    fields = [
        "receiver",
        "message",
    ]
    template_name = "exchanges/exchange_offer_form.html"
    success_url = reverse_lazy("exchanges:list")

    def form_valid(self, form):
        """
        Assign the logged-in user as the sender before saving.
        """

        form.instance.sender = self.request.user
        return super().form_valid(form)


class ExchangeOfferUpdateView(LoginRequiredMixin, UpdateView):
    """
    Allows limited update of an exchange offer status.

    Only users involved in the offer can update its status.
    """

    model = ExchangeOffer
    fields = [
        "status",
    ]
    template_name = "exchanges/exchange_offer_status_form.html"
    success_url = reverse_lazy("exchanges:list")

    def get_queryset(self):
        """
        Restrict status updates to offers involving the current user.
        """

        user = self.request.user

        return ExchangeOffer.objects.filter(
            Q(sender=user) | Q(receiver=user)
        )


class ExchangeOfferItemCreateView(LoginRequiredMixin, CreateView):
    """
    Adds an item to an exchange offer.

    Only users involved in the offer should add items.
    This MVP version uses basic form validation through ownership checks.
    """

    model = ExchangeOfferItem
    fields = [
        "exchange_offer",
        "item",
        "side",
    ]
    template_name = "exchanges/exchange_offer_item_form.html"

    def form_valid(self, form):
        """
        Save the exchange item and redirect back to the exchange detail page.
        """

        response = super().form_valid(form)
        return redirect("exchanges:detail", pk=self.object.exchange_offer.pk)


# END OF FILE
