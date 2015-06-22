from django.forms.models import modelformset_factory
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import *
# Create your views here.
from questions.forms import PageForm, QuestionForm


def list_questionnaires(request):
    questionnaires = Questionnaire.objects.all()

    return render(request, "landing_page.html",
                  {"questionnaires": questionnaires})


def questionnaire(request, pk):
    questionnaire = get_object_or_404(Questionnaire, pk=pk)

    return render(request, "questionnaire.html",
                  {"questionnaire": questionnaire})


def the_form(request):
    PageFormSet = modelformset_factory(Question, exclude=[],
                                       extra=0,
                                     formset=PageForm)
    QuestionFormSet = modelformset_factory(Answer, exclude=[],
                                      formset=QuestionForm)

    page_form = PageFormSet(page_id = 1)

    # import ipdb;ipdb.set_trace()

    return render(request, "name.html", {"page_form": page_form,
                                         "question_class":QuestionFormSet})