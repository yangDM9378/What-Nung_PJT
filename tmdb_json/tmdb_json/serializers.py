from rest_framework import serializers
from .models import Movie, Genre, Credit

class MovieSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = ('name',)

    genres = GenreSerializer(many=True, read_only=True)
    
    class CreditSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Credit
            fields = ('cast_name',)

    credit_set = CreditSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
