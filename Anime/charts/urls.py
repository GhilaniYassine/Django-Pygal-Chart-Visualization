
from django.contrib import admin
from django.urls import path
from charts.views import IndexView,home,IndexView1,IndexView2,clear

urlpatterns = [
  #  path('admin/', admin.site.urls),
    path('', home),
    path('index/', IndexView.as_view()),
    path('index1/', IndexView1.as_view()),
    path('index2/', IndexView2.as_view()),
    path('clear/', clear),

]