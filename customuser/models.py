from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You Must Provide Email Address"))

    def create_user(self, username, first_name, last_name, email, password, **extra_fields):
        if not username:
            raise ValueError(_("You Must Provide User Name"))
        if not first_name:
            raise ValueError(_("You Must Submit First Name"))
        if not last_name:
            raise ValueError(_("You Must Submit Last Name"))
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("An email Address is required"))

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        extra_fields.setdefault('is_stuff', False)
        extra_fields.setdefault('is_superuser', False)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, email, password, **extra_fields):
        extra_fields.setdefault('is_stuff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get("is_stuff") is not True:
            raise ValueError(_("Super User Must Be is_stuff "))

        if extra_fields.get("is_superuser") is not True:
            raise (_("Super User is Must Be is_superuser"))

        if not password:
            raise (_("Please, enter your password"))

        user = self.create_superuser(username, first_name, last_name, email, password, **extra_fields)
        user.save(using=self.db)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name=_('username'), db_index=True, unique=True, max_length=255)
    first_name = models.CharField(verbose_name=_('first_name'), max_length=150)
    last_name = models.CharField(verbose_name=_('last_name'), max_length=255)
    email = models.EmailField(verbose_name=_('email'), unique=True)
    birth_date = models.DateField(null=True)
    is_stuff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    obj = CustomUserManager()
    verbose_name = _("User")
    verbose_name_plural = _("User")

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"


