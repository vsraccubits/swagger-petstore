from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for swaggerpetstore.
    """

    class UserStatuses(models.IntegerChoices):
        ACTIVE = 1, _("Active")
        INACTIVE = 2, _("Inactive")
        BLOCKED = 3, _("Blocked")
        DELETED = 4, _("Deleted")

    phone = models.CharField(max_length=12, verbose_name=_("User Phone"))
    user_status = models.PositiveSmallIntegerField(
        choices=UserStatuses.choices,
        default=UserStatuses.ACTIVE,
        verbose_name=_("User Status"),
    )

    def __str__(self):
        return self.email
