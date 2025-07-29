from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from forum.forms import QuestionCreateForm
from forum.models import Question


class ListQuestionsView(ListView, PermissionRequiredMixin):
    model = Question
    template_name = 'forum/qu-list.html'
    permission_required = 'forum.approve_question'

    def get_queryset(self):
        if self.request.user.has_perm('forum.approve_question'):
            return Question.objects.all()
        return Question.objects.filter(approved=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_questions'] = Question.objects.all()
        return context


class CreateQuestion(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionCreateForm
    template_name = 'forum/qu-create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dashboard', kwargs={'pk': self.request.user.pk})
