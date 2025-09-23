from django.db import models
from django.core.exceptions import ValidationError

from app.shared.models.location import AbstractLocation
from app.shared.models.describable import AbstractDescribable
from app.shared.models.timestamped import AbstractTimeStamped


class Event(AbstractTimeStamped, AbstractDescribable):
    @property
    def location(self) -> EventLocation | None:
        return self.locations.first()

    @property
    def schedules(self) -> list[EventSchedule] | None:
        return self.schedules.all()


class EventLocation(AbstractLocation, AbstractTimeStamped):
    event = models.ForeignKey(
        to=Event,
        on_delete=models.CASCADE,
        related_name="locations",
        help_text="Event associated with the location",
    )

    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.state}, {self.country}"


class EventSchedule(AbstractTimeStamped):
    start_datetime = models.DateTimeField(
        help_text="Start date and time of the event",
    )

    end_datetime = models.DateTimeField(
        help_text="End date and time of the event",
    )

    event = models.ForeignKey(
        to=Event,
        on_delete=models.CASCADE,
        related_name="schedules",
        help_text="Event associated with the schedule",
    )

    def clean(self) -> None:
        if self.end_datetime <= self.start_datetime:
            raise ValidationError("End datetime must be after start datetime")

    def __str__(self) -> str:
        return f"{self.start_datetime} - {self.end_datetime}"
