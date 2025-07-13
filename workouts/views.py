from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from workouts.forms import StartWorkoutSessionForm, CreateWorkoutTypeForm, ExerciseSetForm
from workouts.models import WorkoutSession, WorkoutType, ExerciseSet, Exercise


class StartWorkoutSessionView(LoginRequiredMixin, CreateView):
    model = WorkoutSession
    template_name = "workouts/wt-start-p.html"
    form_class = StartWorkoutSessionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workout_types"] = WorkoutType.objects.filter(user=self.request.user)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form(self):
        form = super().get_form()
        form.fields["workout_type"].queryset = WorkoutType.objects.filter(user=self.request.user)
        return form

    def get_success_url(self):
        return reverse_lazy("add-exercises-to-workout", kwargs={"pk": self.object.pk})  # Adjust as needed


class CreateWorkoutTypeView(LoginRequiredMixin, CreateView):
    model = WorkoutType
    form_class = CreateWorkoutTypeForm
    template_name = "workouts/wt-type-add-p.html"
    success_url = reverse_lazy("start-workout")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteWorkoutTypeView(LoginRequiredMixin, DeleteView):
    model = WorkoutType
    success_url = reverse_lazy("start-workout")

    def post(self, request, *args, **kwargs):
        obj = self.get_object()

        if hasattr(obj, 'user') and obj.user != request.user:
            return HttpResponseForbidden()

        obj.delete()
        return redirect(self.success_url)


class AddExerciseSetView(LoginRequiredMixin, CreateView):
    model = ExerciseSet
    form_class = ExerciseSetForm
    template_name = 'workouts/wt-add-set-p.html'

    def dispatch(self, request, *args, **kwargs):
        self.session = get_object_or_404(WorkoutSession, pk=kwargs['pk'], user=self.request.user)
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Limit exercises to the session's workout type
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