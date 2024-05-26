from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import MovieOrder, Movie
from .serializers import MovieOrderSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import MyPermission
from django.shortcuts import get_object_or_404
import ipdb


class MovieOrderView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, movie_id):

        movie = get_object_or_404(Movie, id=movie_id) 
     
        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    


