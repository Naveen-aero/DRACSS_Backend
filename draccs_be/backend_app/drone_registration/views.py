from rest_framework import viewsets, permissions, filters
from rest_framework.parsers import MultiPartParser, FormParser
from .models import DroneRegistration
from .serializers import DroneRegistrationSerializer

class DroneRegistrationViewSet(viewsets.ModelViewSet):
    queryset = DroneRegistration.objects.all()
    serializer_class = DroneRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]  # adjust as per your app
    parser_classes = (MultiPartParser, FormParser)      #  enables image/file uploads

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        "model_name",
        "uin_number",
        "drone_serial_number",
        "drone_id",       #  NEW
        "manufacturer",
    ]
    ordering_fields = ["created_at", "model_name", "manufacturer", "registered"]  #  NEW
    ordering = ["-created_at"]
