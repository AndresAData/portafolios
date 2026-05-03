from django.apps import AppConfig


class PortafoliosConfig(AppConfig):
    name = 'my_apps.portafolios'

    def ready(self):
        import my_apps.portafolios.signals