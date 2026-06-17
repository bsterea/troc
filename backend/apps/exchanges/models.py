from django.db import models


class ExchangeOffer(models.Model):
    """
    Stores exchange proposals between users.
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

    offered_item = models.ForeignKey(
        "items.Item",
        on_delete=models.CASCADE,
        related_name="offers_made",
    )

    requested_item = models.ForeignKey(
        "items.Item",
        on_delete=models.CASCADE,
        related_name="offers_received",
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
        return (
            f"{self.sender} -> "
            f"{self.receiver} "
            f"({self.status})"
        )
