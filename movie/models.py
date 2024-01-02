from datetime import date

from django.db import models

# Create your models here.


class Category(models.Model):
    """ Category """
    name = models.CharField(max_length=255, primary_key=True)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    """ Actor """
    name = models.CharField(max_length=255)
    birt_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to="actors/")

    def __str__(self):
        return self.name


class Genre(models.Model):
    """ Genres """
    name = models.CharField(max_length=150)
    description = models.TextField()
    url = models.SlugField(max_length=155, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    """Movies"""
    title = models.CharField(max_length=155)
    tagline = models.CharField(max_length=100, default="")
    description = models.TextField()
    poster = models.ImageField(upload_to="movies/")
    year = models.PositiveSmallIntegerField(default=2019)
    country = models.CharField(max_length=255)
    directors = models.ManyToManyField(Actor, related_name="film_director")
    actors = models.ManyToManyField(Actor, related_name="film_actor")
    genres = models.ManyToManyField(Genre)
    world_premiere = models.DateField(default=date.today)
    budget = models.PositiveIntegerField(default=0, help_text="write on dollars")
    fees_in_usa = models.PositiveIntegerField(default=0, help_text="write on dollars")
    fees_in_world = models.PositiveIntegerField(default=0, help_text="write on dollars")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title
