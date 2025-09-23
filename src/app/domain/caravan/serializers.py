from rest_framework import serializers

from app.domain.caravan.models import (
    Caravan,
    CaravanMember,
    CaravanStop,
    CaravanStopLocation,
)


class CaravanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caravan
        fields = "__all__"


class CaravanMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaravanMember
        fields = "__all__"


class CaravanStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaravanStop
        fields = "__all__"


class CaravanStopLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaravanStopLocation
        fields = "__all__"
