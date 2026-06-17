from django.db import models


class Category(models.Model):
    """
    Stores item categories used to classify goods and services.
    """

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    """
    Stores goods or services published by users for direct exchange.

    Location is designed to be international:
    - country: Romania, Denmark, Kenya, New Zealand
    - region: county, state, province, island, administrative area
    - city: city, town, village
    - local_area: optional local detail such as district, commune, neighborhood
    """

    STATUS_AVAILABLE = "available"
    STATUS_RESERVED = "reserved"
    STATUS_EXCHANGED = "exchanged"
    STATUS_REMOVED = "removed"

    STATUS_CHOICES = [
        (STATUS_AVAILABLE, "Available"),
        (STATUS_RESERVED, "Reserved"),
        (STATUS_EXCHANGED, "Exchanged"),
        (STATUS_REMOVED, "Removed"),
    ]

    owner = models.ForeignKey(
        "accounts.UserProfile",
        on_delete=models.CASCADE,
        related_name="items",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="items",
    )

    title = models.CharField(max_length=150)
    description = models.TextField()

    troc_value = models.PositiveIntegerField()

    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    local_area = models.CharField(max_length=100, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_AVAILABLE,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        location_parts = [self.city, self.region, self.country]
        location = ", ".join([part for part in location_parts if part])
        return f"{self.title} - {location}"


class ItemPhoto(models.Model):
    """
    Stores photos attached to an item.
    """

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name="photos",
    )

    image = models.ImageField(upload_to="items/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo for {self.item.title}"


class Favorite(models.Model):
    """
    Stores items saved by users for later review.
    """

    user = models.ForeignKey(
        "accounts.UserProfile",
        on_delete=models.CASCADE,
        related_name="favorites",
    )

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name="favorited_by",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "item")

    def __str__(self):
        return f"{self.user} -> {self.item}"
