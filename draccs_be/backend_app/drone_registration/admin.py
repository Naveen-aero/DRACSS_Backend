from django.contrib import admin
from django.utils.html import format_html
from .models import DroneRegistration

@admin.register(DroneRegistration)
class DroneRegistrationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "model_name",
        "uin_number",
        "drone_serial_number",
        "drone_id",
        "manufacturer",
        "registered",
        "is_active",
        "thumb",
        "created_at",
    )
    search_fields = (
        "model_name",
        "uin_number",
        "drone_serial_number",
        "drone_id",
        "flight_controller_serial_number",
        "battery_serial_number_1",
        "battery_serial_number_2",
        "manufacturer",
        "drone_type",
    )
    list_filter = ("registered", "is_active", "manufacturer", "drone_type", "created_at")
    readonly_fields = ("created_at", "updated_at", "thumb")

    #  All fields in a flat, simple layout (no section titles)
    fields = (
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
        "thumb",
        "registered",
        "is_active",
        "created_at",
        "updated_at",
    )

    def thumb(self, obj):
        if obj.image and hasattr(obj.image, "url"):
            return format_html('<img src="{}" style="height:60px;border-radius:6px;" />', obj.image.url)
        return "-"
    thumb.short_description = "Image"
