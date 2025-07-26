from django.urls import path, include

from workouts.views import CreateWorkoutView, CreateWorkoutTypeView, DeleteWorkoutTypeView, CreateExerciseView, \
    CreateMuscleGroupView, CreateSetView, ExerciseDetailsView, DeleteExerciseView, DeleteMuscleGroupView

urlpatterns = [
    path('', CreateWorkoutView.as_view(), name='wt-start'),
    path('type/create/', CreateWorkoutTypeView.as_view(), name='wt-type-create'),
    path('type/delete/<int:pk>/', DeleteWorkoutTypeView.as_view(), name='wt-type-delete'),
    path('exercise/', CreateExerciseView.as_view(), name='ex-start'),
    path('mg-create/', CreateMuscleGroupView.as_view(), name='mg-create'),
    path('muscle-group/delete/<int:pk>/', DeleteMuscleGroupView.as_view(), name='mg-delete'),

    path('exercise/<int:pk>/', include([
        path('details/', ExerciseDetailsView.as_view(), name='ex-details'),
        path('add-set', CreateSetView.as_view(), name='add-set'),
        path('delete/', DeleteExerciseView.as_view(), name='ex-delete'),
    ])),
]
