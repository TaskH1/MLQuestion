from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import Chapter, Question, Answer
from .forms import ChapterForm, QuestionForm, AnswerForm

# Create your views here.

def index(request):
    """Home page"""
    return render(request, 'ml_question/index.html')

def chapters(request):
    """Show all chapters"""
    chapters = Chapter.objects.order_by('number')
    context = {'chapters': chapters}
    return render(request, 'ml_question/chapters.html', context)

def chapter(request, chapter_id):
    """Show a single chapter and its questions"""
    chapter = Chapter.objects.get(id=chapter_id)
    questions = chapter.questions.order_by('created_at')
    context = {'chapter': chapter, 'questions': questions}
    return render(request, 'ml_question/chapter.html', context)

def question(request, chapter_id, question_id):
    """Show a single question"""
    chapter = Chapter.objects.get(id=chapter_id)
    question = Question.objects.get(id=question_id)
    answer = Answer.objects.get(question_id=question_id)
    context = {'chapter': chapter, 'question': question, 'answer': answer}
    return render(request, 'ml_question/question.html', context)

@csrf_exempt
def new_chapter(request):
    """Create a new chapter"""
    if request.method != 'POST':
        form = ChapterForm()
    else:
        form = ChapterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('ml_question:chapters')
            
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'ml_question/new_chapter.html', context)

@csrf_exempt
def new_question(request, chapter_id):
    """Create a new question and its answer"""
    chapter = Chapter.objects.get(id=chapter_id)
    if request.method != 'POST':
        question_form = QuestionForm()
        answer_form = AnswerForm()
    else:
        question_form = QuestionForm(data=request.POST)
        answer_form = AnswerForm(data=request.POST)
        if question_form.is_valid() and answer_form.is_valid():
            question = question_form.save(commit=False)
            question.chapter = chapter
            question.save()

            answer = answer_form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('ml_question:chapter', chapter_id=chapter_id)
    
    context = {'question_form': question_form,
                'answer_form': answer_form,
                'chapter_id': chapter_id}
    return render(request, 'ml_question/new_question.html', context)
        