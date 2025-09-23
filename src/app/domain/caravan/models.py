from django.db import models
from django.contrib.auth.models import User

from app.domain.event.models import Event
from app.domain.vehicle.models import Verhicle

from app.shared.models.describable import AbstractDescribable
from app.shared.models.location import AbstractLocation
from app.shared.models.timestamped import AbstractTimeStamped


class Caravan(AbstractDescribable, AbstractTimeStamped):
    event = models.ForeignKey(
        to=Event,
        on_delete=models.CASCADE,
        related_name="caravans",
        help_text="Event associated with the caravan",
    )

    vehicle = models.ForeignKey(
        to=Verhicle,
        on_delete=models.CASCADE,
        related_name="caravans",
        help_text="Vehicle used for the caravan",
    )

    @property
    def stops(self) -> list["CaravanStop"] | None:
        return self.stops.all().order_by("time")


class CaravanMember(AbstractTimeStamped):
    class Role(models.IntegerChoices):
        LEADER = 1, "Leader"
        MEMBER = 2, "Member"
        SUPPORT = 3, "Support"
        OTHER = 4, "Other"

    role = models.PositiveSmallIntegerField(
        choices=Role.choices,
        default=Role.MEMBER,
        help_text="Role of the member in the caravan",
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="caravan_memberships",
        help_text="User who is a member of the caravan",
    )

    caravan = models.ForeignKey(
        to=Caravan,
        on_delete=models.CASCADE,
        related_name="members",
        help_text="Caravan to which the member belongs",
    )


class CaravanStop(AbstractTimeStamped):
    class Type(models.IntegerChoices):
        START = 0, "Start"
        REST = 1, "Rest"
        REFUEL = 2, "Refuel"
        MAINTENANCE = 3, "Maintenance"
        OTHER = 4, "Other"
        END = 5, "End"

    time = models.DateTimeField(
        help_text="Scheduled time for the stop",
    )

    type = models.IntegerField(
        choices=Type.choices,
        default=Type.OTHER,
        help_text="Type of the stop",
    )

    notes = models.TextField(
        blank=True,
        help_text="Additional notes about the stop",
    )

    caravan = models.ForeignKey(
        to=Caravan,
        on_delete=models.CASCADE,
        related_name="stops",
        help_text="Caravan associated with the stop",
    )

    @property
    def location(self) -> "CaravanStopLocation" | None:
        return getattr(self, "location", None)


class CaravanStopLocation(AbstractTimeStamped, AbstractLocation):
    stop = models.OneToOneField(
        to=CaravanStop,
        on_delete=models.CASCADE,
        related_name="location",
        help_text="Caravan stop associated with the location",
    )
