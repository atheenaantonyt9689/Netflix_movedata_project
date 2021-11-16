from django.urls import path

from .views import NetflixMovieDataview
urlpatterns = [
path('', NetflixMovieDataview.as_view(), name='home'),
]
