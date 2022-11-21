from .serializers import MymovieSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from tmdb_json.models import Genre, Movie, Comment
from .models import User
# 권한
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie in user.like_movies.all():
        user.like_movies.remove(movie)
    else:
        user.like_movies.add(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def mymovie(request):
    user=request.user
    data=user.like_movies.all()
    serializer = MymovieSerializer(data, many=True)
    return Response(serializer.data)

