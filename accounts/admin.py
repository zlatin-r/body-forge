from django.contrib import admin
from django.contrib.auth import get_user_model
from accounts.forms import AppUserCreationForm

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    form = AppUserCreationForm
