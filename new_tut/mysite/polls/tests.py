from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse
from .models import Question
# Create your tests here.

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        # was_published_recently() returns False for questions whose pub_date
        # is in the future
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        # ensure that method is working as expected previously
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)
    
    def test_was_published_recently_with_recent_question(self):
        # makes sure that the recent stuff remains recent
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59,seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    
def create_question(question_text, days):
    # creates a question with # day offset
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    
    def test_no_questions(self):
        # if no questions exist, then the appropriate message is displayed
        # Reverse gets the URL from just the name! Holy fuck Django does so many
        # fucking things out of the box
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        # questions with a pub date in the past are dipslayed on the index page

        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            ["<Question: Past question.>"]
        )

    def test_future_question(self):
        # questions wiht a pub date in the future aren't displalyed on the page
        # making sure that the above statement is true
        # Positive number means future!
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        # Makes sure that the response contains this line
        self.assertContains(response, "No polls are available.")
        # Makes sure that the latest_question_list is empty because there is 
        # no question
        self.assertQuerysetEqual(response.context["lastest_question_list"], [])

    def test_future_question_and_past_question(self):
        # creating questions to test on
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            ["<Question: Past question.>"]
        )

    def test_two_past_questions(self):
        # questions index may have multiple questions
        create_question(question_text="Past question 1.", days=-30)
        create_question(quesiton_text="Past question 2.", days=-5)

        response = self.client.get(reverse("polls:index"))

        self.assertQuerysetEqual(
            response.context["lastest_question_list"],
            ["<Question: Past question 2.>", "<Question: Past question 1.>"]
        )