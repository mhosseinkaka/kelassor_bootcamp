from django.apps import AppConfig


class ForeignVillaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'foreign_villa'

    def ready(self):
        import foreign_villa.signals