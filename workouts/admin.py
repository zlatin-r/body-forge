from django.contrib import admin
from .models import Workout


@admin.register(Workout)
class WorkoutTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "date_started", "muscle_group")
#
#
# @admin.register(Exercise)
# class ExerciseAdmin(admin.ModelAdmin):
#     list_display = ("name", "description", "workout_type",)
#
#
# @admin.register(MuscleGroup)
# class MuscleGroupAdmin(admin.ModelAdmin):
#     list_display = ("name",)
#
#
# @admin.register(WorkoutSession)
# class WorkoutSessionAdmin(admin.ModelAdmin):
#     list_display = ("user", "workout_type", "date_started",)
#
#
# @admin.register(ExerciseSet)
# class ExerciseSetAdmin(admin.ModelAdmin):
#     list_display = ("workout_session", "exercise", "muscle_group", "series_number", "repetitions", "weight_kg",)
