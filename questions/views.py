from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import *
# Create your views here.
from questions.forms import PageResponseForm


def list_questionnaires(request):
    questionnaires = Questionnaire.objects.all()

    return render(request, "landing_page.html",
                  {"questionnaires": questionnaires})


def questionnaire(request, pk):
    questionnaire = get_object_or_404(Questionnaire, pk=pk)

    return render(request, "questionnaire.html",
                  {"questionnaire": questionnaire})


def page(request, page_id):
   page = Page.objects.get(pk = page_id)
   questions = page.questions.all()
   return render(request, "page.html", {"page": page,
                                        "questions":questions})

def next(request):
    answers = filter(lambda x : x.startswith("answer"),
                 request.POST.keys())
    selected_answer_ids = map(lambda x : int(x.split("_")[1]), answers)

    for selected_answer_id in selected_answer_ids:
        selected_answer = Answer.objects.get(pk = selected_answer_id)
        UserAnswer.objects.create(answer = selected_answer,
                                  questionnaire = None,
                                  session_id = request.session.session_key)


    return render(request, "page.html")