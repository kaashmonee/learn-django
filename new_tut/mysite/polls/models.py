from django.db import models

# Create your models here.

# Some important notes:
    # the choice_text and the things are machine readable, but if there
    # is no human readable parameter provided (like is for pub_date), then
    # the machine readable suffices for the human readable stuff

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    # I guess this is how we associate choice with question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # creates a backend charfield of possible length 200
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
