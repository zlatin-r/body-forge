from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from forum.forms import QuestionCreateForm, AnswerCreateForm
from forum.models import Question, Answer


class ListQuestionsView(LoginRequiredMixin, ListView):
    model = Question
    template_name = 'forum/qu-list.html'

    def get_queryset(self):
        queryset = self.model.objects.all()
        if not self.request.user.has_perm('forum.approve_question'):
            queryset = queryset.filter(approved=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_questions'] = self.get_queryset()
        return context


def approve_question(request, pk):
    if request.method == 'POST':
        question = Question.objects.get(pk=pk)
        question.approved = True
        question.save()

    return redirect('qu-list')


def delete_question(request, pk):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=pk)
        question.delete()

    return redirect('qu-list')


class CreateQuestion(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionCreateForm
    template_name = 'forum/qu-create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dashboard', kwargs={'pk': self.request.user.pk})


class DetailsQuestionView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = 'forum/qu-details.html'
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answers'] = self.object.answers.all()
        return context


class AnswerCreateView(LoginRequiredMixin, CreateView):
    model = Answer
    form_class = AnswerCreateForm
    template_name = 'forum/an-create.html'
    context_object_name = 'answer'

    def dispatch(self, request, *args, **kwargs):
        self.question = get_object_or_404(Question, pk=kwargs['question_pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question = self.question
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('qu-details', kwargs={'pk': self.question.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = self.question
        return context

