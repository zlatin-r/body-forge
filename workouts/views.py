from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from workouts.forms import StartWorkoutSessionForm, CreateWorkoutTypeForm
from workouts.models import WorkoutSession, WorkoutType


class StartWorkoutSessionView(LoginRequiredMixin, CreateView):
    model = WorkoutSession
    template_name = "workouts/wt-start-p.html"
    form_class = StartWorkoutSessionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workout_types"] = WorkoutType.objects.all()
        return context


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
