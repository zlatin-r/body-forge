from django.urls import path, include

from workouts.views import CreateWorkoutView

urlpatterns = [
    path('', CreateWorkoutView.as_view(), name='start-wt'),
]
