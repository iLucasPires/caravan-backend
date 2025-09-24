from factory import Faker, SubFactory, Iterator
from factory.django import DjangoModelFactory

from app.domain.caravan.models import (
    Caravan,
    CaravanMember,
    CaravanStop,
    CaravanStopLocation,
)

from support.factories.user_factory import UserFactory
from support.factories.event_factory import EventFactory
from support.factories.vehicle_factory import VehicleFactory


class CaravanFactory(DjangoModelFactory):
    name = Faker("name")
    description = Faker("text")
    event = SubFactory(EventFactory)
    vehicle = SubFactory(VehicleFactory)

    class Meta:
        model = Caravan


class CaravanMemberFactory(DjangoModelFactory):
    user = SubFactory(UserFactory)
    caravan = SubFactory(CaravanFactory)
    role = Iterator(CaravanMember.Role.values)

    class Meta:
        model = CaravanMember


class CaravanStopFactory(DjangoModelFactory):
    caravan = SubFactory(CaravanFactory)
    time = Faker("date_time")
    type = Iterator(CaravanStop.Type.values)

    class Meta:
        model = CaravanStop


class CaravanStopLocationFactory(DjangoModelFactory):
    stop = SubFactory(CaravanStopFactory)
    street = Faker("street_address")
    city = Faker("city")
    state = Faker("state")
    country = Faker("country")
    latitude = Faker("latitude")
    longitude = Faker("longitude")

    class Meta:
        model = CaravanStopLocation
