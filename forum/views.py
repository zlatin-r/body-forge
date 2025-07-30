from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from forum.forms import QuestionCreateForm, AnswerForm
from forum.models import Question


class ListQuestionsView(ListView, PermissionRequiredMixin):
    model = Question
    template_name = 'forum/qu-list.html'
    permission_required = 'forum.approve_question'

    def get_queryset(self):
        queryset = self.model.objects.all()
        if not self.has_permission():
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
    form_class = AnswerForm

    def get_success_url(self):
        return reverse_lazy('qu-details', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = self.object
            answer.user = self.request.user
            answer.save()
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['answers'] = self.object.answers.all()
        return context
