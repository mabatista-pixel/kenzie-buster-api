from django.db import models
from movies.models import Movie
from users.models import User
from datetime import datetime

class MovieOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movie_orders')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_orders')
    purchased_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.movie.title}"