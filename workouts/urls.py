from django.urls import path, include

from workouts.views import (
    CreateWorkoutView, CreateWorkoutTypeView, DeleteWorkoutTypeView,
    CreateExerciseView, CreateMuscleGroupView, CreateSetView,
    ExerciseDetailsView, DeleteExerciseView, DeleteMuscleGroupView,
    DetailsWorkoutView
)

urlpatterns = [
    path('', CreateWorkoutView.as_view(), name='wt-create'),

    path('<int:pk>/', DetailsWorkoutView.as_view(), name='wt-details'),

    path('type/', include([
        path('create/', CreateWorkoutTypeView.as_view(), name='wt-type-create'),
        path('delete/<int:pk>/', DeleteWorkoutTypeView.as_view(), name='wt-type-delete'),
    ])),

    path('<int:workout_pk>/exercise/add/', CreateExerciseView.as_view(), name='ex-create'),

    path('exercise/<int:pk>/', include([
        path('add-set', CreateSetView.as_view(), name='set-create'),
        path('delete/', DeleteExerciseView.as_view(), name='ex-delete'),
        path('details/', ExerciseDetailsView.as_view(), name='ex-details'),
    ])),

    path('muscle_group/', include([
        path('add/', CreateMuscleGroupView.as_view(), name='mg-create'),
        path('delete/<int:pk>/', DeleteMuscleGroupView.as_view(), name='mg-delete'),
    ])),
]
