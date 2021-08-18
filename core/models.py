from django.db import models
from datetime import datetime


class Genre(models.Model):
    name = models.CharField('жанр фильма', max_length=64)

    def __str__(self):
        return self.name


class Producer(models.Model):
    first_name = models.CharField('имя режиссера', max_length=64)
    last_name = models.CharField('фамилия режиссера', max_length=64)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


class Movie(models.Model):
    name = models.CharField('Название фильма', max_length=64)
    producer = models.ForeignKey('Producer', on_delete=models.SET_NULL, null=True)

    description = models.CharField('описание', max_length=1024)
    genre = models.ManyToManyField(Genre)

    YEAR_CHOICES = []
    for year in range(1950, (datetime.now().year + 5)):
        YEAR_CHOICES.append((year, year))

    release_date = models.IntegerField('год выхода', choices=YEAR_CHOICES, default=2000, blank=True)

    def __str__(self):
        return f"{self.name}, {self.release_date}"

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()])

