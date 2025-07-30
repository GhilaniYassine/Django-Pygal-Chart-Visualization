import pygal
from .models import *
class AnimePieChart():
    def __init__(self,**kwargs):
        self.chart=pygal.Pie(**kwargs)
        self.chart.title='THE differnet anime genres'
        self.chart.style=pygal.style.DarkStyle
    def get_data(self):
        
        genre_counts={}
        genres = Anime.objects.values_list('genres', flat=True).distinct()
        for genre in genres:
            count = Anime.objects.filter(genres=genre).count()
            genre_counts[genre] = count
        genre_data = {genre: count for genre, count in genre_counts.items()}
        return genre_data


        
    def generate(self):
        chart_data=self.get_data()
        for key,value in chart_data.items():
            self.chart.add(key,value)
        return self.chart.render(is_unicode=True)
