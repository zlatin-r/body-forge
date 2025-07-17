from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from workouts.forms import WorkoutStartForm, MuscleGroupCreateForm, WorkoutTypeCreateForm
from workouts.models import Workout, MuscleGroup, WorkoutType


class StartWorkout(LoginRequiredMixin, CreateView):
    model = Workout
    form_class = WorkoutStartForm
    template_name = "workouts/wt-start.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mg_create_form"] = MuscleGroupCreateForm()
        context["wt_type_create_form"] = WorkoutTypeCreateForm()
        context["all_mg"] = MuscleGroup.objects.filter(user=self.request.user)
        context["all_wt_types"] = WorkoutType.objects.all()
        return context


class CreateMuscleGroup(LoginRequiredMixin, CreateView):
    model = MuscleGroup
    form_class = MuscleGroupCreateForm
    template_name = "workouts/wt-start.html"
    success_url = reverse_lazy("start-workout")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteMuscleGroup(LoginRequiredMixin, DeleteView):
    model = MuscleGroup
    success_url = reverse_lazy("start-workout")
    template_name = "workouts/wt-start.html"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class CreateWorkoutType(LoginRequiredMixin, CreateView):
    model = WorkoutType
    form_class = WorkoutTypeCreateForm
    template_name = "workouts/wt-start.html"
    success_url = reverse_lazy("start-workout")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)