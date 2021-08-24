from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from core.models import Movie, Director
from django.db.models import Q, Count
import core.forms
import core.filters


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

    def get_filters(self):
        return core.filters.MovieFilter(self.request.GET)

    def get_context_data(self, **kwargs):
        c = super().get_context_data()
        c['form'] = core.forms.MovieSearch(self.request.GET or None)
        return c

    def get_queryset(self):
        return self.get_filters().qs


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

    def get_filters(self):
        return core.filters.DirectorFilter(self.request.GET)

    def get_context_data(self, **kwargs):
        c = super().get_context_data()
        c['form'] = core.forms.DirectorSearch(self.request.GET or None)
        return c

    def get_queryset(self):
        return self.get_filters().qs
