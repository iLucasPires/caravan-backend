from django.db import models


class AbstractDescribable(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Name of the entity",
    )

    description = models.TextField(
        blank=True,
        help_text="Description of the entity",
    )

    class Meta:
        abstract = True
