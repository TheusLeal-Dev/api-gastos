from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GastoViewSet

router = DefaultRouter()
router.register(r"gastos", GastoViewSet, basename="gastos")

urlpatterns = [
    path("", include(router.urls)),
]
