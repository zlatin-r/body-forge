from django.contrib import admin
from django.contrib.auth import get_user_model
from accounts.forms import AppUserCreationForm
from accounts.models import Profile

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    form = AppUserCreationForm


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ...