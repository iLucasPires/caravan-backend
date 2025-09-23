from django.db import models
from django.contrib.auth.models import User

from app.shared.models.timestamped import TimestampedModel
from app.shared.models.describable import DescribableModel


class Vehicle(TimestampedModel, DescribableModel):
    class Type(models.IntegerChoices):
        CAR = 1, "Car"
        TRUCK = 2, "Truck"
        MOTORCYCLE = 3, "Motorcycle"
        BUS = 4, "Bus"
        VAN = 5, "Van"
        OTHER = 6, "Other"

    class Status(models.IntegerChoices):
        ACTIVE = 1, "Active"
        INACTIVE = 2, "Inactive"
        MAINTENANCE = 3, "Maintenance"
        DECOMMISSIONED = 4, "Decommissioned"

    capacity = models.PositiveSmallIntegerField(
        help_text="Seating capacity of the vehicle",
    )

    type = models.PositiveSmallIntegerField(
        choices=Type.choices,
        default=Type.BUS,
        help_text="Type of the vehicle",
    )

    status = models.PositiveSmallIntegerField(
        choices=Status.choices,
        default=Status.ACTIVE,
        help_text="Current status of the vehicle",
    )


class VehicleLog(TimestampedModel):
    message = models.TextField(
        blank=True,
        null=True,
        help_text="Log message",
    )

    vehicle = models.ForeignKey(
        to=Vehicle,
        on_delete=models.CASCADE,
        related_name="logs",
        help_text="Vehicle associated with the log entry",
    )


class VehicleAssignment(TimestampedModel):
    class Role(models.IntegerChoices):
        DRIVER = 1, "Driver"
        NAVIGATOR = 2, "Navigator"
        PASSENGER = 3, "Passenger"
        MECHANIC = 4, "Mechanic"
        OTHER = 5, "Other"

    role = models.PositiveSmallIntegerField(
        choices=Role.choices,
        default=Role.PASSENGER,
        help_text="Role of the user in relation to the vehicle",
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="vehicle_assignments",
        help_text="User assigned to the vehicle",
    )

    vehicle = models.ForeignKey(
        to=Vehicle,
        on_delete=models.CASCADE,
        related_name="assignments",
        help_text="Vehicle to which the user is assigned",
    )
