from django.contrib.auth import get_user_model, login
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import AppUserCreationForm

UserModel = get_user_model()


class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = "accounts/register-page.html"
    success_url = reverse_lazy("home-page")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
