from django import forms
from .models import WorkoutType, WorkoutSession


class CreateWorkoutTypeForm(forms.ModelForm):
    class Meta:
        model = WorkoutType
        fields = ("name",)


class StartWorkoutSessionForm(forms.ModelForm):
    class Meta:
        model = WorkoutSession
        fields = ("workout_type",)
