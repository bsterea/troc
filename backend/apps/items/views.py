from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Item


class ItemListView(ListView):
    """
    Displays available items.
    """

    model = Item
    template_name = "items/item_list.html"
    context_object_name = "items"

    def get_queryset(self):
        """
        Return only available items, newest first.
        """

        return Item.objects.filter(
            status=Item.STATUS_AVAILABLE
        ).order_by("-created_at")


class ItemDetailView(DetailView):
    """
    Displays item details.
    """

    model = Item
    template_name = "items/item_detail.html"
    context_object_name = "item"


class ItemCreateView(LoginRequiredMixin, CreateView):
    """
    Allows a logged-in user to create an item.
    """

    model = Item
    fields = [
        "category",
        "title",
        "description",
        "troc_value",
        "country",
        "region",
        "city",
        "local_area",
    ]
    template_name = "items/item_form.html"
    success_url = reverse_lazy("items:list")

    def form_valid(self, form):
        """
        Assign the logged-in user as item owner before saving.
        """

        form.instance.owner = self.request.user
        return super().form_valid(form)


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    """
    Allows the owner to edit an item.
    """

    model = Item
    fields = [
        "category",
        "title",
        "description",
        "troc_value",
        "country",
        "region",
        "city",
        "local_area",
        "status",
    ]
    template_name = "items/item_form.html"
    success_url = reverse_lazy("items:list")

    def get_queryset(self):
        """
        Restrict item editing to the logged-in owner.
        """

        return Item.objects.filter(owner=self.request.user)


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    """
    Allows the owner to delete an item.
    """

    model = Item
    template_name = "items/item_confirm_delete.html"
    success_url = reverse_lazy("items:list")

    def get_queryset(self):
        """
        Restrict item deletion to the logged-in owner.
        """

        return Item.objects.filter(owner=self.request.user)


# END OF FILE
