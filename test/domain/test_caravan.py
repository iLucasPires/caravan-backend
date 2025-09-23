import pytest

from support.factories.caravan_factory import CaravanFactory
from support.factories.user_factory import UserFactory
from support.factories.event_factory import EventFactory
from support.factories.vehicle_factory import VehicleFactory


@pytest.mark.django_db
def test_list_caravans(client):
    user = UserFactory()
    client.force_authenticate(user=user)
    CaravanFactory.create_batch(5)

    response = client.get("/api/caravan/")
    response_json = response.json()

    assert response.status_code == 200
    assert len(response_json) == 5


@pytest.mark.django_db
def test_create_caravan(client):
    user = UserFactory()
    client.force_authenticate(user=user)

    event = EventFactory()
    vehicle = VehicleFactory()

    data = {
        "name": "My Caravan",
        "description": "A caravan for testing",
        "event": event.id,
        "vehicle": vehicle.id,
    }

    response = client.post("/api/caravan/", data=data)
    response_json = response.json()

    assert response.status_code == 201
    assert response_json["name"] == "My Caravan"
    assert response_json["description"] == "A caravan for testing"
    assert response_json["event"] == event.id
    assert response_json["vehicle"] == vehicle.id
