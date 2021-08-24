from django import forms
import core.models


class MovieSearch(forms.Form):
    name = forms.CharField(label='Название', required=False)
    release_date = forms.IntegerField(label='Год выхода', required=False)
    genre = forms.ModelMultipleChoiceField(label='жанр', queryset=core.models.Genre.objects.all(), required=False)
    director = forms.ModelChoiceField(label='Режиссер', queryset=core.models.Director.objects.all(), required=False)


class DirectorSearch(forms.Form):
    first_name = forms.CharField(label='имя', required=False)
    last_name = forms.CharField(label='фамилия', required=False)
    country = forms.CharField(label='страна', required=False)
