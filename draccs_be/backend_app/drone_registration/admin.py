from django.contrib import admin
from .models import DroneRegistration

@admin.register(DroneRegistration)
class DroneRegistrationAdmin(admin.ModelAdmin):
    list_display = (
        "id", "model_name", "uin_number", "drone_serial_number",
        "manufacturer", "is_active", "created_at",
    )
    search_fields = (
        "model_name", "uin_number", "drone_serial_number",
        "flight_controller_serial_number", "battery_serial_number_1",
        "battery_serial_number_2", "manufacturer", "drone_type",
    )
    list_filter = ("is_active", "manufacturer", "drone_type", "created_at")
