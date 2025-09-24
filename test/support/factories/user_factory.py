from django.contrib.auth.models import User

from factory import Faker
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    username = Faker("user_name")
    email = Faker("email")
    first_name = Faker("first_name")
    last_name = Faker("last_name")

    class Meta:
        model = User
