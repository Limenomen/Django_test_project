from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from core.models import Movie, Director, Actor


class ListMixin:

    def get_queryset(self):
        queryset = self.model.objects.all()
        print(list(queryset))
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__istartswith=name)
        print(name)
        return queryset


class HomeView(TemplateView):
    template_name = 'core/index.html'


class MovieListView(ListMixin, ListView):
    model = Movie
    template_name = 'core/movies.html'


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'core/movie_detail.html'


class DirectorDetailView(DetailView):
    model = Director
    template_name = 'core/director_detail.html'


class ActorListView(ListView):
    model = Actor
    template_name = 'core/actors.html'
