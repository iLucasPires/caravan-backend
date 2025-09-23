# app/domain/caravan/urls.py
from rest_framework_nested import routers

from app.domain.caravan.views import (
    CaravanViewSet,
    CaravanMemberViewSet,
    CaravanStopViewSet,
    CaravanStopLocationViewSet,
)

router = routers.SimpleRouter()

router.register(
    prefix=r"caravan",
    viewset=CaravanViewSet,
    basename="caravan",
)

# Nested routes for caravan
caravan_router = routers.NestedSimpleRouter(
    parent_router=router,
    parent_prefix=r"caravan",
    lookup="caravan",
)

caravan_router.register(
    prefix=r"stops",
    viewset=CaravanStopViewSet,
    basename="caravan-stops",
)

caravan_router.register(
    prefix=r"members",
    viewset=CaravanMemberViewSet,
    basename="caravan-members",
)

# Nested routes for caravan stops
stop_router = routers.NestedSimpleRouter(
    parent_router=caravan_router,
    parent_prefix=r"stops",
    lookup="stop",
)

stop_router.register(
    prefix=r"locations",
    viewset=CaravanStopLocationViewSet,
    basename="stop-locations",
)

urlpatterns = [
    *router.urls,
    *caravan_router.urls,
    *stop_router.urls,
]
