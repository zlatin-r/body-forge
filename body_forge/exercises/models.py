from django.db import models

from body_forge.workouts.models import Workout


class Exercise(models.Model):
    WORKOUT_TYPES = (
        ('strength', 'Strength Training'),
        ('cardio', 'Cardio'),
        ('flexibility', 'Flexibility'),
        ('other', 'Other'),
    )

    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE,
        related_name='exercises'
    )
    name = models.CharField(max_length=100)
    exercise_type = models.CharField(
        max_length=20,
        choices=WORKOUT_TYPES,
        default='strength'
    )
    sets = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    reps = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    weight = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Weight in kg/lbs"
    )
    duration = models.DurationField(
        blank=True,
        null=True,
        help_text="Duration for cardio exercises"
    )
    distance = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Distance in km/miles for cardio"
    )
    notes = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['workout', 'id']

    def __str__(self):
        return f"{self.name} ({self.get_exercise_type_display()})"
