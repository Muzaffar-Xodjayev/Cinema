from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Movie

# Create your views here.


class MoviesView(ListView):
    """List of movies"""
    model = Movie
    queryset = Movie.objects.filter(draft=True)
    template_name = "movies/movies.html"


class MovieDetailView(DetailView):
    """Detail of one movie"""
    model = Movie
    slug_field = "url"
    template_name = "movies/movie_detail.html"

