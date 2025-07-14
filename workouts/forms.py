from django import forms
from .models import Workout, MuscleGroup


class WorkoutStartForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ("muscle_group",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['muscle_group'].empty_label = None


class MuscleGroupCreateForm(forms.ModelForm):
    class Meta:
        model = MuscleGroup
        fields = ("name",)
