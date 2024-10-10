from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .models import Chapter, Question, Answer
from .forms import ChapterForm, QuestionForm, AnswerForm, UserAnswerForm
from accounts.models import UserAnswer
from accounts.utils import evaluate_answer_with_llm

# Create your views here.

def index(request):
    """Home page"""
    return render(request, 'ml_question/index.html')

# Chapter
def chapters(request):
    """Show all chapters"""
    chapters = Chapter.objects.order_by('number')
    context = {'chapters': chapters}
    return render(request, 'ml_question/chapters.html', context)

def chapter(request, chapter_id):
    """Show a single chapter and its questions"""
    chapter = get_object_or_404(Chapter, id=chapter_id)
    questions = chapter.questions.order_by('created_at')
    context = {'chapter': chapter, 'questions': questions}
    return render(request, 'ml_question/chapter.html', context)

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

def edit_chapter(request, chapter_id):
    """Edit an existing chpater"""
    chapter = get_object_or_404(Chapter, id=chapter_id)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current chpater.
        form = ChapterForm(instance=chapter)
    else:
        # POST data submitted; process data.
        form = ChapterForm(instance=chapter, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('ml_question:chapter', chapter_id=chapter.id)
    
    context = {'chapter': chapter, 'form': form}
    return render(request, 'ml_question/edit_chapter.html', context)

#@csrf_exempt
def delete_chapter(request, chapter_id):
    """Delete an existing chapter"""
    chapter = get_object_or_404(Chapter, id=chapter_id)

    if request.method == 'POST':
        chapter.delete()
        return redirect('ml_question:chapters')
    
    context = {'chapter': chapter}
    return render(request, 'ml_question/delete_chapter.html', context)
        

# Question
def question(request, chapter_id, question_id):
    """Show a single question"""
    chapter = get_object_or_404(Chapter, id=chapter_id)
    question = get_object_or_404(Question, id=question_id)
    answer = get_object_or_404(Answer, question_id=question_id)
    user_answer_form = UserAnswerForm()
    context = {'chapter': chapter, 'question': question, 'answer': answer, 'user_answer_form': user_answer_form}
    return render(request, 'ml_question/question.html', context)

def new_question(request, chapter_id):
    """Create a new question and its answer"""
    chapter = get_object_or_404(Chapter, id=chapter_id)
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
                'chapter': chapter}
    return render(request, 'ml_question/new_question.html', context)

def edit_question(request, question_id):
    """Edit a exsiting question and an answer"""
    question = get_object_or_404(Question, id=question_id)
    answer = Answer.objects.get(question_id=question_id)

    if request.method != 'POST':
        question_form = QuestionForm(instance=question)
        answer_form = AnswerForm(instance=answer)
    else:
        question_form = QuestionForm(instance=question, data=request.POST)
        answer_form = AnswerForm(instance=answer, data=request.POST)
        if question_form.is_valid() and answer_form.is_valid():
            question_form.save()
            answer_form.save()
            return redirect('ml_question:question', chapter_id=question.chapter_id, question_id=question.id)
        else:
            print(question_form.errors)
    
    
    context = {'question_form': question_form,
               'answer_form': answer_form,
               'question_id': question_id}
    return render(request, 'ml_question/edit_question.html', context)

@csrf_exempt
def delete_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answer = get_object_or_404(Answer, question_id=question_id)

    if request.method == 'POST':
        question.delete()
        return redirect('ml_question:chapter', chapter_id=question.chapter_id)

    context = {'question': question,
                'answer': answer}
    return render(request, 'ml_question/delete_question.html', context)


def submit_answer(request, chapter_id, question_id):
    if request.method == 'POST':
        print("POST request received.")
        user_answer = request.POST.get('submitted_answer')

        # Get the related chapter and question
        chapter = get_object_or_404(Chapter, id=chapter_id)
        question = get_object_or_404(Question, id=question_id)

        # Evaluate the user's answer using the LLM
        correct_answer = question.answer
        is_correct, feedback = evaluate_answer_with_llm(user_answer, correct_answer.answer_text)

        # Save the user's answer to the database
        user_answer_obj = UserAnswer.objects.create(
            user=request.user,
            question=question,
            submitted_answer=user_answer,
            is_correct=is_correct,
            feedback=feedback
        )
        
        return redirect('ml_question:feedback', user_answer_id=user_answer_obj.id)
    return HttpResponse("Invalid request method.", status=405)

def show_feedback(request, user_answer_id):
    user_answer = get_object_or_404(UserAnswer, id=user_answer_id)
    question = user_answer.question
    correct_answer = question.answer

    context = {
        'user_answer': user_answer,
        'question': question,
        'correct_answer': correct_answer,
        'chapter': question.chapter
    }

    return render(request, 'ml_question/feedback.html', context)

