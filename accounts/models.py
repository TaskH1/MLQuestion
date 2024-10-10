from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from ml_question.models import Question, Answer

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    submitted_answer = models.TextField(null=False)
    is_correct = models.BooleanField(default=False)
    feedback = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Answer by {self.user.username} for {self.question.question_text}"

