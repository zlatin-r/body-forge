from django.urls import path, include

from workouts.views import (
    CreateWorkoutView, CreateWorkoutTypeView, DeleteWorkoutTypeView,
)

urlpatterns = [
    path('', CreateWorkoutView.as_view(), name='wt-create'),
    path('add-type/',CreateWorkoutTypeView.as_view(), name='wt-type-create'),
    path('delete-type/<int:pk>/',DeleteWorkoutTypeView.as_view(), name='wt-type-delete'),
]
