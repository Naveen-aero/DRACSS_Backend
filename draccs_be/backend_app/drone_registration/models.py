from django.db import models

def drone_attachment_path(instance, filename):
    # uploads to MEDIA_ROOT/drone_attachments/<uin>/<filename>
    uin = instance.uin_number or "no_uin"
    return f"drone_attachments/{uin}/{filename}"

class DroneRegistration(models.Model):
    model_name = models.CharField(max_length=120)
    drone_type = models.CharField(max_length=120, blank=True)
    manufacturer = models.CharField(max_length=120, blank=True)

    # Often unique identifiers
    uin_number = models.CharField(max_length=64, unique=True)
    drone_serial_number = models.CharField(max_length=120, unique=True)

    flight_controller_serial_number = models.CharField(max_length=120, blank=True)
    remote_controller = models.CharField(max_length=120, blank=True)
    battery_charger_serial_number = models.CharField(max_length=120, blank=True)
    battery_serial_number_1 = models.CharField(max_length=120, blank=True)
    battery_serial_number_2 = models.CharField(max_length=120, blank=True)

    # File upload (optional)
    attachment = models.FileField(upload_to=drone_attachment_path, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.model_name} / {self.uin_number}"
