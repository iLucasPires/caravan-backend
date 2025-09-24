from factory import Faker
from factory.django import DjangoModelFactory

from app.domain.vehicle.models import Vehicle


class VehicleFactory(DjangoModelFactory):
    name = Faker("name")
    description = Faker("text")
    capacity = Faker("random_int", min=1, max=50)

    class Meta:
        model = Vehicle
