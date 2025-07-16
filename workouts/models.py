from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class WorkoutType(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )


class MuscleGroup(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name="muscle_groups",
    )
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name


class Workout(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )
    workout_type = models.ManyToManyField(
        to=WorkoutType,
        related_name="workouts",
    )
    muscle_group = models.ManyToManyField(
        to=MuscleGroup,
        related_name="workouts",
    )
    date_started = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"Workout on {self.date_started.strftime('%Y-%m-%d %H:%M')} by {self.user.username}"
