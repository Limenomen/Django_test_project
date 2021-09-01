from django.urls import path, include
import core.views

app_name = 'core'

urlpatterns = [
    path('', core.views.HomeView.as_view(), name='home'),
    path('movies/', core.views.MovieListView.as_view(), name='movies'),
    path('movies/create', core.views.MovieCreateView.as_view(), name='movie_create'),
    path('movies/<int:pk>/', core.views.MovieDetailView.as_view(), name='movie_detail'),
    path('movies/<int:pk>/delete/', core.views.MovieDeleteView.as_view(), name='movie_delete'),
    path('movies/<int:pk>/update/', core.views.MovieUpdateView.as_view(), name='movie_update'),
    path('movies/add_review/<int:pk>/', core.views.AddReview.as_view(), name='movie_add_review'),
    path('directors/', core.views.DirectorListView.as_view(), name='directors'),
    path('directors/create', core.views.DirectorCreateView.as_view(), name='director_create'),
    path('directors/<int:pk>/', core.views.DirectorDetailView.as_view(), name='director_detail'),
    path('directors/<int:pk>/update/', core.views.DirectorUpdateView.as_view(), name='director_update'),
    path('directors/<int:pk>/delete/', core.views.DirectorDeleteView.as_view(), name='director_delete'),
]
