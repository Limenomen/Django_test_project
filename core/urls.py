from django.urls import path, include
import core.views

app_name = 'core'

urlpatterns = [
    path('', core.views.HomeView.as_view(), name='home'),
    path('movies/', core.views.MovieListView.as_view(), name='movies'),
    path('movie/<int:pk>/', core.views.MovieDetailView.as_view(), name='movie_detail'),
    path('director/<int:pk>/', core.views.DirectorDetailView.as_view(), name='director_detail'),
]
