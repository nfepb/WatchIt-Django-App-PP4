from django.contrib import admin
from .models import Movie, Review, Genre, WatchlistItem


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # Defines the fields visible in Admin panel for the Movie model

    list_display = (
        'movie_title', 'movie_genre', 'director', 'movie_genre',
        'year_released', 'movie_created_on'
        )
    # From Django Slug Tutorial:
    prepopulated_fields = {'slug': ('movie_title', 'director')}
    search_fields = ('movie_title', 'director')
    list_filter = ('movie_updated_on', 'movie_genre')
    actions = ['approve_movies']

    def approve_movies(self, request, queryset):
        # Function to approve newly added movies
        queryset.update(movie_approved=True)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # Defines the fields visible in Admin panel for the Review model

    list_display = (
        'reviewed_movie', 'author', 'review_created_on'
        )
    search_fields = ('author', 'content')
    list_filter = ('review_created_on', 'reviewed_movie')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    # Defines the fields visible in Admin panel for the Genre model

    # From Django Slug Tutorial:
    prepopulated_fields = {'slug': ['genre_name']}
    list_filter = ['genre_name']
    list_display = ('genre_name', 'slug')


@admin.register(WatchlistItem)
class WatchlistItemAdmin(admin.ModelAdmin):
    # Defines the fields visible in Admin panel for the Watchlist model

    list_display = (
        'watchlistItem_movie', 'watchlistItem_user', 'movie_status',
        'added_on'
        )
    search_fields = ('watchlistItem_movie', 'watchlistItem_user')
    list_filter = ['movie_status']
