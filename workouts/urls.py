from django.urls import path, include

from workouts.views import CreateWorkoutView, CreateWorkoutTypeView

urlpatterns = [
    path('', CreateWorkoutView.as_view(), name='start-wt'),
    path('wt-type/create/', CreateWorkoutTypeView.as_view(), name='create-wt-type'),
]
