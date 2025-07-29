from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView, TemplateView, DeleteView, ListView

from accounts.forms import AppUserCreationForm, ProfileEditForm
from accounts.models import Profile
from forum.models import Question
from workouts.models import Workout

UserModel = get_user_model()


class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/profile-register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        # Signal for profile creation

        if response.status_code in [301, 302]:
            login(self.request, self.object)
        return response

    def get_success_url(self):
        profile = self.object.profile
        return reverse_lazy('profile-edit', kwargs={'pk': profile.pk})


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'accounts/profile-details.html'


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit.html'

    def test_func(self):
        return self.request.user.profile.pk == self.kwargs['pk']

    def get_success_url(self):
        return reverse("profile-details", kwargs={"pk": self.object.pk})


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.user

    def post(self, request, *args, **kwargs):
        profile = self.get_object()
        user = profile.user
        logout(request)
        user.delete()
        return redirect(self.success_url)


class DashboardView(LoginRequiredMixin, ListView):
    model = Workout
    template_name = 'accounts/dashboard.html'
    context_object_name = 'workouts'

    def get_queryset(self):
        return (Workout.objects.filter(user=self.request.user)
                .order_by('-created')
                .prefetch_related('exercises', 'exercises__sets'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_questions'] = Question.objects.filter(user=self.request.user)
        return context