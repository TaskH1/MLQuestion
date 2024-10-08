from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from ml_question.models import Question, Answer

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    submitted_answer = models.TextField()
    correct = models.BooleanField(default=False)

    