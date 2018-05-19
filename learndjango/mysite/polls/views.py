from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("""Hello, world. You're at the polls index. Please
                          feel free to eat my dick""")



# Create your views here.
