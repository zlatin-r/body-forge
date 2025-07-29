from django import forms

from forum.models import Question


class QuestionBaseForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ('user', 'approved',)


class QuestionCreateForm(QuestionBaseForm):
    pass
