from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class MovieRating(models.TextChoices):
    G = 'G'
    PG = 'PG'
    PG_13 = 'PG-13'
    R = 'R'
    NC_17 = 'NC-17'


class Movie(models.Model):

    user = models.ForeignKey('users.User', related_name='movies', on_delete=models.CASCADE)

    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, default='', blank=True)
    rating = models.CharField(max_length=20, choices=MovieRating.choices, default=MovieRating.G)
    synopsis = models.TextField(default='', blank=True)

    def __str__(self):
        return self.title