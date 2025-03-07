from django.apps import AppConfig


class SocialmediaAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'socialmedia_app'

    def ready(self):
        import socialmedia_app.signals  # Import signals
