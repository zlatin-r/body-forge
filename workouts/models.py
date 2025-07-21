from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class MuscleGroup(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

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

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(
        max_length=100
    )
    muscle_group = models.ForeignKey(
        'MuscleGroup',
        on_delete=models.CASCADE,
        related_name='exercises',
    )

    def __str__(self):
        return f"{self.name} ({self.muscle_group})"


class Workout(models.Model):
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
    date_started = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"Workout on {self.date_started.strftime('%Y-%m-%d %H:%M')} by {self.user.profile.username}"

# class PerformedExercise(models.Model):
#     workout = models.ForeignKey(
#         Workout,
#         on_delete=models.CASCADE,
#         related_name='performed_exercises',
#     )
#     exercise = models.ForeignKey(
#         Exercise,
#         on_delete=models.CASCADE,
#         related_name='performed_instances',
#     )
#
#     def __str__(self):
#         return f"{self.exercise.name} in {self.workout}"


# class ExerciseSet(models.Model):
#     performed_exercise = models.ForeignKey(
#         PerformedExercise,
#         on_delete=models.CASCADE,
#         related_name='sets',
#     )
#     set_number = models.PositiveIntegerField()
#     repetitions = models.PositiveIntegerField()
#     weight = models.DecimalField(
#         max_digits=5,
#         decimal_places=2,
#     )
#
#     def __str__(self):
#         return f"Set {self.set_number} - {self.repetitions} reps @ {self.weight} kg"
