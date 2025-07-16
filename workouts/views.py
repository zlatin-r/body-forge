from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from workouts.forms import WorkoutStartForm, MuscleGroupCreateForm
from workouts.models import Workout, MuscleGroup


class StartWorkout(LoginRequiredMixin, CreateView):
    model = Workout
    form_class = WorkoutStartForm
    template_name = "workouts/wt-start.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mg_create_form"] = MuscleGroupCreateForm()
        context["all_mg"] = MuscleGroup.objects.filter(user=self.request.user)
        return context


class CreateMuscleGroup(LoginRequiredMixin, CreateView):
    model = MuscleGroup
    form_class = MuscleGroupCreateForm
    template_name = "workouts/wt-start.html"
    success_url = reverse_lazy("start-workout")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
