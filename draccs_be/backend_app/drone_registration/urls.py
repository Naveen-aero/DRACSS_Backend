from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DroneRegistrationViewSet

router = DefaultRouter()
# Endpoint name requested: drone_registration
router.register(r"drone_registration", DroneRegistrationViewSet, basename="drone-registration")

urlpatterns = [
    path("", include(router.urls)),
]
