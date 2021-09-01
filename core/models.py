from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField('жанр фильма', max_length=64)

    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField('имя режиссера', max_length=64)
    last_name = models.CharField('фамилия режиссера', max_length=64)
    date_of_birth = models.DateField('дата рождения', null=True, blank=True)
    date_of_death = models.DateField('дата смерти', null=True, blank=True)
    country = models.CharField('страна', max_length=32, null=True, blank=True)
    biography = models.TextField('биография', max_length=4096, null=True, blank=True)
    image = models.ImageField('Изображение', upload_to='directors/', blank=True)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    def get_absolute_url(self):
        return reverse('core:director_detail', args=[str(self.pk)])


class Movie(models.Model):
    name = models.CharField('Название фильма', max_length=64)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    description = models.TextField('описание', max_length=4096, blank=True)
    genre = models.ManyToManyField(Genre)
    image = models.ImageField('Изображение', upload_to='movies/', blank=True)

    YEAR_CHOICES = [(year, year) for year in range(1950, (datetime.now().year + 5))]
    release_date = models.IntegerField('год выхода', choices=YEAR_CHOICES, default=2000, blank=True)

    def __str__(self):
        return f"{self.name}, {self.release_date}"

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()])

    def get_absolute_url(self):
        return reverse('core:movie_detail', args=[str(self.pk)])


class MovieReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    review = models.TextField('рецензия', max_length=4096)

    def __str__(self):
        return self.review
