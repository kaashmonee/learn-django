from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

# Some important notes:
    # the choice_text and the things are machine readable, but if there
    # is no human readable parameter provided (like is for pub_date), then
    # the machine readable suffices for the human readable stuff

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __repr__(self):
        return self.question_text

    # basically determines if the question was published recently
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # I guess this is how we associate choice with question
    # When we do this, the Django creates a choice_set for each instance of 
    # Question so that the all the choices can be associated with it
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # creates a backend charfield of possible length 200
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __repr__(self):
        return self.choice_text
