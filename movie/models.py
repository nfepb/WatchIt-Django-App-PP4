from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models import Avg


class Movie(models.Model):
    """
    Movie Class model
    """
    movie_title = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=200, null=False, unique=True)
    movie_genre = models.ForeignKey(
        'Genre', on_delete=models.PROTECT, related_name='movie_genre'
        )
    director = models.CharField(max_length=200, null=False, blank=False)
    year_released = models.DateField()
    synopsis = models.TextField()
    movie_poster = CloudinaryField('image', default='placeholder')
    movie_approved = models.BooleanField(default=False)
    movie_created_on = models.DateTimeField(auto_now_add=True)
    movie_updated_on = models.DateTimeField(auto_now=True)
    in_watchlists = models.ManyToManyField(
        User,
        related_name='in_watchlists',
        blank=True
    )

    class Meta:
        """
        Order our movies based on decreasing average rating order
        """
        # TO BE MODIFIED BY "-average_rating"
        ordering = ['-movie_created_on']
        constraints = [
            models.UniqueConstraint(fields=['movie_title', 'director'],
                                    name='unique_movie_listing')
        ]

    def __str__(self):
        return self.movie_title

    def count_in_watchlists(self):
        """
        Returns count of movies in user watchlist
        """
        return self.in_watchlists.count()


class Review(models.Model):
    """
    Review Class model
    """
    reviewed_movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="reviews"
        )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True,
        related_name="author"
        )
    content = models.TextField()
    review_created_on = models.DateTimeField(auto_now_add=True)
    review_updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, related_name="review_likes", blank=True
        )

    class Meta:
        ordering = ['-review_created_on', '-review_updated_on']

    def __str__(self):
        return f"Review by {self.author}: {self.content}"


class Genre(models.Model):
    """
    Genre Class Model
    """
    genre_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, null=False, unique=True)
    genre_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.genre_name


STATUS = (
    (0, "Not yet watched"),
    (1, "Watched")
)


class WatchlistItem(models.Model):
    """
    WatchlistItem Class model
    """
    watchlistItem_movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="movie_watchlist"
        )
    watchlistItem_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_watchlist"
        )
    movie_status = models.IntegerField(choices=STATUS, default=0)
    added_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-added_on']

    def __str__(self):
        return f"Added {self.watchlistItem_movie} to list of {self.watchlistItem_user}"
