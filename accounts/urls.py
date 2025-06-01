from django.urls import path, include

from accounts import views

urlpatterns = [
    path('register/', views.AppUserRegisterView.as_view(), name='register'),
    path('login/', views.AppUserLoginView.as_view(), name="login"),
    path('<int:pk>/', include([
        path('edit/', views.ProfileEditView.as_view(), name='profile-edit'),
    ])),
]
