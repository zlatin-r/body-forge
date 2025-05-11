from django.urls import path

from body_forge.common.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]