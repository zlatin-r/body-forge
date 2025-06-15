from django.urls import path

from workouts import views

urlpatterns = [
    path('start/', views.StartWorkoutView.as_view(), name='start-workout'),
    path('add-sets/<int:workout_id>/', views.AddWorkoutSetsView.as_view(), name='add-workout-sets'),
    path('summary/<int:workout_id>/', views.WorkoutSummaryView.as_view(), name='workout-summary'),
]
