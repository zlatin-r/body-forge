from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class WorkoutType(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(
        max_length=100,
    )
    description = models.TextField(
        blank=True,
    )
    workout_type = models.ForeignKey(
        to=WorkoutType,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class MuscleGroup(models.Model):
    name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.name


class WorkoutSession(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE
    )
    workout_type = models.ForeignKey(
        to=WorkoutType,
        on_delete=models.SET_NULL,
        null=True,
    )
    date_started = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.user.username} - {self.workout_type} ({self.date_started.date()})"


class ExerciseSet(models.Model):
    workout_session = models.ForeignKey(
        to=WorkoutSession,
        on_delete=models.CASCADE,
    )
    exercise = models.ForeignKey(
        to=Exercise,
        on_delete=models.CASCADE,
    )
    muscle_group = models.ForeignKey(
        to=MuscleGroup,
        on_delete=models.SET_NULL,
        null=True,
    )
    series_number = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()
    weight_kg = models.FloatField()

    def __str__(self):
        return f"{self.exercise.name} - {self.repetitions} reps @ {self.weight_kg} kg"

