from django.apps import AppConfig

class UserModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_module'

class CoreConfig(AppConfig):
    name = 'user_module'
    label = 'user_module'
