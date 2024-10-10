"""Define the url pattern for ml_question app"""
# needed when mapping URLs to views
from django.urls import path

from . import views
# distiguish this file from files of the same name in other apps within the project
# this is a namespace
app_name = "ml_question"

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Chapter
    # Page where all chapters is showed
    path('chapters/', views.chapters, name='chapters' ),
    # Individual chapter page
    path('chapters/<int:chapter_id>', views.chapter, name='chapter'),
    # Page for adding a new chapter
    path('new_chapter/', views.new_chapter, name='new_chapter'),
    # Page for editing chapter
    path('edit_chapter/<int:chapter_id>', views.edit_chapter, name='edit_chapter'),
    # Delete a chapter
    path('delete_chapter/<int:chapter_id>', views.delete_chapter, name='delete_chapter'),
    
    # Question
    # Individual quesition page
    path('chapters/<int:chapter_id>/<int:question_id>/', views.question, name='question'),
    # Page for adding a new question and an answer
    path('chapters/<int:chapter_id>/new_question/', views.new_question, name='new_question'),
    # Page for editing a question and an answer
    path('edit_question/<int:question_id>/', views.edit_question, name='edit_question'),
    # Deleter a quesiton and an answer
    path('delete_question/<int:question_id>/', views.delete_question, name='delete_question'),

    # Submit Answer
    path('chapters/<int:chapter_id>/<int:question_id>/submit', views.submit_answer, name='submit_answer'),
    # Page for Feedback
    path('feedback/<int:user_answer_id>/', views.show_feedback, name='feedback')
]