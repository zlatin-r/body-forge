from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator
from django.db import models

from accounts.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = "email"

    objects = AppUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    NAME_MAX_LENGTH = 30
    MAX_DIGITS = 5
    DECIMAL_PLACES = 2
    MIN_VALUE = 0.01

    UPLOAD_DIR = "profile_pictures/"

    user = models.OneToOneField(
        to=AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    username = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=False,
        null=True,
    )
    first_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=True,
        null=True,
    )
    height = models.DecimalField(
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES,
        blank=True,
        null=True,
        validators=[
            MinValueValidator(MIN_VALUE),
        ]
    )
    body_weight = models.DecimalField(
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES,
        blank=True,
        null=True,
        validators=[
            MinValueValidator(MIN_VALUE)
        ]
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )
    date_joined = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True,
    )
    profile_picture = models.ImageField(
        upload_to=UPLOAD_DIR,
        blank=True,
        null=True,
    )

    @property
    def full_name(self):
        return f"{self.first_name or ''} {self.last_name or ''}"
