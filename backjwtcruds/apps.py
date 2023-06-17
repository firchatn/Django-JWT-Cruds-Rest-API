from django.apps import AppConfig


class BackjwtcrudsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "backjwtcruds"

    def ready(self):
        import backjwtcruds.signals

