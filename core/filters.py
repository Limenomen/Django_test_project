import django_filters
from django_filters import FilterSet
from core import models


class MovieFilter(FilterSet):

    name = django_filters.CharFilter(lookup_expr='icontains')
    release_date = django_filters.NumberFilter()
    genre = django_filters.CharFilter(lookup_expr='exact')
    director = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = models.Movie
        fields = ['name', 'release_date', 'genre', 'director']


class DirectorFilter(FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    country = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Director
        fields = ['first_name', 'last_name', 'country']
