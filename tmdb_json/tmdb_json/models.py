from django.db import models

# Create your models here.

class Genre(models.Model):
    genre_id = models.IntegerField()
    name = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    released_date = models.DateTimeField(auto_now_add=True)
    popularity=models.FloatField()
    vote_avg=models.IntegerField()
    overview = models.TextField()
    poster_path = models.TextField()
    backdrop_path = models.TextField(null=True)
    genres = models.ManyToManyField(Genre)
    movie_id = models.IntegerField()

class Credit(models.Model):
    credit_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cast_name = models.TextField()
    profile_path = models.TextField(null=True)
