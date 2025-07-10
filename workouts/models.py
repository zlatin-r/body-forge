from django.contrib.auth import get_user, get_user_model
from django.db import models
from workouts.workout_type_choices import WorkoutTypes

User = get_user_model()


class Workout(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    workout_type = models.CharField(
        max_length=20,
        choices=WorkoutTypes,
    )
    date = models.DateField(
        auto_now_add=True,
    )
    notes = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.user} - {self.workout_type} on {self.date}"

    class Meta:
        ordering = ['-date']


class MuscleGroup(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    def __str__(self):
        return self.name


class WorkoutMuscleGroup(models.Model):
    workout = models.ForeignKey(
        to=Workout,
        on_delete=models.CASCADE,
        related_name='muscle_groups'
    )
    muscle_group = models.ForeignKey(
        to=MuscleGroup,
        on_delete=models.CASCADE
    )


class Exercise(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    muscle_group = models.ForeignKey(
        to=MuscleGroup,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name


class WorkoutSet(models.Model):
    workout = models.ForeignKey(
        to=Workout,
        on_delete=models.CASCADE,
        related_name='sets'
    )
    exercise = models.ForeignKey(
        to=Exercise,
        on_delete=models.CASCADE
    )
    set_number = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()
    weight = models.FloatField(
        help_text="In kilograms"
    )

    def __str__(self):
        return f"{self.exercise} | Set {self.set_number} | {self.repetitions} reps @ {self.weight} kg"
