from django.db import models


class AbstractLocation(models.Model):
    street = models.CharField(
        max_length=200,
        help_text="Street address",
    )

    city = models.CharField(
        max_length=100,
        help_text="City",
    )

    state = models.CharField(
        max_length=100,
        help_text="State or province",
    )

    country = models.CharField(
        max_length=100,
        help_text="Country",
    )

    postal_code = models.CharField(
        max_length=20,
        blank=True,
        help_text="Postal code",
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        help_text="Longitude",
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        help_text="Latitude",
    )

    class Meta:
        abstract = True