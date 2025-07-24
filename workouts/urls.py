from django.urls import path, include

from workouts.views import CreateWorkoutView, CreateWorkoutTypeView, DeleteWorkoutTypeView, CreateExerciseView, \
    CreateMuscleGroupView, CreateSetView, ExerciseDetailsView

urlpatterns = [
    path('', CreateWorkoutView.as_view(), name='wt-start'),
    path('type/create/', CreateWorkoutTypeView.as_view(), name='wt-type-create'),
    path('type/delete/<int:pk>/', DeleteWorkoutTypeView.as_view(), name='wt-type-delete'),
    path('exercise/', include([
        path('', CreateExerciseView.as_view(), name='ex-start'),
        path('mg-create/', CreateMuscleGroupView.as_view(), name='mg-create'),
        path('details/<int:pk>/', ExerciseDetailsView.as_view(), name='ex-details'),
    ])),
]
