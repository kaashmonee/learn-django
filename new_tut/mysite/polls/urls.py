from django.urls import path
from . import views

# This is so that the app knows which namespace to use
# That is, there could be different details and stuff, but it will use this
# one because that's where the app name is

app_name = "polls"

urlpatterns = [
    path('', views.index, name='index'),
    # You can basically next our views and stuff...this is pretty cool, 
    # not going to lie
    path('fuckme/', views.fuckme, name='fuckme'),

    # We're in the polls urlsconf, so this will all be appending to polls

    # /polls/5
    path("<int:question_id>/", views.detail, name="detail"),

    # /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),

    # /polls/5/vote/
    path("<int:question_id>/vote", views.vote, name="vote")
]