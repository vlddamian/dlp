from django import forms
from django.forms import BaseModelFormSet

from questions.models import Page, Question, PageQuestion


__author__ = 'vlad.damian'

# http://yergler.net/blog/2013/09/03/nested-formsets-redux/
class PageForm(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        page_id = kwargs.pop("page_id")
        super(PageForm, self).__init__(*args, **kwargs)
        self.queryset = \
            Page.objects.get(pk = page_id).questions.all()



class QuestionForm(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        question_id = kwargs.pop("question_id")
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.queryset = \
            Question.objects.get(pk = question_id).answers.all()