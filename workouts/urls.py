from django.urls import path, include
from workouts.views import StartWorkout

urlpatterns = [
    path('start-wt/', StartWorkout.as_view(), name='start-workout'),
    # path('add-workout-type/', CreateWorkoutTypeView.as_view(), name='add-workout-type'),
    # path('workout-type/<int:pk>/', include([
        # path('delete/', DeleteWorkoutTypeView.as_view(), name='delete-workout-type'),
    # ])),
]
