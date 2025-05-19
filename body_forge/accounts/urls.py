from django.contrib.auth.views import LogoutView
from django.urls import path, include

from body_forge.accounts import views

urlpatterns = [
    path('register/', views.AppUserRegisterView.as_view(), name='register-user'),
    path('login/', views.AppUserLoginView.as_view(), name='login-user'),
    path('logout/', LogoutView.as_view(), name="logout-user"),
    path('<int:pk>/', include([
        path('edit/', views.profile_edit_view.as_view(), name='edit-profile-page'),
    ])),
    path('details/<int:pk>/', views.ProfileDetailsView.as_view(), name='profile-details'),
    path('dashboard/', views.UserDashboardView.as_view(), name='dashboard'),
]
