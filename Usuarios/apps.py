from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Usuarios'

    def ready(self):
        import Usuarios.signals  # Reemplaza 'miapp' con el nombre real de tu aplicación