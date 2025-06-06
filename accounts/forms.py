from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Profile

UserModel = get_user_model()


class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("email", "password1", "password2")

        widgets = {
            'email': forms.TextInput(attrs={"class": "form-control"}),
            'password1': forms.PasswordInput(attrs={"class": "form-control"}),
            'password2': forms.PasswordInput(attrs={"class": "form-control"}),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ("user", "date_joined", "date_of_birth")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['profile_picture'].widget = forms.FileInput(attrs={
            'accept': 'image/*'
        })
