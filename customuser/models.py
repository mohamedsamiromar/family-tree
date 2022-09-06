from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(
        verbose_name=_('username'), db_index=True, unique=True, max_length=255)
    first_name = models.CharField(verbose_name=_('first_name'), max_length=150)
    middle_name = models.CharField(
        verbose_name=_('middle_name'), max_length=150, default=False)
    last_name = models.CharField(verbose_name=_('last_name'), max_length=255)
    email = models.EmailField(verbose_name=_('email'), unique=True)
    birth_date = models.DateField(null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"


