from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

# Create your views here.

def index(request):
    return render(request, "chat/index.html", {})

# No clue what's going on here...
def room(request, room_name):
    # renders the page, the request, and the json?
    return render(request, "chat/room.html", {
        "room_name_json": mark_safe(json.dumps(room_name))
    })