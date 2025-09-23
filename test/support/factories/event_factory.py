import factory

from app.domain.event.models import Event


class EventFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
    description = factory.Faker("text")

    class Meta:
        model = Event
