from django import forms
from .models import WorkoutSession


class StartWorkoutSessionForm(forms.ModelForm):
    class Meta:
        model = WorkoutSession
        fields = ['workout_type']
        widgets = {
            'workout_type': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select workout type',
            }),
        }
        labels = {
            'workout_type': 'Workout Type',
        }

    def __init__(self, *args, **kwargs):
        super(StartWorkoutSessionForm, self).__init__(*args, **kwargs)
        self.fields['workout_type'].empty_label = "Choose workout type"


# class ExerciseForm(forms.ModelForm):
#     class Meta:
#         model = Exercise
#         fields = ['name', 'description', 'workout_type']
#
#
# class AddExerciseSetForm(forms.ModelForm):
#     class Meta:
#         model = ExerciseSet
#         fields = ['exercise', 'muscle_group', 'series_number', 'repetitions', 'weight_kg']
#         widgets = {
#             'series_number': forms.NumberInput(attrs={'min': 1}),
#             'repetitions': forms.NumberInput(attrs={'min': 1}),
#             'weight_kg': forms.NumberInput(attrs={'step': 0.5}),
#         }
