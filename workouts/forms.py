from django import forms
from .models import Workout, WorkoutType


class StartWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['workout_type']
        widgets = {
            'workout_type': forms.Select(attrs={'class': 'form-control'})
        }
