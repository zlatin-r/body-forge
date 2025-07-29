from django.urls import path, include

from forum.views import CreateQuestion
from workouts.views import (
    CreateWorkoutView, CreateWorkoutTypeView, DeleteWorkoutTypeView, DetailsWorkoutView, CreateExerciseView,
    CreateMuscleGroupView, DeleteMuscleGroupView, DeleteExerciseView, CreateSetView,
)

urlpatterns = [
    path('', CreateWorkoutView.as_view(), name='wt-create'),
    path('add-type/', CreateWorkoutTypeView.as_view(), name='wt-type-create'),
    path('delete-type/<int:pk>/', DeleteWorkoutTypeView.as_view(), name='wt-type-delete'),
    path('delete-muscle-group/<int:pk>/', DeleteMuscleGroupView.as_view(), name='mg-delete'),
    path('delete-exercise/<int:pk>/', DeleteExerciseView.as_view(), name='ex-delete'),

    path('<int:workout_pk>/', include([
        path('details/', DetailsWorkoutView.as_view(), name='wt-details'),

        path('add-exercise/', CreateExerciseView.as_view(), name='ex-create'),
        path('add-muscle-group/', CreateMuscleGroupView.as_view(), name='mg-create'),
        path('exercise/<int:exercise_pk>/', include([
            path('add-set/', CreateSetView.as_view(), name='set-create'),
        ])),
    ])),
    path('forum/', include([
        path('add-question/', CreateQuestion.as_view(), name='qu-create'),
    ])),
]
