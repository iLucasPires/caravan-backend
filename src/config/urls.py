from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/redoc/", SpectacularRedocView.as_view(), name="redoc"),
    path("api/docs/", SpectacularSwaggerView.as_view(), name="docs"),
]

urlpatterns += [
    path("api/", include("djoser.urls")),
    path("api/", include("djoser.urls.jwt")),
]

urlpatterns += [
    path("api/", include("app.domain.caravan.urls")),
]
