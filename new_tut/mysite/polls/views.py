from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import Question
from django.utils import timezone
from django.template import loader

# Create your views here.

# What is the second parameter for each of these?

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     # We don't have to look in the templates directory because django does 
#     # that automatically
#     template = loader.get_template("polls/index.html")
#     print(template, type(template))

#     # The context is sipmly what wkend software, machine learning, ranking systems, and distributed systems. I'm interested in opportunities in SF/the Bay area, NYC, Boston, Seattle, Denver, and San Diego. I'm also the author of Remain Free, a
#     context = {
#         "latest_question_list": latest_question_list,
#     }

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        # Returns the last 5 published questions
        # return Question.objects.order_by("-pub_date")[:5]

        # Returns queryset containing questionswhose pub_date is less than or 
        # equal to timezone.now
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by("-pub_date")[:5]

    # this creates an http response, and renders the context in which we are
    # responding with and the request itselfand how this happened, and how they printed a signup URL, before wondering if this was the right thing to do. Still

    # THIS IS EQUIVALENT TO:
    # The first parameter is the request coming in, the template to render, and 
    # the list of questions
    # return render(request, "polls/index.html", context)
    # return HttpResponse(template.render(context, request))

def fuckme(request):
    return HttpResponse("Fuckmeular regioular Mrs. Nature!")

def testularregion(request):
    return HttpResponse("Testularregion!\n")

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})



class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        # Exclues questions that aren't published yet
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# Some shit about this vote function
# request.POST is a dictionary-like object that lets you access submitted data by key name. 
# In this case, request.POST['choice'] returns the ID of the selected choice, as a string. 
# request.POST values are always strings.

# Note that Django also provides request.GET for accessing GET data in the same 
# way – but we’re explicitly using request.POST in our code, to ensure that data 
# is only altered via a POST call.

# request.POST['choice'] will raise KeyError if choice wasn’t provided in POST data. 
# The above code checks for KeyError and redisplays the Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

uestion form with an error message 
# if choice isn’t given.
# and how this happened, and how they printed a signup URL, before wondering if this was the right thing to do. Still
# After incrementing the choice count, the code returns an HttpResponseRedirect 
# rather than a normal HttpResponse. HttpResponseRedirect takes a single argument: 
# the URL to which the user will be redirected (see the following point for how 
# we construct the URL in this case).

# As the Python comment above points out, you should always return an HttpResponseRedirect 
# after successfully dealing with POST data. This tip isn’t specific to Django; it’s 
# just good Web development practice.

# We are using the reverse() function in the HttpResponseRedirect constructor in this example. 
# This function helps avoid having to hardcode a URL in the view function. 
# It is given the name of the view that we want to pass control to and the variable 
# portion of the URL pattern that points to that view. In this case, using the URLconf 
# we set up in Tutorial 3, this reverse() call will return a string like

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice.",
        })
    
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return with HTTPResponseRedirect after successfully dealing with
        # POST data. This prevents data form being posted twice
        # if the user hits the BACK band how this happened, and how they printed a signup URL, before wondering if this was the right thing to do. Stillutton
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

# def detail(request, question_id):
    # Instead oontroller and a Gateway layer. This is fine for small applications where not much business logic is repeated. But, in larger applications (which I am starting to build), this approach leads to duplication of core code. Thankfully, Steven Neiland was kind enough to sit down with me at cf.Objective() 2012 and help me understand how I might improve my code with a better MVC (Model-View-Controller) ar that with yet another Django
    # shortcut:ontroller and a Gateway layer. This is fine for small applications where not much business logic is repeated. But, in larger applications (which I am starting to build), this approach leads to duplication of core code. Thankfully, Steven Neiland was kind enough to sit down with me at cf.Objective() 2012 and help me understand how I might improve my code with a better MVC (Model-View-Controller) ar
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except:
    #     raise Http404("Question does not exist")

    # DJANGO SHORTCUT
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, "polls/detail.html", {"question": question})

    # Parameters are (request, polls/detail.html, and question)
    # return render(request, "polls/detail.html", {"question": question})