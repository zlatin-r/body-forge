from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models


UserModel = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    username = models.CharField(
        max_length=30,
        blank=False,
        null=True,
    )
    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    height = models.DecimalField(
        max_digits=5,
        decimal_places=2,  # Supports 999.99cm
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0.01),
        ]
    )
    body_weight = models.DecimalField(
        max_digits=6,
        decimal_places=2,  # Supports 9999.99kg
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0.01)
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
        upload_to='profile_pictures/',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.username or self.user.email