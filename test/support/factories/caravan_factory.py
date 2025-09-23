import factory
from django.utils import timezone

from app.domain.caravan.models import (
    Caravan,
    CaravanMember,
    CaravanStop,
    CaravanStopLocation,
)

from support.factories.user_factory import UserFactory
from support.factories.event_factory import EventFactory
from support.factories.vehicle_factory import VehicleFactory


class CaravanFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
    description = factory.Faker("text")
    event = factory.SubFactory(EventFactory)
    vehicle = factory.SubFactory(VehicleFactory)

    class Meta:
        model = Caravan


class CaravanMemberFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    caravan = factory.SubFactory(CaravanFactory)
    role = factory.Iterator(CaravanMember.Role.values)

    class Meta:
        model = CaravanMember


class CaravanStopFactory(factory.django.DjangoModelFactory):
    caravan = factory.SubFactory(CaravanFactory)
    time = factory.Faker("date_time", tzinfo=timezone.get_current_timezone())
    type = factory.Iterator(CaravanStop.Type.values)

    class Meta:
        model = CaravanStop


class CaravanStopLocationFactory(factory.django.DjangoModelFactory):
    stop = factory.SubFactory(CaravanStopFactory)
    street = factory.Faker("street_address")
    city = factory.Faker("city")
    state = factory.Faker("state")
    country = factory.Faker("country")
    latitude = factory.Faker("latitude")
    longitude = factory.Faker("longitude")

    class Meta:
        model = CaravanStopLocation
