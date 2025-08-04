from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import Profile
from forum.models import Question
from workouts.models import Workout, WorkoutType

UserModel = get_user_model()


class IntegrationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email='testuser@example.com',
            password='password123'
        )
        self.client.login(email='testuser@example.com', password='password123')

    def test_user_creation_and_profile_signal(self):
        self.assertTrue(Profile.objects.filter(user=self.user).exists())

    def test_dashboard_displays_workouts_and_questions(self):
        workout_type = WorkoutType.objects.create(user=self.user, name='Test Workout')
        Workout.objects.create(user=self.user, workout_type=workout_type)
        Question.objects.create(user=self.user, title='Test Question', content='Test Content')

        response = self.client.get(reverse('dashboard', kwargs={'pk': self.user.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Workout')
        self.assertContains(response, 'Test Question')

    def test_user_deletion_cascades(self):
        workout_type = WorkoutType.objects.create(user=self.user, name='Test Workout')
        Workout.objects.create(user=self.user, workout_type=workout_type)
        Question.objects.create(user=self.user, title='Test Question', content='Test Content')

        user_pk = self.user.pk
        self.user.delete()

        self.assertFalse(UserModel.objects.filter(pk=user_pk).exists())
        self.assertFalse(Profile.objects.filter(user__pk=user_pk).exists())
        self.assertFalse(Workout.objects.filter(user__pk=user_pk).exists())
        self.assertFalse(Question.objects.filter(user__pk=user_pk).exists())

    def test_unauthenticated_user_access(self):
        self.client.logout()
        response = self.client.get(reverse('dashboard', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 302)  # Redirect to login

        response = self.client.get(reverse('qu-list'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

        response = self.client.get(reverse('wt-create'))
        self.assertEqual(response.status_code, 302)  # Redirect to login