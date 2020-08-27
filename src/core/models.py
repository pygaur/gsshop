"""
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

from .abstract_models import AbstractUser


class Types(models.TextChoices):
    USER = "USER", "User"
    ADMIN = "ADMIN", "Admin"
    DASHBOARD_USER = "DASHBOARD_USER", "DASHBOARD_USER"


class User(AbstractUser):
    """
    custom user model
    """
    base_type = Types.USER

    # What type of user are we?
    type = models.CharField(
        _("Type"), max_length=50, choices=Types.choices, default=base_type
    )

