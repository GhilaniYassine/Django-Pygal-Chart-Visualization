from django.views.generic import TemplateView
from pygal.style import DarkStyle
from django.shortcuts import render,redirect
from django.http import HttpResponse
from  .models import *
from .charts import AnimePieChart
# get the anime names from  the database 
anime_names = Anime.objects.values_list('name', flat=True)


class home(TemplateView):
    template_name = 'pie.html'

    def get_context_data(self, **kwargs):
        context = super(home, self).get_context_data(**kwargs)

        # Instantiate our chart. We'll keep the size/style/etc.
        # config here in the view instead of `charts.py`.
        cht_employee = AnimePieChart(
            height=600,
            width=800,
            explicit_size=True,
            style=DarkStyle
        )

        # Call the `.generate()` method on our chart object
        # and pass it to template context.
        context['cht_employee'] = cht_employee.generate()
        return context