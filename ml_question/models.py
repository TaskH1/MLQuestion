from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Define the table name
    class Meta:
        db_table = 'questions'
        
    def __str__(self):
        """Return a string representation of the model."""
        return self.question_text

    
