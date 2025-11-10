from rest_framework import viewsets, permissions, filters
from .models import DroneRegistration
from .serializers import DroneRegistrationSerializer

class DroneRegistrationViewSet(viewsets.ModelViewSet):
    queryset = DroneRegistration.objects.all()
    serializer_class = DroneRegistrationSerializer
    permission_classes = [permissions.AllowAny]  # tighten later
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        "model_name", "uin_number", "drone_serial_number",
        "manufacturer", "drone_type", "flight_controller_serial_number",
        "remote_controller", "battery_serial_number_1", "battery_serial_number_2",
    ]
    ordering_fields = ["created_at", "model_name", "uin_number", "drone_serial_number"]
    ordering = ["-created_at"]
