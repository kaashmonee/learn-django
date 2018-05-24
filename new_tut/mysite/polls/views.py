from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader

# Create your views here.

# What is the second parameter for each of these?

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # We don't have to look in the templates directory because django does 
    # that automatically
    template = loader.get_template("polls/index.html")
    print(template, type(template))

    # The context is sipmly what w
    context = {
        "latest_question_list": latest_question_list,
    }

    # this creates an http response, and renders the context in which we are
    # responding with and the request itself

    # THIS IS EQUIVALENT TO:
    # The first parameter is the request coming in, the template to render, and 
    # the list of questions
    return render(request, "polls/index.html", context)
    # return HttpResponse(template.render(context, request))

def fuckme(request):
    return HttpResponse("Fuckmeular regioular Mrs. Nature!")

def testularregion(request):
    return HttpResponse("Testularregion!\n")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def detail(request, question_id):
    # Instead of the code below, we can substitue that with yet another Django
    # shortcut:
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except:
    #     raise Http404("Question does not exist")

    # DJANGO SHORTCUT
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

    # Parameters are (request, polls/detail.html, and question)
    return render(request, "polls/detail.html", {"question": question})