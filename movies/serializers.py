from rest_framework import serializers
from .models import Movie, MovieRating
from django.contrib.auth import get_user_model


User = get_user_model()


class MovieSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    rating = serializers.CharField(required=False)
    duration = serializers.CharField(required=False)
    synopsis = serializers.CharField(required=False)
    added_by = serializers.SerializerMethodField(read_only=True)

    def validate_rating(self, value):
        valid_ratings = [choice.value for choice in MovieRating]
        if value not in valid_ratings:
            raise serializers.ValidationError("f\"{value}\" is not a valid choice.")
        return value

    def get_added_by(self, obj):
        return obj.user.email if obj.user else None
    
    def create(self, validated_data):
        user = validated_data.pop('user', None)
        if not user:
            raise serializers.ValidationError("User is required to create a movie.")
        
        movie = Movie.objects.create(user=user, **validated_data)
        return movie