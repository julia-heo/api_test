from django.contrib import admin
from django.urls import path
from .views import *

app_name='api'      

urlpatterns = [
    path('test/',testView),
    path("won/tocken/",tockenView),
    path("home/",homeView)
]