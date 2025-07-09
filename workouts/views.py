from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from workouts.forms import StartWorkoutSessionForm
from workouts.models import WorkoutSession, WorkoutType


class StartWorkoutSessionView(LoginRequiredMixin, CreateView):
    model = WorkoutSession
    template_name = "workouts/workout-start-page.html"
    form_class = StartWorkoutSessionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workout_types"] = WorkoutType.objects.all()
        return context


class CreateWorkoutTypeView(LoginRequiredMixin, CreateView):
    model = WorkoutType
    

# @login_required
# def start_workout_view(request):
#     if request.method == 'POST':
#         form = StartWorkoutForm(request.POST)
#         if form.is_valid():
#             workout_session = form.save(commit=False)
#             workout_session.user = request.user
#             workout_session.save()
#             return redirect('add-exercise', session_id=workout_session.id)
#     else:
#         form = StartWorkoutForm()
#
#     return render(request, 'workouts/workout-start-page.html', {'form': form})

#
# @login_required
# def create_exercise_view(request):
#     if request.method == 'POST':
#         form = ExerciseForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('create-exercise')  # Redirect to same page or workout flow
#     else:
#         form = ExerciseForm()
#
#     return render(request, 'workouts/exercise-create-page.html', {'form': form})
#
# @login_required
# def add_exercise_set_view(request, session_id):
#     session = get_object_or_404(WorkoutSession, pk=session_id, user=request.user)
#
#     if request.method == 'POST':
#         form = AddExerciseSetForm(request.POST)
#         if form.is_valid():
#             exercise_set = form.save(commit=False)
#             exercise_set.workout_session = session
#             exercise_set.save()
#             return redirect('add-exercise-set', session_id=session_id)
#     else:
#         form = AddExerciseSetForm()
#
#     return render(request, 'workouts/add-exercise-set.html', {
#         'form': form,
#         'session': session
#     })
