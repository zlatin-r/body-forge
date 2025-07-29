from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.models import TimeStampedModel

UserModel = get_user_model()


class Question(TimeStampedModel):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='asked_questions',
        verbose_name='Asked By',
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Question Title'
    )
    content = models.TextField(
        verbose_name='Question Details'
    )
    approved = models.BooleanField(
        default=False,
    )

    class Meta:
        permissions = [
            ('approve_question', 'Can approve question'),
        ]