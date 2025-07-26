from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView

from common.mixins import UserObjectOwnerMixin
from workouts.forms import CreateWorkoutForm, CreateWorkoutTypeForm, CreateExerciseForm, CreateMuscleGroupForm, \
    CreateSetForm
from workouts.models import Workout, WorkoutType, Exercise, MuscleGroup, ExerciseSet


class CreateWorkoutView(LoginRequiredMixin, UserObjectOwnerMixin, CreateView):
    model = Workout
    form_class = CreateWorkoutForm
    template_name = 'workouts/wt-start.html'

    def get_success_url(self):
        return reverse_lazy('dashboard', kwargs={'pk': self.request.user.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wt_types'] = WorkoutType.objects.filter(user=self.request.user)
        context['exercises'] = Exercise.objects.filter(user=self.request.user).prefetch_related('sets')
        return context


class CreateWorkoutTypeView(LoginRequiredMixin, UserObjectOwnerMixin, CreateView):
    model = WorkoutType
    form_class = CreateWorkoutTypeForm
    template_name = 'workouts/wt-type-create.html'

    def get_success_url(self):
        return reverse('wt-start')


class DeleteWorkoutTypeView(LoginRequiredMixin, DeleteView):
    model = WorkoutType

    def post(self, request, *args, **kwargs):
        workout_type = self.get_object()

        if workout_type.user == request.user:
            workout_type.delete()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False}, status=403)


class CreateExerciseView(LoginRequiredMixin, UserObjectOwnerMixin, CreateView):
    model = Exercise
    form_class = CreateExerciseForm
    template_name = 'workouts/ex-start.html'

    def get_success_url(self):
        return reverse_lazy('ex-details', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['muscle_groups'] = MuscleGroup.objects.filter(user=self.request.user)
        context['exercises'] = Exercise.objects.filter(user=self.request.user)
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CreateMuscleGroupView(LoginRequiredMixin, UserObjectOwnerMixin, CreateView):
    model = MuscleGroup
    form_class = CreateMuscleGroupForm
    template_name = 'workouts/mg-create.html'
    success_url = reverse_lazy('ex-start')


class ExerciseDetailsView(LoginRequiredMixin, DetailView):
    model = Exercise
    template_name = 'workouts/ex-details.html'
    context_object_name = 'exercise'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreateSetForm()
        return context


class CreateSetView(LoginRequiredMixin, CreateView):
    model = ExerciseSet
    form_class = CreateSetForm
    template_name = 'workouts/set-create.html'

    def form_valid(self, form):
        exercise_pk = self.kwargs.get('pk')
        form.instance.exercise = Exercise.objects.get(pk=exercise_pk, user=self.request.user)
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        self.exercise = Exercise.objects.get(pk=kwargs['pk'], user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exercise'] = self.exercise
        return context

    def get_success_url(self):
        return reverse_lazy('wt-start')


class DeleteExerciseView(LoginRequiredMixin, DeleteView):
    model = Exercise

    def post(self, request, *args, **kwargs):
        exercise = self.get_object()

        if exercise.user == request.user:
            exercise.delete()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=403)


class DeleteMuscleGroupView(LoginRequiredMixin, DeleteView):
    model = MuscleGroup

    def post(self, request, *args, **kwargs):
        muscle_group = self.get_object()

        if muscle_group.user == request.user:
            muscle_group.delete()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=403)
