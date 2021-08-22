from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from core.models import Movie, Director
from django.db.models import Q, Count


class TittleMixin:

    title: str = None

    def get_title(self) -> str:
        return self.title

    def get_context_data(self, **kwargs):
        c = super().get_context_data()
        c['title'] = self.get_title()
        return c


class HomeView(TittleMixin, TemplateView):
    title = 'Главная'
    template_name = 'core/index.html'


class MovieListView(TittleMixin, ListView):
    title = 'Фильмы'
    model = Movie
    template_name = 'core/movies.html'

    def get_queryset(self):
        queryset = self.model.objects.all()
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__istartswith=name)
        return queryset


class MovieDetailView(TittleMixin, DetailView):
    model = Movie
    template_name = 'core/movie_detail.html'

    def get_title(self):
        return str(self.get_object())


class DirectorDetailView(TittleMixin, DetailView):
    model = Director
    template_name = 'core/director_detail.html'

    def get_title(self):
        return str(self.get_object())


class DirectorListView(TittleMixin, ListView):
    model = Director
    title = 'Режиссеры'
    template_name = 'core/directors.html'


    def get_queryset(self):
        queryset = self.model.objects.all()
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(Q(first_name__istartswith=name) | Q(last_name__istartswith=name))
        return queryset
