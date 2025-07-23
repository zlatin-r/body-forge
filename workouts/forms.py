from django import forms

from workouts.models import Workout, WorkoutType, Exercise, MuscleGroup


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


class CreateExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'muscle_group']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # <-- important line
        super().__init__(*args, **kwargs)
        if user:
            self.fields['muscle_group'].queryset = MuscleGroup.objects.filter(user=user)


class CreateMuscleGroupForm(forms.ModelForm):
    class Meta:
        model = MuscleGroup
        fields = ['name']
