from rest_framework import serializers
from .models import Movie, Genre, Credit, Comment

class MovieSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = ('name',)

    genres = GenreSerializer(many=True, read_only=True)
    
    class CreditSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Credit
            fields = ('cast_name', 'profile_path')

    credit_set = CreditSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie',)
