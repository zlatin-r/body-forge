from django.urls import path
from workouts.views import *

urlpatterns = [
    path('start/', StartWorkoutView.as_view(), name='start-workout'),
    # path('add-sets/<int:workout_id>/', AddWorkoutSetsView.as_view(), name='add-workout-sets'),
    # path('summary/<int:workout_id>/', WorkoutSummaryView.as_view(), name='workout-summary'),
]
