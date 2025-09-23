import factory

from app.domain.vehicle.models import Vehicle


class VehicleFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
    description = factory.Faker("text")
    capacity = factory.Faker("random_int", min=1, max=50)

    class Meta:
        model = Vehicle
