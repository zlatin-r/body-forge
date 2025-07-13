from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView

from workouts.forms import (
    StartWorkoutForm,
    CreateMuscleGroupForm,
    CreateWorkoutTypeForm,
    ExerciseSetForm,
)
from workouts.models import (
    Workout,
    WorkoutType,
    MuscleGroup,
    WorkoutSession,
    Exercise,
    ExerciseSet,
)


class StartWorkoutView(LoginRequiredMixin, FormView):
    model = Workout
    form_class = StartWorkoutForm
    template_name = 'workouts/start-workout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workout_types"] = WorkoutType.objects.filter(user=self.request.user)
        return context

    def form_valid(self, form):
        workout = form.save(commit=False)
        workout.user = self.request.user
        workout.save()
        form.save_m2m()
        return redirect('add-exercises-to-workout', pk=workout.pk)

    def get_form(self):
        form = super().get_form()
        form.fields["workout_type"].queryset = WorkoutType.objects.filter(user=self.request.user)
        return form


class CreateWorkoutTypeView(LoginRequiredMixin, CreateView):
    model = WorkoutType
    form_class = CreateWorkoutTypeForm
    template_name = "workouts/wt-type-add-p.html"
    success_url = reverse_lazy("start-workout")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CreateMuscleGroupView(LoginRequiredMixin, CreateView):
    model = MuscleGroup
    form_class = CreateMuscleGroupForm
    success_url = reverse_lazy('start-workout')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_muscle_gps'] = MuscleGroup.objects.all()
        return context


class AddExerciseSetView(LoginRequiredMixin, CreateView):
    model = ExerciseSet
    form_class = ExerciseSetForm
    template_name = 'workouts/wt-add-set-p.html'

    def dispatch(self, request, *args, **kwargs):
        self.session = get_object_or_404(WorkoutSession, pk=kwargs['pk'], user=self.request.user)
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['exercise'].queryset = Exercise.objects.filter(workout_type=self.session.workout_type)
        return form

    def form_valid(self, form):
        form.instance.workout_session = self.session
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['session'] = self.session
        context['previous_sets'] = ExerciseSet.objects.filter(workout_session=self.session).order_by('series_number')
        return context

    def get_success_url(self):
        return reverse_lazy('add-exercises-to-workout', kwargs={'pk': self.session.pk})
