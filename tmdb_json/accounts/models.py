from django.contrib.auth.models import AbstractUser
from django.db import models
from tmdb_json.models import Movie

# Create your models here.
class User(AbstractUser):
    nick_name = models.TextField()
    like_movies = models.ManyToManyField(Movie, related_name='like_users')
    def __str__(self):
        return self.username