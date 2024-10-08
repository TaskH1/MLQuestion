from django.db import models
from django.utils import timezone

# Create your models here.

class Chapter(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.number}. {self.title}"

class Question(models.Model):
    chapter = models.ForeignKey(Chapter, null=False, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        """Return a string representation of the model."""
        return self.question_text

class Answer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='answer')
    answer_text = models.TextField(max_length=1000)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.answer_text[:50]}..."
