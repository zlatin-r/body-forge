from django.urls import path, include

from forum.views import CreateQuestion, ListQuestionsView

urlpatterns = [
    path('forum/', include([
        path('', ListQuestionsView.as_view(), name='qu-list'),
        path('add-question/', CreateQuestion.as_view(), name='qu-create'),
    ])),
]
