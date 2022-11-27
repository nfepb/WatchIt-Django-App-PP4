from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomepageList.as_view(), name='home'),
    path('<slug:slug>', views.MovieDetails.as_view(), name='movie_details'),
    path('add_movie/', views.AddMovie.as_view(), name='add_movie'),
    path(
        'genre/<slug:slug>', views.GenreDetails.as_view(), name='genre_details'
        ),
    path('moviebox/', views.MovieboxList.as_view(), name='moviebox'),
    path('add_movie/', views.AddMovie.as_view(), name='add_movie'),
    path('watchlist/<slug:slug>', views.WatchlistMovie.as_view(),
         name='in_watchlists'),
]
