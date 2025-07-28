from django import forms
from django.core.exceptions import ValidationError

from workouts.models import Workout, WorkoutType, Exercise, MuscleGroup, ExerciseSet


class CreateWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['workout_type']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['workout_type'].queryset = WorkoutType.objects.filter(user=user)


class CreateWorkoutTypeForm(forms.ModelForm):
    class Meta:
        model = WorkoutType
        fields = ['name']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if WorkoutType.objects.filter(user=self.user, name__iexact=name).exists():
            raise forms.ValidationError("You already have a workout type with this name.")
        return name


# class CreateExerciseForm(forms.ModelForm):
#     class Meta:
#         model = Exercise
#         fields = ['name', 'muscle_group']
#
#     def __init__(self, *args, **kwargs):
#         self.user = kwargs.pop('user', None)
#         super().__init__(*args, **kwargs)
#         if self.user:
#             self.fields['muscle_group'].queryset = MuscleGroup.objects.filter(user=self.user)
#
#     def clean(self):
#         cleaned_data = super().clean()
#         name = cleaned_data.get('name')
#         muscle_group = cleaned_data.get('muscle_group')
#
#         if name and muscle_group:
#             if Exercise.objects.filter(user=self.user, name__iexact=name, muscle_group=muscle_group).exists():
#                 raise ValidationError("You already have an exercise with this name and muscle group.")
#
#         return cleaned_data
#
#
# class CreateMuscleGroupForm(forms.ModelForm):
#     class Meta:
#         model = MuscleGroup
#         fields = ['name']
#
#     def __init__(self, *args, **kwargs):
#         self.user = kwargs.pop('user', None)
#         super().__init__(*args, **kwargs)
#
#     def clean_name(self):
#         name = self.cleaned_data.get('name')
#         if MuscleGroup.objects.filter(user=self.user, name__iexact=name).exists():
#             raise forms.ValidationError("You already have a muscle group with this name.")
#         return name
#
#
# class CreateSetForm(forms.ModelForm):
#     class Meta:
#         model = ExerciseSet
#         fields = ['repetitions', 'weight']
#         widgets = {
#             'repetitions': forms.NumberInput(attrs={'min': 1}),
#             'weight': forms.NumberInput(attrs={'min': 0, 'step': '0.01'}),
#         }
