from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class MuscleGroup(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name="muscle_groups",
    )
    name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.name


class Workout(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )
    muscle_group = models.ManyToManyField(
        to=MuscleGroup,
        related_name="workouts",
    )
    date_started = models.DateTimeField(
        auto_now_add=True,
    )
