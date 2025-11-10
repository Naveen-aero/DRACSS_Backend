from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet

router = DefaultRouter()  # expects a trailing slash
router.register(r"accounts", AccountViewSet, basename="account")

urlpatterns = [
    path("", include(router.urls)),
]
