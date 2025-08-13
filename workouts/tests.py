from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from workouts.models import MuscleGroup, WorkoutType, Workout, Exercise, ExerciseSet

UserModel = get_user_model()


class WorkoutTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email='testuser@example.com',
            password='password123'
        )
        self.client.login(email='testuser@example.com', password='password123')

        self.muscle_group = MuscleGroup.objects.create(user=self.user, name='Chest')
        self.workout_type = WorkoutType.objects.create(user=self.user, name='Push Day')
        self.workout = Workout.objects.create(user=self.user, workout_type=self.workout_type)
        self.exercise = Exercise.objects.create(
            user=self.user,
            name='Bench Press',
            muscle_group=self.muscle_group,
            workout=self.workout
        )

    def test_muscle_group_model(self):
        self.assertEqual(str(self.muscle_group), 'Chest')

    def test_workout_type_model(self):
        self.assertEqual(str(self.workout_type), 'Push Day')

    def test_exercise_model(self):
        self.assertEqual(str(self.exercise), 'Bench Press (Chest)')

    def test_workout_model(self):
        self.assertIn('Workout on', str(self.workout))

    def test_exercise_set_model(self):
        exercise_set = ExerciseSet.objects.create(exercise=self.exercise, repetitions=10, weight=100)
        self.assertEqual(str(exercise_set), '10 reps @ 100.00 kg')

    def test_create_workout_view(self):
        response = self.client.post(reverse('wt-create'), {'workout_type': self.workout_type.pk})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Workout.objects.filter(user=self.user, workout_type=self.workout_type).exists())

    def test_details_workout_view(self):
        response = self.client.get(reverse('wt-details', kwargs={'workout_pk': self.workout.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Push Day')

    def test_create_workout_type_view(self):
        response = self.client.post(reverse('wt-type-create'), {'name': 'Pull Day'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(WorkoutType.objects.filter(user=self.user, name='Pull Day').exists())

    def test_delete_workout_type_view(self):
        workout_type_to_delete = WorkoutType.objects.create(user=self.user, name='Leg Day')
        response = self.client.post(reverse('wt-type-delete', kwargs={'pk': workout_type_to_delete.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(WorkoutType.objects.filter(pk=workout_type_to_delete.pk).exists())

    def test_create_exercise_view(self):
        response = self.client.post(
            reverse('ex-create', kwargs={'workout_pk': self.workout.pk}),
            {'name': 'Incline Bench Press', 'muscle_group': self.muscle_group.pk}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Exercise.objects.filter(name='Incline Bench Press').exists())

    def test_create_muscle_group_view(self):
        response = self.client.post(
            reverse('mg-create', kwargs={'workout_pk': self.workout.pk}),
            {'name': 'Shoulders'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(MuscleGroup.objects.filter(name='Shoulders').exists())

    def test_delete_muscle_group_view(self):
        muscle_group_to_delete = MuscleGroup.objects.create(user=self.user, name='Triceps')
        response = self.client.post(reverse('mg-delete', kwargs={'pk': muscle_group_to_delete.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(MuscleGroup.objects.filter(pk=muscle_group_to_delete.pk).exists())

    def test_delete_exercise_view(self):
        exercise_to_delete = Exercise.objects.create(
            user=self.user,
            name='Dumbbell Flyes',
            muscle_group=self.muscle_group,
            workout=self.workout
        )
        response = self.client.post(reverse('ex-delete', kwargs={'pk': exercise_to_delete.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Exercise.objects.filter(pk=exercise_to_delete.pk).exists())

    def test_create_set_view(self):
        response = self.client.post(
            reverse('set-create', kwargs={'workout_pk': self.workout.pk, 'exercise_pk': self.exercise.pk}),
            {'repetitions': 12, 'weight': 80}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(ExerciseSet.objects.filter(repetitions=12, weight=80).exists())


