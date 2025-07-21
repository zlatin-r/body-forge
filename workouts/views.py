from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView

from workouts.forms import CreateWorkoutForm, CreateWorkoutTypeForm
from workouts.models import Workout, WorkoutType


class CreateWorkoutView(LoginRequiredMixin, CreateView):
    model = Workout
    form_class = CreateWorkoutForm
    template_name = 'workouts/wt-start.html'

    def get_success_url(self):
        return reverse_lazy('dashboard', kwargs={'pk': self.request.user.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wt_types'] = WorkoutType.objects.filter(user=self.request.user)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CreateWorkoutTypeView(LoginRequiredMixin, CreateView):
    model = WorkoutType
    form_class = CreateWorkoutTypeForm
    template_name = 'workouts/wt-type-create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('wt-start')  # Adjust to your start view URL name


class DeleteWorkoutTypeView(LoginRequiredMixin, DeleteView):
    model = WorkoutType

    def post(self, request, *args, **kwargs):
        workout_type = self.get_object()

        if workout_type.user == request.user:
            workout_type.delete()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False}, status=403)
