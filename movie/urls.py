from django.urls import path
from .views import *


urlpatterns = [
    path("", MoviesView.as_view(), name="movie-page"),
    path("<slug:slug>/", MovieDetailView.as_view(), name="movie-detail-page"),
]
