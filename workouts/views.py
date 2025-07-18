from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from workouts.forms import CreateWorkoutForm, CreateWorkoutTypeForm
from workouts.models import Workout, WorkoutType


class CreateWorkoutView(LoginRequiredMixin, CreateView):
    model = Workout
    form_class = CreateWorkoutForm
    template_name = 'workouts/wt-start.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wt_types'] = WorkoutType.objects.filter(workouts__user=self.request.user).distinct()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CreateWorkoutTypeView(LoginRequiredMixin, CreateView):
    model = WorkoutType
    form_class = CreateWorkoutTypeForm
    template_name = 'workouts/modals/wt-create-type-modal.html'
