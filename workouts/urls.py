from django.urls import path, include

from workouts.views import CreateWorkoutView, CreateWorkoutTypeView, DeleteWorkoutTypeView

urlpatterns = [
    path('', CreateWorkoutView.as_view(), name='wt-start'),
    path('type/create/', CreateWorkoutTypeView.as_view(), name='wt-type-create'),
    path('type/delete/<int:pk>/', DeleteWorkoutTypeView.as_view(), name='wt-type-delete'),
]
