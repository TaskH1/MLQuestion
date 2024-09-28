"""Define the url pattern for ml_question app"""
# needed when mapping URLs to views
from django.urls import path

from . import views
# distiguish this file from files of the same name in other apps within the project
app_name = "ml_question"

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Chapter page where all chapters is showed
    path('chapters/', views.chapters, name='chapters' ),
    # Individual chapter page
    path('chapters/<int:chapter_id>', views.chapter, name='chapter'),
    # Individual quesition page
    path('chapters/<int:chapter_id>/<int:question_id>', views.question, name='question'),
]