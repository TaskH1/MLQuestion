"""Define the url pattern for ml_question app"""
from django.urls import path

from . import views

app_name = "ml_question"
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]