from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "q_n_a.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import q_n_a.users.signals  # noqa F401
        except ImportError:
            pass
