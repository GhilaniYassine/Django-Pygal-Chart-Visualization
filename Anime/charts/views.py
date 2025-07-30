from django.views.generic import TemplateView
from pygal.style import DarkStyle
from django.shortcuts import render,redirect
from django.http import HttpResponse
from  .models import Employee
from .charts import EmployeePieChart,EmployeeGaugeChart,EmployeeBarChart

def clear(request):
    Employee.objects.all().delete()
    return redirect('/home')
def home(request):
    if request.method=='POST':
        department=request.POST['department']
        strength=request.POST['strength']
        print(department)
        print(strength)
        Employee.objects.create(department=department, strength=strength)


    return render(request,'home.html')

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        # Instantiate our chart. We'll keep the size/style/etc.
        # config here in the view instead of `charts.py`.
        cht_employee = EmployeePieChart(
            height=600,
            width=800,
            explicit_size=True,
            style=DarkStyle
        )

        # Call the `.generate()` method on our chart object
        # and pass it to template context.
        context['cht_employee'] = cht_employee.generate()
        return context
class IndexView1(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView1, self).get_context_data(**kwargs)

        # Instantiate our chart. We'll keep the size/style/etc.
        # config here in the view instead of `charts.py`.
        cht_employee = EmployeeLineChart(
            height=600,
            width=800,
            explicit_size=True,
            style=DarkStyle
        )

        # Call the `.generate()` method on our chart object
        # and pass it to template context.
        context['cht_employee'] = cht_employee.generate()
        return context
class IndexView2(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView2, self).get_context_data(**kwargs)

        # Instantiate our chart. We'll keep the size/style/etc.
        # config here in the view instead of `charts.py`.
        cht_employee = EmployeeBarChart(
            height=600,
            width=800,
            explicit_size=True,
            style=DarkStyle
        )

        # Call the `.generate()` method on our chart object
        # and pass it to template context.
        context['cht_employee'] = cht_employee.generate()
        return context