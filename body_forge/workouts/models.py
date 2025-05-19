from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Workout(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='workouts'
    )
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Name of the workout session"
    )
    date = models.DateField(
        default=timezone.now,
        help_text="Date when the workout occurred"
    )
    duration = models.DurationField(
        blank=True,
        null=True,
        help_text="Duration of the workout (HH:MM:SS)"
    )
    notes = models.TextField(
        blank=True,
        null=True,
        help_text="Additional notes about the workout"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name = "Workout"
        verbose_name_plural = "Workouts"

    def __str__(self):
        return f"{self.name or 'Unnamed Workout'} - {self.date.strftime('%Y-%m-%d')}"

    @property
    def exercises_count(self):
        """Returns the count of exercises in this workout"""
        return self.exercises.count()
