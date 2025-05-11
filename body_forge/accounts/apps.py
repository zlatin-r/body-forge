from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'body_forge.accounts'

    def ready(self):
        import body_forge.accounts.signals
