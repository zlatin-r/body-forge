from django import forms

from workouts.models import MuscleGroup, Workout


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


# class StartWorkoutForm(forms.ModelForm):
#     muscle_groups = forms.ModelMultipleChoiceField(
#         queryset=MuscleGroup.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=True,
#         label="Muscle Groups to Train"
#     )
#
#     class Meta:
#         model = Workout
#         fields = ['workout_type', 'muscle_groups']
#         widgets = {
#             'workout_type': forms.Select(attrs={'class': 'form-control'}),
#         }
#
#
# class WorkoutSetForm(forms.ModelForm):
#     class Meta:
#         model = WorkoutSet
#         fields = ['exercise', 'set_number', 'repetitions', 'weight']
#         widgets = {
#             'exercise': forms.Select(attrs={'class': 'form-control'}),
#             'set_number': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
#             'repetitions': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
#             'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.5}),
#         }
#
#
# WorkoutSetFormSet = modelformset_factory(
#     WorkoutSet,
#     form=WorkoutSetForm,
#     extra=3,  # Number of empty forms to display
#     can_delete=False,
# )
