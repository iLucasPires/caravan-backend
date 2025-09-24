from factory import Faker
from factory.django import DjangoModelFactory

from app.domain.event.models import Event


class EventFactory(DjangoModelFactory):
    name = Faker("name")
    description = Faker("text")

    class Meta:
        model = Event
