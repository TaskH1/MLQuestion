from django.shortcuts import render
from .models import Chapter, Question, Answer

# Create your views here.
def index(request):
    # Home page
    return render(request, 'ml_question/index.html')

def chapters(request):
    # Show all chapters
    chapters = Chapter.objects.order_by('number')
    context = {'chapters': chapters}
    return render(request, 'ml_question/chapters.html', context)

def chapter(request, chapter_id):
    # Show a single chapter
    chapter = Chapter.objects.get(id=chapter_id)
    questions = chapter.questions.order_by('created_at')
    context = {'chapter': chapter, 'questions': questions}
    return render(request, 'ml_question/chapter.html', context)

def question(request, chapter_id, question_id):
    # Show a single question
    chapter = Chapter.objects.get(id=chapter_id)
    question = Question.objects.get(id=question_id)
    answer = Answer.objects.get(question_id=question_id)
    context = {'chapter': chapter, 'question': question, 'answer': answer}
    return render(request, 'ml_question/question.html', context)