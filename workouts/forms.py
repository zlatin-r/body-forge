from django import forms
from django.forms import modelformset_factory

from .models import WorkoutType, WorkoutSession, ExerciseSet, MuscleGroup, Workout, WorkoutSet


class StartWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['workout_type', 'muscle_groups']

    muscle_groups = forms.ModelMultipleChoiceField(
        queryset=MuscleGroup.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        help_text="Muscle Groups to Train"
    )


class CreateMuscleGroupForm(forms.ModelForm):
    class Meta:
        model = MuscleGroup
        fields = ['name']


class ExerciseSetForm(forms.ModelForm):
    class Meta:
        model = ExerciseSet
        fields = ['exercise', 'muscle_group', 'series_number', 'repetitions', 'weight_kg']


class WorkoutSetForm(forms.ModelForm):
    class Meta:
        model = WorkoutSet
        fields = ['exercise', 'set_number', 'repetitions', 'weight']
        widgets = {
            'exercise': forms.Select(attrs={'class': 'form-control'}),
            'set_number': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'repetitions': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.5}),
        }


WorkoutSetFormSet = modelformset_factory(
    WorkoutSet,
    form=WorkoutSetForm,
    extra=3,
    can_delete=False,
)
