from django.db import models

# Create your models here.
class NetflixMovieData(models.Model):

    title = models.CharField(max_length=100)
    genre  = models.CharField(max_length=100)
    premiere = models.CharField(max_length=50)
    runtime = models.CharField(max_length=30)
    imdb_score = models.CharField(max_length=30)
    lanaguage = models.CharField(max_length=100)

    def __str__(self):        
        return self.title