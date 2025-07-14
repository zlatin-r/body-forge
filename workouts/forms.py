from django import forms
from .models import Workout, MuscleGroup


class WorkoutStartForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ("muscle_group",)


class MuscleGroupCreateForm(forms.ModelForm):
    class Meta:
        model = MuscleGroup
        fields = ("name",)
