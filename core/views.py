from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Movie, Director


class HomeView(TemplateView):
    template_name = 'core/index.html'


class MovieListView(ListView):
    model = Movie
    template_name = 'core/movies.html'


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'core/movie_detail.html'


class DirectorDetailView(DetailView):
    model = Director
    template_name = 'core/director_detail.html'
