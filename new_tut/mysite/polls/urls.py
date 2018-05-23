from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # You can basically next our views and stuff...this is pretty cool, 
    # not going to lie
    path('fuckme/', views.fuckme, name='fuckme'),
    # path('anothertest/testular/', views.testularregion, name='testular'),
]