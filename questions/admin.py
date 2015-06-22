from django.contrib import admin
from .models import *

# Register your models here.
# https://docs.djangoproject.com/en/dev/ref/contrib/admin/#working-with-many-to-many-intermediary-models

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

class PageQuestionnaireInline(admin.TabularInline):
    model = PageQuestionnaire
    extra = 0

class PageQuestionInline(admin.TabularInline):
    model = PageQuestion
    extra = 0

class PageAdmin(admin.ModelAdmin):
    inlines = (PageQuestionInline, )

class QuestionnaireAdmin(admin.ModelAdmin):
    inlines = (PageQuestionnaireInline, )

admin.site.register(Question, QuestionAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Questionnaire, QuestionnaireAdmin)

