from django.contrib import admin
from .models import Workout, WorkoutType, Exercise, MuscleGroup, ExerciseSet


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "workout_type", "created")
    list_filter = ("workout_type", "created")
    search_fields = ("user__email", "workout_type__name")
    ordering = ("-created",)


@admin.register(WorkoutType)
class WorkoutTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "user")
    search_fields = ("name", "user__email")


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "muscle_group", "workout")
    list_filter = ("muscle_group",)
    search_fields = ("name", "user__email", "muscle_group__name", "workout__id")
    ordering = ("-created",)


@admin.register(MuscleGroup)
class MuscleGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "user")
    search_fields = ("name", "user__email")


@admin.register(ExerciseSet)
class ExerciseSetAdmin(admin.ModelAdmin):
    list_display = ("id", "exercise", "repetitions", "weight")
    search_fields = ("exercise__name",)
