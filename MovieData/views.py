from django.shortcuts import render
from django import views
from django.views.generic.base import View
from django.urls import reverse, reverse_lazy

from MovieData.models import NetflixMovieData

# Create your views here.
class NetflixMovieDataview(View ):

    model= NetflixMovieData

    template_name = 'movie/index.html'
    success_url = reverse_lazy('home')


    def get(self,request,*args,**kwargs):   
       
        genre_data=NetflixMovieData.objects.values('genre',).order_by('genre',).distinct()
        language_data=NetflixMovieData.objects.values('lanaguage',).order_by('lanaguage').distinct()
       
        context={
              "genre_data":genre_data,
              "language_data":language_data

        }           
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs): 
        if request.method == "POST":            

        # print(request.POST.get('genre'))
            genre=request.POST.get('genre')
            language=request.POST.get('lanaguage') 
            # print("helloooo form posttt       ",genre,language)       
            search_result = NetflixMovieData.objects.filter(genre=genre,lanaguage=language)
            count_search_result = search_result.count() 
            # print(search_result)
       
        context={
           "search_result": search_result,
           "count_search_result": count_search_result

        }           
        return render(request,self.template_name,context)





