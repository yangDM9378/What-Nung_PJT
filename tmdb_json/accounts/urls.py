from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_pk>/movie', views.like_movie),
    path('mymovie/', views.mymovie)
]
