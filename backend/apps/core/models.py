
from django.db import models


class Notification(models.Model):
    """
    Stores user notifications.
    """

    TYPE_MESSAGE = "message"
    TYPE_EXCHANGE = "exchange"
    TYPE_SYSTEM = "system"

    TYPE_CHOICES = [
        (TYPE_MESSAGE, "Message"),
        (TYPE_EXCHANGE, "Exchange"),
        (TYPE_SYSTEM, "System"),
    ]

    user = models.ForeignKey(
        "accounts.UserProfile",
        on_delete=models.CASCADE,
        related_name="notifications",
    )

    notification_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
    )

    title = models.CharField(max_length=255)

    message = models.TextField()

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
