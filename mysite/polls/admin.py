from django.contrib import admin
from .models import Choice, Question
from .models import Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)


# Register your models here.
