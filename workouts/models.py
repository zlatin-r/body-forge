from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.models import TimeStampedModel

UserModel = get_user_model()


class MuscleGroup(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='muscle_groups'
    )
    name = models.CharField(
        max_length=100,
    )

    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name


class WorkoutType(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='workout_types'
    )
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    muscle_group = models.ManyToManyField(
        'MuscleGroup',
        related_name='workout_types',
        blank=True,
    )

    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name


class Exercise(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='exercises'
    )
    name = models.CharField(
        max_length=100
    )
    muscle_group = models.ForeignKey(
        'MuscleGroup',
        on_delete=models.CASCADE,
        related_name='exercises',
    )
    # sets = models.

    class Meta:
        unique_together = ('user', 'name', 'muscle_group')

    def __str__(self):
        return f"{self.name} ({self.muscle_group.name})"


class Workout(TimeStampedModel):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name="workouts"
    )
    workout_type = models.ForeignKey(
        'WorkoutType',
        on_delete=models.SET_NULL,
        null=True,
        related_name="workouts",
    )

    def __str__(self):
        return f"Workout on {self.created.strftime('%Y-%m-%d %H:%M')} by {self.user.profile.username}"


class ExerciseSet(TimeStampedModel):
    exercise = models.ForeignKey(
        'Exercise',
        on_delete=models.CASCADE,
        related_name='sets',
    )
    repetitions = models.PositiveIntegerField()
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    def __str__(self):
        return f"{self.repetitions} reps @ {self.weight} kg"
