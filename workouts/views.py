from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, request
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView

from common.mixins import UserObjectOwnerMixin
from workouts.forms import (CreateWorkoutForm, CreateWorkoutTypeForm, CreateExerciseForm, CreateMuscleGroupForm,
                            CreateSetForm, )
from workouts.models import Workout, WorkoutType, Exercise, MuscleGroup, ExerciseSet


class CreateWorkoutView(LoginRequiredMixin, UserObjectOwnerMixin, CreateView):
    model = Workout
    form_class = CreateWorkoutForm
    template_name = 'workouts/wt-create.html'

    def get_success_url(self):
        return reverse_lazy('wt-details', kwargs={'workout_pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wt_types'] = WorkoutType.objects.filter(user=self.request.user)
        return context


class DetailsWorkoutView(LoginRequiredMixin, DetailView):
    model = Workout
    template_name = 'workouts/wt-details.html'
    context_object_name = 'workout'
    pk_url_kwarg = 'workout_pk'

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        workout = self.get_object()
        context['workout'] = workout
        context['exercises'] = self.object.exercises.all().prefetch_related('sets')
        return context


class CreateWorkoutTypeView(LoginRequiredMixin, UserObjectOwnerMixin, CreateView):
    model = WorkoutType
    form_class = CreateWorkoutTypeForm
    template_name = 'workouts/wt-type-create.html'

    def get_success_url(self):
        return reverse('wt-create')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class DeleteWorkoutTypeView(LoginRequiredMixin, DeleteView):
    model = WorkoutType

    def post(self, request, *args, **kwargs):
        workout_type = self.get_object()

        if workout_type.user == request.user:
            workout_type.delete()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False}, status=403)


class CreateExerciseView(LoginRequiredMixin, CreateView):
    model = Exercise
    form_class = CreateExerciseForm
    template_name = 'workouts/ex-create.html'

    def dispatch(self, request, *args, **kwargs):
        self.workout = Workout.objects.get(pk=kwargs['workout_pk'], user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.workout = self.workout
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('wt-details', kwargs={'workout_pk': self.workout.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['muscle_groups'] = MuscleGroup.objects.filter(user=self.request.user)
        context['workout'] = self.workout
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CreateMuscleGroupView(LoginRequiredMixin, UserObjectOwnerMixin, CreateView):
    model = MuscleGroup
    form_class = CreateMuscleGroupForm
    template_name = 'workouts/mg-create.html'

    def dispatch(self, request, *args, **kwargs):
        self.workout_pk = kwargs.get('workout_pk')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('ex-create', kwargs={'workout_pk': self.workout_pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workout_pk'] = self.workout_pk
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class DeleteMuscleGroupView(LoginRequiredMixin, DeleteView):
    model = MuscleGroup

    def post(self, request, *args, **kwargs):
        muscle_group = self.get_object()

        if muscle_group.user == request.user:
            muscle_group.delete()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=403)


class DeleteExerciseView(LoginRequiredMixin, DeleteView):
    model = Exercise

    def post(self, request, *args, **kwargs):
        exercise = self.get_object()

        if exercise.user == request.user:
            exercise.delete()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=403)


class CreateSetView(LoginRequiredMixin, CreateView):
    model = ExerciseSet
    form_class = CreateSetForm
    template_name = 'workouts/set-create.html'

    def form_valid(self, form):
        form.instance.exercise = self.exercise
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        self.workout = get_object_or_404(Workout, pk=kwargs['workout_pk'], user=request.user)
        self.exercise = get_object_or_404(Exercise, pk=kwargs['exercise_pk'], user=request.user, workout=self.workout)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workout'] = self.workout
        context['exercise'] = self.exercise
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse_lazy('wt-details', kwargs={'workout_pk': self.workout.pk})
#
#
