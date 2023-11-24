

from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("wf",views.weather,name='weather'),
    path("",views.home,name='home'),
    path("todo",views.index,name='todo'),
    path("calculator",views.calculator,name='calculator'),
    path("contact",views.index,name='contact'),
    path("del/<int:pk>",views.delete,name='delete')
     
]

