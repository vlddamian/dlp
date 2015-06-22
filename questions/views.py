from django.shortcuts import render

from .models import *
# Create your views here.


def list_questionnaires(request):
    questionnaires = Questionnaire.objects.all()

    return render(request, "landing_page.html",
                  {"questionnaires": questionnaires})