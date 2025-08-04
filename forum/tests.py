from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from forum.models import Question, Answer

UserModel = get_user_model()


class ForumTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email='test@example.com',
            password='password123',
        )
        self.superuser = UserModel.objects.create_superuser(
            email='superuser@example.com',
            password='password123',
        )
        self.question = Question.objects.create(
            user=self.user,
            title='Test Question',
            content='Test Content',
            approved=True,
        )
        self.unapproved_question = Question.objects.create(
            user=self.user,
            title='Unapproved Question',
            content='Test Content',
        )

    def test_question_model(self):
        self.assertEqual(str(self.question.title), 'Test Question')
        self.assertEqual(self.question.user, self.user)

    def test_answer_model(self):
        answer = Answer.objects.create(
            question=self.question,
            user=self.user,
            content='Test Answer',
        )
        self.assertEqual(
            str(answer),
            f'Answer by {self.user.email} on "{self.question.title}"'
        )

    def test_list_questions_view_unauthenticated(self):
        response = self.client.get(reverse('qu-list'))
        self.assertEqual(response.status_code, 302)

    def test_list_questions_view_authenticated(self):
        self.client.login(email='test@example.com', password='password123')
        response = self.client.get(reverse('qu-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Question')
        self.assertNotContains(response, 'Unapproved Question')

    def test_list_questions_view_superuser(self):
        self.client.login(email='superuser@example.com', password='password123')
        response = self.client.get(reverse('qu-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Question')
        self.assertContains(response, 'Unapproved Question')

    def test_create_question_view_unauthenticated(self):
        response = self.client.get(reverse('qu-create'))
        self.assertEqual(response.status_code, 302)

    def test_create_question_view_authenticated(self):
        self.client.login(email='test@example.com', password='password123')
        response = self.client.post(
            reverse('qu-create'),
            {'title': 'New Question', 'content': 'New Content'},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Question.objects.filter(title='New Question').exists())

    def test_details_question_view_unauthenticated(self):
        response = self.client.get(
            reverse('qu-details', kwargs={'pk': self.question.pk})
        )
        self.assertEqual(response.status_code, 302)

    def test_details_question_view_authenticated(self):
        self.client.login(email='test@example.com', password='password123')
        response = self.client.get(
            reverse('qu-details', kwargs={'pk': self.question.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Question')

    def test_approve_question_view(self):
        self.client.login(email='superuser@example.com', password='password123')
        response = self.client.post(
            reverse('qu-approve', kwargs={'pk': self.unapproved_question.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.unapproved_question.refresh_from_db()
        self.assertTrue(self.unapproved_question.approved)

    def test_delete_question_view(self):
        self.client.login(email='superuser@example.com', password='password123')
        response = self.client.post(
            reverse('qu-delete', kwargs={'pk': self.question.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Question.objects.filter(pk=self.question.pk).exists())

    def test_create_answer_view(self):
        self.client.login(email='test@example.com', password='password123')
        response = self.client.post(
            reverse('an-create', kwargs={'question_pk': self.question.pk}),
            {'content': 'My new answer'},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Answer.objects.filter(content='My new answer').exists()
        )