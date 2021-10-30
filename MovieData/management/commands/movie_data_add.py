# from typing_extensions import runtime
from django.core.management.base import BaseCommand
from django.utils import timezone
import csv 
from MovieData.models import NetflixMovieData


class Command(BaseCommand):
    help = 'Netflix movie data'

    def handle(self, *args, **kwargs):
        with open("MovieData/netflixoriginals.csv",'r')as file:
            reader = csv.reader(file)
            header=next(reader)
            for i in reader:
                # print(i)
                 title = i[0]                             
                 genre = i[1]
                 premiere = i[2] 
                 runtime = i[3] 
                 imdb_score = i[4] 
                 lanaguage = i[5]
                 movie_obj=NetflixMovieData(title=title,genre=genre,premiere=premiere,runtime=runtime,imdb_score=imdb_score,lanaguage=lanaguage)
                 movie_obj.save()
                
                



  
    