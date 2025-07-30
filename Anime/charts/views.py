from django.views.generic import TemplateView
from pygal.style import DarkStyle
from django.shortcuts import render,redirect
from django.http import HttpResponse
from  .models import *
from .charts import AnimePieChart
# get the anime names from  the database 
anime_names = Anime.objects.values_list('name', flat=True)

def home(request):

    
    return render(request, 'pie.html')