from django.contrib import admin

# Register your models here.
from .models import Question, Answer, Chapter

# Inline for Answers
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

# Inline for Questions
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    inlines = [AnswerInline]

# equivalent to admin.site.register(Chapter, ChapterAdmin)
@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
