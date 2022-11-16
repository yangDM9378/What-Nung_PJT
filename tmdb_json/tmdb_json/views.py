from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieSerializer
from .models import Genre, Movie
from django.shortcuts import render

# Create your views here.
@api_view(['GET'])
def index(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)