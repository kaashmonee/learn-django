from django.conf.urls import url

from . import views

urlpatterns= [
    # Routes to index and room name
    url(r'^$', views.index, name="index"),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name="room"),
]