from django import forms

from .models import Chapter, Question, Answer

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['number', 'title', 'description']
        labels = {'number': 'Chapter Number',
                  'title': 'Chapter Title',
                  'description': 'Chapter description'}


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        labels = {'question_text': 'Question'}

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text']
        labels = {'answer_text': 'Answer'}
        