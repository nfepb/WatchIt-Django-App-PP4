from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomepageList.as_view(), name='home'),
    path('<slug:slug>', views.MovieDetails.as_view(), name='movie_details'),
    path(
        'genre/<slug:slug>', views.GenreDetails.as_view(), name='genre_details'
        ),
]
