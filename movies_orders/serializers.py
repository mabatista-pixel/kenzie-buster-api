from rest_framework import serializers
from .models import MovieOrder, Movie, User
from datetime import datetime, date



class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, required=False)
    title = serializers.CharField(source='movie.title', read_only=True, required=False)
    purchased_at = serializers.DateTimeField(read_only=True, required=False)
    price = serializers.DecimalField(max_digits=8, decimal_places=2, required=True)
    purchased_by = serializers.EmailField(source='user.email', read_only=True, required=False)


    def create(self, validated_data):

        return MovieOrder.objects.create(
         **validated_data
        )

