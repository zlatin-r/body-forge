from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from workouts.forms import StartWorkoutForm, CreateMuscleGroupForm
from workouts.models import MuscleGroup, Workout


class StartWorkoutView(LoginRequiredMixin, FormView):
    model = Workout
    form_class = StartWorkoutForm
    template_name = 'workouts/start-workout.html'


class CreateMuscleGroupView(LoginRequiredMixin, CreateView):
    model = MuscleGroup
    form_class = CreateMuscleGroupForm
    success_url = reverse_lazy('workouts/start-workout')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_muscle_gps'] = MuscleGroup.objects.all()
        return context




# class StartWorkoutView(LoginRequiredMixin, FormView):
#     template_name = 'workouts/start-workout.html'
#     form_class = StartWorkoutForm
#
#     def form_valid(self, form):
#         workout = form.save(commit=False)
#         workout.user = self.request.user
#         workout.save()
#         return redirect('add-workout-sets', workout_id=workout.id)
#
#
# class AddWorkoutSetsView(LoginRequiredMixin, FormView):
#     template_name = 'workouts/add_sets.html'
#     form_class = WorkoutSetFormSet
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         workout = get_object_or_404(Workout, id=self.kwargs['workout_id'], user=self.request.user)
#         context['workout'] = workout
#         return context
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         workout = get_object_or_404(Workout, id=self.kwargs['workout_id'], user=self.request.user)
#         kwargs['queryset'] = WorkoutSet.objects.filter(workout=workout)
#         return kwargs
#
#     def form_valid(self, formset):
#         workout = get_object_or_404(Workout, id=self.kwargs['workout_id'], user=self.request.user)
#
#         for form in formset:
#             if form.cleaned_data:
#                 set_obj = form.save(commit=False)
#                 set_obj.workout = workout
#                 set_obj.save()
#
#         return redirect('workout-summary', workout_id=workout.id)
#
#
# class WorkoutSummaryView(LoginRequiredMixin, TemplateView):
#     template_name = 'workouts/workout_summary.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         workout = get_object_or_404(Workout, id=self.kwargs['workout_id'], user=self.request.user)
#         sets = WorkoutSet.objects.filter(workout=workout)
#         context['workout'] = workout
#         context['sets'] = sets
#         return context
