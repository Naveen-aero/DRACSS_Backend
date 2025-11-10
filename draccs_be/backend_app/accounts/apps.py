from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "backend_app.accounts"   # must match your folder path
    # (optional) you can keep or drop this; app label will still be "accounts"
    # label = "accounts"
