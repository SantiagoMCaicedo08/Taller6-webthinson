from django.apps import AppConfig

class MainAppConfig(AppConfig):
    name = 'main_app'

    def ready(self):
        from . import signals  # Importar las señales para que se registren