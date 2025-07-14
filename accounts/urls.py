from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include

from accounts import views

urlpatterns = [
    path('register/', views.AppUserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/profile-login.html'), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('<int:pk>/', include([
        path('dasboard/', views.DashboardView.as_view(), name='dashboard'),
        path('details/', views.ProfileDetailsView.as_view(), name='profile-details'),
        path('edit/', views.ProfileEditView.as_view(), name='profile-edit'),
        path('delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
    ])),
]
