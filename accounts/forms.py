from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Profile

UserModel = get_user_model()


class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("email",)


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model =Profile
        fields = "__all__"


class ProfileEditForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ("user", "date_joined", "date_of_birth")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['profile_picture'].widget = forms.FileInput(attrs={
            'accept': 'image/*'
        })
