from django.urls import path

from accounts import views

urlpatterns = [
    path('register/',views.AppUserRegisterView.as_view(), name='register'),
]