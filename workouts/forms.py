from django import forms
from .models import Workout, MuscleGroup, WorkoutType


class WorkoutStartForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ("muscle_group",)

        widgets = {
            "muscle_group": forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields["muscle_group"].queryset = MuscleGroup.objects.filter(user=user)


class MuscleGroupCreateForm(forms.ModelForm):
    class Meta:
        model = MuscleGroup
        fields = ("name",)


class WorkoutTypeCreateForm(forms.ModelForm):
    class Meta:
        model = WorkoutType
        fields = ("name",)
