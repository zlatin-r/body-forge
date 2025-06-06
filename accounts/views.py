from typing import Any

from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, TemplateView, DeleteView

from accounts.forms import AppUserCreationForm, ProfileEditForm
from accounts.models import Profile

UserModel = get_user_model()


class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = "accounts/register-page.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

    def get_success_url(self):
        profile = self.object.profile
        return reverse_lazy("profile-edit", kwargs={"pk": profile.pk})


class AppUserLoginView(LoginView):
    template_name = "accounts/login-page.html"

    def get_success_url(self):
        return reverse_lazy("dashboard", kwargs={"pk": self.request.user.pk})


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/dashboard.html"


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = "accounts/profile-details-page.html"


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = "accounts/profile-edit-page.html"

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.user

    def get_success_url(self):
        return reverse_lazy("profile-details", kwargs={"pk": self.object.pk})


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    template_name = "accounts/profile-delete-page.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.user

    def post(self, request, *args, **kwargs):
        profile = self.get_object()
        user = profile.user
        logout(request)
        user.delete()
        return redirect(self.success_url)
