from django.urls import path, include
from workouts.views import StartWorkout, CreateMuscleGroup, DeleteMuscleGroup

urlpatterns = [
    path('start-wt/', StartWorkout.as_view(), name='start-workout'),
    path('add-mg/', CreateMuscleGroup.as_view(), name='add-muscle-group'),
    path("delete-mg/<int:pk>/", DeleteMuscleGroup.as_view(), name="delete-muscle-group"),
]
