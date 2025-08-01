from django import forms

from forum.models import Question, Answer


class QuestionBaseForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ('user', 'approved',)


class QuestionCreateForm(QuestionBaseForm):
    pass


class AnswerCreateForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your answer here...'}),
        }