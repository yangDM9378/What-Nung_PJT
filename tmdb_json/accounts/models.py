from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    nick_name = models.TextField()

    def __str__(self):
        return self.username
