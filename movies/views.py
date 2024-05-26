from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from .models import Movie
from .serializers import MovieSerializer
from .permissions import MyCustomPermission


class MovieView(APIView, PageNumberPagination):

    permission_classes = [MyCustomPermission]
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        movies = Movie.objects.all()
        result_page = self.paginate_queryset(movies, request, view=self)
        serializer = MovieSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)
    

class MovieDetailView(APIView):

    permission_classes = [MyCustomPermission]
    
    def get(self, request, movie_id):
        movie = Movie.objects.filter(id=movie_id).first()
        if movie:
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        return Response({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, movie_id):
        movie = Movie.objects.filter(id=movie_id).first()
        if movie:
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
