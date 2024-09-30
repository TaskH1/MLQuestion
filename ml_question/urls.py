"""Define the url pattern for ml_question app"""
# needed when mapping URLs to views
from django.urls import path

from . import views
# distiguish this file from files of the same name in other apps within the project
app_name = "ml_question"

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Chapter
    # Chapter page where all chapters is showed
    path('chapters/', views.chapters, name='chapters' ),
    # Individual chapter page
    path('chapters/<int:chapter_id>', views.chapter, name='chapter'),
    # Page for adding a new chapter
    path('new_chapter/', views.new_chapter, name='new_chapter'),
    # Question
    # Individual quesition page
    path('chapters/<int:chapter_id>/<int:question_id>', views.question, name='question'),
    # Page for adding a new question
    path('chapters/<int:chapter_id>/new_question', views.new_question, name='new_question'),
]