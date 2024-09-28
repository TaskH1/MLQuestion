from django.shortcuts import render
from .models import Chapter

# Create your views here.
def index(request):
    # Home page
    return render(request, 'ml_question/index.html')

def chapters(request):
    # Show all chapters
    chapters = Chapter.objects.order_by('number')
    context = {'chapters': chapters}
    return render(request, 'ml_question/chapters.html', context)

    