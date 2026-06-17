from django.db import models


class ExchangeOffer(models.Model):
    """
    Stores an exchange proposal between two users.

    An exchange offer can contain one or more offered items
    and one or more requested items.

    This allows:
    - one item for one item
    - one item for multiple items
    - multiple items for one item
    - multiple items for multiple items
    - goods for services
    - services for goods
    """

    STATUS_PENDING = "pending"
    STATUS_ACCEPTED = "accepted"
    STATUS_REJECTED = "rejected"
    STATUS_CANCELLED = "cancelled"
    STATUS_COMPLETED = "completed"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_ACCEPTED, "Accepted"),
        (STATUS_REJECTED, "Rejected"),
        (STATUS_CANCELLED, "Cancelled"),
        (STATUS_COMPLETED, "Completed"),
    ]

    sender = models.ForeignKey(
        "accounts.UserProfile",
        on_delete=models.CASCADE,
        related_name="sent_exchange_offers",
    )

    receiver = models.ForeignKey(
        "accounts.UserProfile",
        on_delete=models.CASCADE,
        related_name="received_exchange_offers",
    )

    message = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.sender} -> {self.receiver} ({self.status})"


class ExchangeOfferItem(models.Model):
    """
    Stores the items included in an exchange offer.

    Each item belongs to one side of the offer:
    - offered: item offered by the sender
    - requested: item requested from the receiver
    """

    SIDE_OFFERED = "offered"
    SIDE_REQUESTED = "requested"

    SIDE_CHOICES = [
        (SIDE_OFFERED, "Offered"),
        (SIDE_REQUESTED, "Requested"),
    ]

    exchange_offer = models.ForeignKey(
        ExchangeOffer,
        on_delete=models.CASCADE,
        related_name="exchange_items",
    )

    item = models.ForeignKey(
        "items.Item",
        on_delete=models.CASCADE,
        related_name="exchange_offer_items",
    )

    side = models.CharField(
        max_length=20,
        choices=SIDE_CHOICES,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("exchange_offer", "item", "side")

    def __str__(self):
        return f"{self.exchange_offer} - {self.side} - {self.item}"
