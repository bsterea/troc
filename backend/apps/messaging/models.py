from django.db import models


class Message(models.Model):
    """
    Stores messages exchanged between users.
    """

    exchange_offer = models.ForeignKey(
        "exchanges.ExchangeOffer",
        on_delete=models.CASCADE,
        related_name="messages",
    )

    sender = models.ForeignKey(
        "accounts.UserProfile",
        on_delete=models.CASCADE,
        related_name="sent_messages",
    )

    receiver = models.ForeignKey(
        "accounts.UserProfile",
        on_delete=models.CASCADE,
        related_name="received_messages",
    )

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return (
            f"Message from "
            f"{self.sender} "
            f"to "
            f"{self.receiver}"
        )
