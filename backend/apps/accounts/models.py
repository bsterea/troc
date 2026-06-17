from django.db import models


class UserProfile(models.Model):
    """
    Stores the public and personal profile data for a Troc user.

    The phone number is the primary contact identifier, but it is not public.
    Email is optional.

    Location is designed to be international:
    - country: Romania, Denmark, Kenya, New Zealand
    - region: county, state, province, island, administrative area
    - city: city, town, village
    - local_area: optional local detail such as district, commune, neighborhood
    """

    ACCOUNT_STATUS_ACTIVE = "active"
    ACCOUNT_STATUS_SUSPENDED = "suspended"
    ACCOUNT_STATUS_DELETED = "deleted"

    ACCOUNT_STATUS_CHOICES = [
        (ACCOUNT_STATUS_ACTIVE, "Active"),
        (ACCOUNT_STATUS_SUSPENDED, "Suspended"),
        (ACCOUNT_STATUS_DELETED, "Deleted"),
    ]

    phone_number = models.CharField(max_length=30, unique=True)
    email = models.EmailField(blank=True, null=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    local_area = models.CharField(max_length=100, blank=True)

    account_status = models.CharField(
        max_length=20,
        choices=ACCOUNT_STATUS_CHOICES,
        default=ACCOUNT_STATUS_ACTIVE,
    )

    is_phone_public = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        location_parts = [self.city, self.region, self.country]
        location = ", ".join([part for part in location_parts if part])
        return f"{self.first_name} {self.last_name} - {location}"
