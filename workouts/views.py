from django.urls import reverse_lazy
from django.views.generic import CreateView

from workouts.forms import StartWorkoutForm
from workouts.models import Workout, WorkoutType


class StartWorkoutView(CreateView):
    model = Workout
    form_class = StartWorkoutForm
    template_name = 'workouts/wt-start.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wt_types'] = WorkoutType.objects.filter(workouts__user=self.request.user)

        return context

