import pygal
from .models import Employee
class EmployeePieChart():
    def __init__(self,**kwargs):
        self.chart=pygal.Pie(**kwargs)
        self.chart.title='Employees in different department'
    def get_data(self):
        data={}
        for emp in Employee.objects.all():
            data[emp.department]=emp.strength
        return data
    def generate(self):
        chart_data=self.get_data()
        for key,value in chart_data.items():
            self.chart.add(key,value)
        return self.chart.render(is_unicode=True)
class EmployeeGaugeChart():
    def __init__(self,**kwargs):
        self.chart=pygal.Gauge(**kwargs)
        self.chart.title='Employees in different department'
    def get_data(self):
        data={}
        for emp in Employee.objects.all():
            data[emp.department]=emp.strength
        return data
    def generate(self):
        chart_data=self.get_data()
        for key,value in chart_data.items():
            self.chart.add(key,value)
        return self.chart.render(is_unicode=True)
class EmployeeBarChart():
    def __init__(self,**kwargs):
        self.chart=pygal.Bar(**kwargs)
        self.chart.title='Employees in different department'
    def get_data(self):
        data={}
        for emp in Employee.objects.all():
            data[emp.department]=emp.strength
        return data
    def generate(self):
        chart_data=self.get_data()
        for key,value in chart_data.items():
            self.chart.add(key,value)
        return self.chart.render(is_unicode=True)