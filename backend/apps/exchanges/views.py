from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import ExchangeOffer, ExchangeOfferItem


class ExchangeOfferListView(LoginRequiredMixin, ListView):
    """
    Displays exchange offers related to the logged-in user.
    """

    model = ExchangeOffer
    template_name = "exchanges/exchange_offer_list.html"
    context_object_name = "exchange_offers"

    def get_queryset(self):
        user = self.request.user
        return ExchangeOffer.objects.filter(
            sender=user
        ) | ExchangeOffer.objects.filter(
            receiver=user
        )


class ExchangeOfferDetailView(LoginRequiredMixin, DetailView):
    """
    Displays details for one exchange offer.
    """

    model = ExchangeOffer
    template_name = "exchanges/exchange_offer_detail.html"
    context_object_name = "exchange_offer"


class ExchangeOfferCreateView(LoginRequiredMixin, CreateView):
    """
    Creates a new exchange offer.
    """

    model = ExchangeOffer
    fields = [
        "receiver",
        "message",
    ]
    template_name = "exchanges/exchange_offer_form.html"
    success_url = reverse_lazy("exchanges:list")

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)


class ExchangeOfferUpdateView(LoginRequiredMixin, UpdateView):
    """
    Allows limited update of an exchange offer status.
    """

    model = ExchangeOffer
    fields = [
        "status",
    ]
    template_name = "exchanges/exchange_offer_status_form.html"
    success_url = reverse_lazy("exchanges:list")


class ExchangeOfferItemCreateView(LoginRequiredMixin, CreateView):
    """
    Adds an item to an exchange offer.
    """

    model = ExchangeOfferItem
    fields = [
        "exchange_offer",
        "item",
        "side",
    ]
    template_name = "exchanges/exchange_offer_item_form.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect("exchanges:detail", pk=self.object.exchange_offer.pk)
