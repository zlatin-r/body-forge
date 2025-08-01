from django.contrib import admin

from forum.models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'approved', 'created')
    list_filter = ('approved', 'created')
    search_fields = ('title', 'content', 'user__email')
    ordering = ('-created',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'created')
    search_fields = ('content', 'user__email', 'question__title')
    ordering = ('-created',)
