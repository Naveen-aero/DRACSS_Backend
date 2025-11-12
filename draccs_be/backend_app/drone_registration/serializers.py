from rest_framework import serializers
from .models import DroneRegistration

class DroneRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneRegistration
        fields = [
            "id",
            "model_name",
            "drone_type",
            "manufacturer",
            "uin_number",
            "drone_serial_number",
            "drone_id",                   
            "flight_controller_serial_number",
            "remote_controller",
            "battery_charger_serial_number",
            "battery_serial_number_1",
            "battery_serial_number_2",
            "attachment",
            "image",                 
            "registered",                
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_drone_id(self, value):
        # Allow blank/None; if provided, enforce uniqueness manually to support partial updates.
        if not value:
            return value
        qs = DroneRegistration.objects.filter(drone_id=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("drone_id must be unique.")
        return value
