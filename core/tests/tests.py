from django.test import TestCase, Client
from core import models
from django.urls import reverse


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
