from django.apps import AppConfig

class AuthModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_module'

class CoreConfig(AppConfig):
    name = 'auth_module'
    label = 'auth_module'
