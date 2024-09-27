from django.db import models

# Create your models here.

class Chapter(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    chapter = models.ForeignKey(Chapter, null=True, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

        
    def __str__(self):
        """Return a string representation of the model."""
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(max_length=500)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.answer_text
