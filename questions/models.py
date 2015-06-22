# Create your models here.
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=120)

    def __unicode__(self):
        return "Question: {}".format(self.question_text)

class Answer(models.Model):
    answer_text = models.CharField(max_length=120)
    question = models.ForeignKey(Question)
    is_correct = models.BooleanField()
    score = models.IntegerField()

    def __unicode__(self):
        return "Answer: {}".format(self.answer_text)

class Page(models.Model):
    questions = models.ManyToManyField(Question, through = "PageQuestion")
    name = models.CharField(max_length=128, default="Unnamed page")

    def __unicode__(self):
        return "Page: {} ".format(self.name)

class Questionnaire(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    pages = models.ManyToManyField(Page, through="PageQuestionnaire")

    def __unicode__(self):
        return "Questionnaire: {}".format(self.name)

class PageQuestionnaire(models.Model):
    page = models.ForeignKey(Page)
    questionnaire = models.ForeignKey(Questionnaire)
    order = models.IntegerField()

class PageQuestion(models.Model):
    page = models.ForeignKey(Page)
    question = models.ForeignKey(Question)
    order = models.IntegerField()
