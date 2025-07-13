from django import forms
from .models import WorkoutType, WorkoutSession, ExerciseSet


class CreateWorkoutTypeForm(forms.ModelForm):
    class Meta:
        model = WorkoutType
        fields = ("name",)


class StartWorkoutSessionForm(forms.ModelForm):
    class Meta:
        model = WorkoutSession
        fields = ("workout_type",)



class ExerciseSetForm(forms.ModelForm):
    class Meta:
        model = ExerciseSet
        fields = ['exercise', 'muscle_group', 'series_number', 'repetitions', 'weight_kg']