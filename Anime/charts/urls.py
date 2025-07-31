
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
path('bar',home.as_view()),
path('anime_list/', anime_list, name='anime_list'),
path('',home_page, name='home_page'),
]