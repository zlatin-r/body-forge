from django.urls import path
from workouts.views import StartWorkoutSessionView

urlpatterns = [
    path('start-workout/', StartWorkoutSessionView.as_view(), name='start-workout'),
]
