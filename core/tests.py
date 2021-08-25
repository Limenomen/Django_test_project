from django.test import TestCase
from core import models
from django.urls import reverse


class DirectorModel(TestCase):
    def setUp(self):
        self.director = models.Director.objects.create(first_name='first_name', last_name='last_name')

    def test_get_absolute_url(self):
        self.assertEquals(self.director.get_absolute_url(), f'/directors/{self.director.pk}/')

    def test_str(self):
        self.assertEquals(
            str(self.director),
            f'{self.director.first_name}, {self.director.last_name}'
        )


class MovieModel(TestCase):
    def setUp(self):
        self.director = models.Director.objects.create(first_name='first_name', last_name='last_name')
        self.genre1 = models.Genre.objects.create(name='genre1')
        self.genre2 = models.Genre.objects.create(name='genre2')
        self.movie = models.Movie.objects.create(name='Movie', director=self.director)
        self.movie.genre.set([self.genre1, self.genre2])

    def test_display_genre(self):
        self.assertEqual(self.movie.display_genre(), 'genre1, genre2')

    def test_str(self):
        self.assertEqual(
            str(self.movie),
            f'{self.movie.name}, {self.movie.release_date}'
        )

    def test_get_absolute_url(self):
        self.assertEqual(self.movie.get_absolute_url(), f'/movies/{self.movie.pk}/')


class MovieSearch(TestCase):
    def setUp(self):
        self.client = Client()
        self.director = models.Director.objects.create(first_name='first_name', last_name='last_name')
        self.genre1 = models.Genre.objects.create(name='genre1')
        self.genre2 = models.Genre.objects.create(name='genre2')
        self.movie1 = models.Movie.objects.create(name='Movie1', director=self.director)
        self.movie2 = models.Movie.objects.create(name='Movie2', director=self.director)
        self.movie1.genre.set([self.genre1, self.genre2])
        self.movie2.genre.set([self.genre1, self.genre2])

    def test_search_without_params(self):
        response = self.client.get(reverse('core:movies'))
        self.assertEqual(200, response.status_code)
        self.assertSequenceEqual(
            list(response.context['object_list']),
            list(models.Movie.objects.all()),
        )

