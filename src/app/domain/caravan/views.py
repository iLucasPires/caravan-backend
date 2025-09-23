from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from app.domain.caravan.models import (
    Caravan,
    CaravanMember,
    CaravanStop,
    CaravanStopLocation,
)
from app.domain.caravan.serializers import (
    CaravanSerializer,
    CaravanMemberSerializer,
    CaravanStopSerializer,
    CaravanStopLocationSerializer,
)


@extend_schema(tags=["Caravan"])
class CaravanViewSet(viewsets.ModelViewSet):
    queryset = Caravan.objects.all()
    serializer_class = CaravanSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(tags=["Caravan Members"])
class CaravanMemberViewSet(viewsets.ModelViewSet):
    queryset = CaravanMember.objects.all()
    serializer_class = CaravanMemberSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(tags=["Caravan Stops"])
class CaravanStopViewSet(viewsets.ModelViewSet):
    queryset = CaravanStop.objects.all()
    serializer_class = CaravanStopSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(tags=["Caravan Stop Locations"])
class CaravanStopLocationViewSet(viewsets.ModelViewSet):
    queryset = CaravanStopLocation.objects.all()
    serializer_class = CaravanStopLocationSerializer
    permission_classes = [IsAuthenticated]
