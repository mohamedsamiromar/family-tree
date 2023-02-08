from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from enum import Enum


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_by = models.DateTimeField(auto_now=True, null=True, blank=True)
    hidden = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        abstract = True


class GroupEnum(Enum):
    PERSON = 'person'
    ADMIN_GROUP = 'Admin'


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
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return False

    @property
    def full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"



class LoginLog(TimeStampedModel):
    email = models.EmailField(null=True)

    def __str__(self):
        return '{} Logged in at {}'.format(self.username, self.created_at)


