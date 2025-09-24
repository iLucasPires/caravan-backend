from pytest import fixture, mark
from rest_framework import status

from support.factories.caravan_factory import CaravanFactory, CaravanMemberFactory
from support.factories.user_factory import UserFactory


@fixture
def user():
    return UserFactory()


@fixture
def caravan():
    return CaravanFactory()


@fixture
def caravan_member(caravan, user):
    return CaravanMemberFactory(caravan=caravan, user=user)


@mark.django_db
class TestCaravanMemberAPI:
    BASE_URL = "/api/caravan/{}/members/"
    DETAIL_URL = "/api/caravan/{}/members/{}/"

    def get_base_url(self, caravan_id):
        return f"/api/caravan/{caravan_id}/members/"

    def test_list_caravan_members(self, auth_client, caravan):
        CaravanMemberFactory.create_batch(5, caravan=caravan)

        response = auth_client.get(self.BASE_URL.format(caravan.id))
        response_json = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert len(response_json) == 5

    def test_list_caravan_members_empty(self, auth_client, caravan):
        response = auth_client.get(self.BASE_URL.format(caravan.id))
        response_json = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert response_json == []

    def test_create_caravan_member(self, auth_client, caravan, user):
        caravan_member_data = CaravanMemberFactory.build(caravan=caravan, user=user)

        data = {
            "user": caravan_member_data.user.id,
            "caravan": caravan_member_data.caravan.id,
            "role": caravan_member_data.role,
        }

        response = auth_client.post(self.BASE_URL.format(caravan.id), data)
        response_json = response.json()

        assert response.status_code == status.HTTP_201_CREATED
        assert response_json["user"] == caravan_member_data.user.id

    def test_retrieve_caravan_member(self, auth_client, caravan_member):
        response = auth_client.get(
            self.DETAIL_URL.format(
                caravan_member.caravan.id,
                caravan_member.id,
            )
        )
        response_json = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert response_json["user"] == caravan_member.user.id

    def test_update_caravan_member(self, auth_client, caravan_member):
        new_user = UserFactory()
        caravan_member_data = CaravanMemberFactory.build(user=new_user)

        data = {
            "user": caravan_member_data.user.id,
            "caravan": caravan_member.caravan.id,
            "role": caravan_member_data.role,
        }

        response = auth_client.put(
            self.DETAIL_URL.format(
                caravan_member.caravan.id,
                caravan_member.id,
            ),
            data,
        )
        response_json = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert response_json["user"] == caravan_member_data.user.id

    def test_delete_caravan_member(self, auth_client, caravan_member):
        response = auth_client.delete(
            self.DETAIL_URL.format(
                caravan_member.caravan.id,
                caravan_member.id,
            )
        )
        assert response.status_code == status.HTTP_204_NO_CONTENT

        response = auth_client.get(
            self.DETAIL_URL.format(
                caravan_member.caravan.id,
                caravan_member.id,
            )
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND
