from pytest import fixture, mark
from rest_framework import status

from support.factories.caravan_factory import CaravanFactory
from support.factories.user_factory import UserFactory
from support.factories.event_factory import EventFactory
from support.factories.vehicle_factory import VehicleFactory


@fixture
def user():
    return UserFactory()


@fixture
def caravan():
    return CaravanFactory()


@fixture
def event():
    return EventFactory()


@fixture
def vehicle():
    return VehicleFactory()


@mark.django_db
class TestCaravanAPI:
    BASE_URL = "/api/caravan/"

    def test_list_caravans(self, auth_client):
        CaravanFactory.create_batch(5)

        response = auth_client.get(self.BASE_URL)
        response_json = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert len(response_json) == 5

    def test_list_caravans_empty(self, auth_client):
        response = auth_client.get(self.BASE_URL)
        response_json = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert response_json == []

    def test_create_caravan(self, auth_client, event, vehicle):
        caravan_data = CaravanFactory.build(event=event, vehicle=vehicle)

        data = {
            "name": caravan_data.name,
            "description": caravan_data.description,
            "event": caravan_data.event.id,
            "vehicle": caravan_data.vehicle.id,
        }

        response = auth_client.post(self.BASE_URL, data)
        response_json = response.json()

        assert response.status_code == status.HTTP_201_CREATED
        assert response_json["name"] == caravan_data.name


    def test_create_caravan_duplicate_name(self, auth_client, event, vehicle):
        existing_caravan = CaravanFactory()
        caravan_data = CaravanFactory.build(event=event, vehicle=vehicle)

        data = {
            "name": existing_caravan.name,
            "description": caravan_data.description,
            "event": caravan_data.event.id,
            "vehicle": caravan_data.vehicle.id,
        }

        response = auth_client.post(self.BASE_URL, data)
        response_json = response.json()

        assert response.status_code == status.HTTP_201_CREATED
        assert response_json["name"] == existing_caravan.name
        
    def test_create_caravan_missing_required_fields(self, auth_client, event, vehicle):
        required_field = "name"
        caravan_data = CaravanFactory.build(event=event, vehicle=vehicle)

        data = {
            "name": caravan_data.name,
            "description": caravan_data.description,
            "event": caravan_data.event.id,
            "vehicle": caravan_data.vehicle.id,
        }

        data.pop(required_field)

        response = auth_client.post(self.BASE_URL, data)
        response_json = response.json()

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response_json.get(required_field)

    def test_retrieve_caravan(self, auth_client, caravan):
        response = auth_client.get(f"{self.BASE_URL}{caravan.id}/")
        response_json = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert response_json["name"] == caravan.name

    def test_update_caravan(self, auth_client, caravan, event, vehicle):
        caravan_data = CaravanFactory.build(event=event, vehicle=vehicle)

        data = {
            "name": caravan_data.name,
            "description": caravan_data.description,
            "event": caravan_data.event.id,
            "vehicle": caravan_data.vehicle.id,
        }

        response = auth_client.put(f"{self.BASE_URL}{caravan.id}/", data)
        response_json = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert response_json["name"] == caravan_data.name

    def test_delete_caravan(self, auth_client, caravan):
        response = auth_client.delete(f"{self.BASE_URL}{caravan.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT

        response = auth_client.get(f"{self.BASE_URL}{caravan.id}/")
        assert response.status_code == status.HTTP_404_NOT_FOUND
