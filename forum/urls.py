from django.urls import path, include

from forum.views import CreateQuestion, ListQuestionsView, approve_question, DetailsQuestionView, delete_question, \
    AnswerCreateView

urlpatterns = [
    path('', include([
        path('', ListQuestionsView.as_view(), name='qu-list'),
        path('add-question/', CreateQuestion.as_view(), name='qu-create'),
        path('question/<int:question_pk>/add-answer/', AnswerCreateView.as_view(), name='an-create'),
        path('details-qu/<int:pk>/', DetailsQuestionView.as_view(), name='qu-details'),
        path('approve-qu/<int:pk>/', approve_question, name='qu-approve'),
        path('delete-qu/<int:pk>/', delete_question, name='qu-delete'),
    ])),
]
