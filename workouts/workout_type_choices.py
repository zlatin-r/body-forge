from django.db import models


class WorkoutTypes(models.TextChoices):
    STRENGTH = 'Strength', 'Strength'
    CARDIO = 'Cardio', 'Cardio'
    MIXED = "Mixed", "Mixed"
    OTHER = "Other", "Other"
