from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main),
    path('moives/<int:movie_pk>/comments/', views.comment_create),
]
