from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("""Greetular Mrs. Mister.\nYou are at the poll appular
                          regoiular natular madular region!""")

def fuckme(request):
    return HttpResponse("Fuckmeular regioular Mrs. Nature!")

def testularregion(request):
    return HttpResponse("Testularregion!\n")


# print ddf