from django.urls import path, include

from workouts.views import StartWorkoutView

urlpatterns = [
    path('start-wt/', StartWorkoutView.as_view(), name="start-wt"),
]
