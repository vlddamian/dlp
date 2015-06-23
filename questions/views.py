from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import *
# Create your views here.

def list_questionnaires(request):
    questionnaires = Questionnaire.objects.all()

    return render(request, "landing_page.html",
                  {"questionnaires": questionnaires})


def questionnaire(request, pk):
    # should render the pages here
    questionnaire = get_object_or_404(Questionnaire, pk = pk)
    ordered_pages = [p.page for p in
                     PageQuestionnaire.objects.filter(questionnaire = questionnaire).
                     order_by("order")]

    return redirect("page/{}".format(ordered_pages[0].pk))

def page(request, questionnaire_id, page_id):
   questionnaire = get_object_or_404(Questionnaire, pk = questionnaire_id)
   page = get_object_or_404(questionnaire.pages, pk = page_id)

   ordered_questions = [q.question for q in
                        PageQuestion.objects.filter(page = page_id).
                            order_by("order")]

   return render(request, "page.html", {"page": page,
                                        "questions":ordered_questions,
                                        "questionnaire": questionnaire})


def next_page_in_questionnaire(questionnaire_id, current_page_id):
    questionnaire = get_object_or_404(Questionnaire, pk = questionnaire_id)
    ordered_pages = [p.page for p in PageQuestionnaire.objects.filter(
        questionnaire = questionnaire).order_by("order")]
    index = 0
    current_page_id = int(current_page_id)

    for page in ordered_pages:
        if page.pk == current_page_id:
            break
        index += 1
    if index == len(ordered_pages) - 1:
        next_pk = None
    else:
        next_pk = ordered_pages[index + 1].pk

    return next_pk

def next(request, questionnaire_pk, page_pk):
    answers = filter(lambda x : x.startswith("answer"),
                 request.POST.keys())
    selected_answer_ids = map(lambda x : int(x.split("_")[1]), answers)

    for selected_answer_id in selected_answer_ids:
        selected_answer = Answer.objects.get(pk = selected_answer_id)
        UserAnswer.objects.create(answer = selected_answer,
                                  questionnaire = None,
                                  session_id = request.session.session_key)

    next_page_pk = next_page_in_questionnaire(questionnaire_id = questionnaire_pk,
                               current_page_id=page_pk)
    if next_page_pk == None:
        return render(request, "score.html")

    return redirect("/questionnaires/{}/page/{}".format(questionnaire_pk,
                                                       next_page_pk))