from django.shortcuts import render

# Create your views here.

def index(request):
    # returns and renders the home.html file
    return render(request, 'personal/home.html')