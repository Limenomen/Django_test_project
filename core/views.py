from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView, UpdateView
from core.models import Movie, Director, MovieReview
from django.urls import reverse
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


class MovieDeleteView(TittleMixin, DeleteView):
    model = Movie

    def get_title(self) -> str:
        return 'Удаление: ' + str(self.get_object())

    def get_success_url(self):
        return reverse('core:movies')


class DirectorDeleteView(TittleMixin, DeleteView):
    model = Director

    def get_title(self) -> str:
        return 'Удаление: ' + str(self.get_object())

    def get_success_url(self):
        return reverse('core:directors')


class MovieCreateView(TittleMixin, CreateView):
    model = Movie
    fields = '__all__'
    title = 'Добавление фильма'

    def get_success_url(self):
        return reverse('core:movies')


class MovieUpdateView(TittleMixin, UpdateView):
    model = Movie
    fields = '__all__'

    def get_title(self) -> str:
        return 'Изменение: ' + str(self.get_object())

    def get_success_url(self):
        return self.get_object().get_absolute_url()


class DirectorCreateView(TittleMixin, CreateView):
    model = Director
    fields = '__all__'
    title = 'Добавление режиссера'

    def get_success_url(self):
        return reverse('core:directors')


class DirectorUpdateView(TittleMixin, UpdateView):
    model = Director
    fields = '__all__'

    def get_title(self) -> str:
        return 'Изменение: ' + str(self.get_object())

    def get_success_url(self):
        return self.get_object().get_absolute_url()


class AddReview(CreateView):
    model = MovieReview
    template_name = 'core/review_form.html'
    fields = ['review']
    movie = None

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.movie = form.instance.movie = Movie.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return self.movie.get_absolute_url()
