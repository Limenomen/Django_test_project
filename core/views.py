from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import AccessMixin
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


class MovieDeleteView(AccessMixin, TittleMixin, DeleteView):
    model = Movie

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(self.get_object().get_absolute_url())
        return super(MovieDeleteView, self).dispatch(request, *args, **kwargs)

    def get_title(self) -> str:
        return 'Удаление: ' + str(self.get_object())

    def get_success_url(self):
        return reverse('core:movies')


class DirectorDeleteView(AccessMixin, TittleMixin, DeleteView):
    model = Director

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(self.get_object().get_absolute_url())
        return super(DirectorDeleteView, self).dispatch(request, *args, **kwargs)

    def get_title(self) -> str:
        return 'Удаление: ' + str(self.get_object())

    def get_success_url(self):
        return reverse('core:directors')


class MovieCreateView(AccessMixin, TittleMixin, CreateView):
    model = Movie
    fields = '__all__'
    title = 'Добавление фильма'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('core:movies')
        return super(MovieCreateView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('core:movies')


class MovieUpdateView(AccessMixin, TittleMixin, UpdateView):
    model = Movie
    fields = '__all__'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('core:movies')
        return super(MovieUpdateView, self).dispatch(request, *args, **kwargs)

    def get_title(self) -> str:
        return 'Изменение: ' + str(self.get_object())

    def get_success_url(self):
        return self.get_object().get_absolute_url()


class DirectorCreateView(AccessMixin, TittleMixin, CreateView):
    model = Director
    fields = '__all__'
    title = 'Добавление режиссера'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('core:directors')
        return super(DirectorCreateView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('core:directors')


class DirectorUpdateView(AccessMixin, TittleMixin, UpdateView):
    model = Director
    fields = '__all__'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('core:directors')
        return super(DirectorUpdateView, self).dispatch(request, *args, **kwargs)

    def get_title(self) -> str:
        return 'Изменение: ' + str(self.get_object())

    def get_success_url(self):
        return self.get_object().get_absolute_url()


class AddReview(TittleMixin, CreateView):
    model = MovieReview
    title = 'добавление рецензии'
    template_name = 'core/review_form.html'
    fields = ['review']
    movie = None

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.movie = form.instance.movie = Movie.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return self.movie.get_absolute_url()
