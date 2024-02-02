
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from apps.abstracts.abstract_model import BaseAbstractModel


class User(
    BaseAbstractModel,
    AbstractUser
):
    is_verified = models.BooleanField(
        _("user is verified"),
        default=False,
        help_text=_(
            _("Designates that this user is allowed to access to the api.")
        ),
    )

    def __str__(self):
        return f"{self.get_full_name()} - @{self.username}"

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
