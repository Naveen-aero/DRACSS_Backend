from rest_framework import viewsets, permissions, filters
from .models import Account
from .serializers import AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.AllowAny]  # open for now
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "email", "phone", "employee_id", "designation", "client_type"]
    ordering_fields = ["created_at", "name", "email", "employee_id"]
    ordering = ["-created_at"]
