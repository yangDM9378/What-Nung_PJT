from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('moives/<int:movie_pk>/comments/', views.comment_create),
    path('movies/<int:movie_pk>/cnt/', views.cnt),
]
