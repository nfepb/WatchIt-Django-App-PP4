from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, View, CreateView
from .models import Movie, Review, WatchlistItem, Genre
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddMovieForm, MovieForm
from django.utils.text import slugify
from django.contrib import messages


class HomepageList(ListView):
    """
    Looks for Movie model and returns list:
    approved = True ordered by created date on home page
    """
    model = Movie
    queryset = Movie.objects.filter(movie_approved=True).order_by(
        '-movie_created_on'
        )
    template_name = 'index.html'
    # limiting number of posts that can appear on Movie page:
    paginate_by = 8

    def get_context_data(self, **kwargs):
        """
        Takes the genre object from Genre model
        and returns a list
        """
        context_data = super().get_context_data(**kwargs)
        context_data['genre_list'] = Genre.objects.all()
        return context_data


class WatchlistList(ListView):
    """
    Looks for WatchlistItem model and returns list:
    movies approved = True ordered by added date on watchlist page
    """
    model = WatchlistItem
    queryset = WatchlistItem.objects.filter(
        ).order_by('-added_on')
    template_name = 'forum/watchlist.html'
    paginate_by = 12
    context_object_name = 'watchlist'


class MovieDetails(View):
    """
    Displays movie object from Movie model &
    reviews posted on this object.
    Based on the I Think Therefore I Blog Project:
    The Post Detail View - part 1
    """

    def get(self, request, slug, *args, **kwargs):
        """
        Gets full movie detail with associated reviews
        """
        queryset = Movie.objects.filter(movie_approved=True)
        movie = get_object_or_404(queryset, slug=slug)
        reviews = movie.reviews.order_by('-review_created_on')

        return render(
            request,
            'movie_details.html',
            {
                'movie': movie,
                'reviews': reviews,
                'reviewed': False,
                'review_form': MovieForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Display Movie details with associated reviews
        Current user can post a review form for approval
        """
        queryset = Movie.objects.filter(movie_approved=True)
        movie = get_object_or_404(queryset, slug=slug)
        reviews = movie.reviews.order_by('-review_created_on')

        review_form = MovieForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review_form.instance.author = request.user
            review_form.instance.reviewed_movie = movie
            review.movie = movie
            review.save()

        else:
            review_form = MovieForm()

        return render(
            request,
            'movie/movie_details.html',
            {
                'movie': movie,
                'reviews': reviews,
                'reviewed': True,
                'review_form': review_form
            },
        )


class GenreDetails(View):
    """
    Returns all the genre object from the genre model
    filtered by the genre category and with movie_approved = True
    """

    def get(self, request, slug, *args, **kwargs):
        """
        Get all the genre objects from the Genre model
        and the specific slug of the genre object
        Gets all the movie objects filtered then by
        their genre with movie_approved = True
        returns the single genre object instance,
        the movie object and the genre object list
        """

        genre_object = Genre.objects.all()
        genres = get_object_or_404(genre_object, slug=slug)
        movies = genres.movie_genre.filter(
            movie_approved=True).order_by('-movie_created_on')

        return render(
            request,
            'genre_details.html',
            {
                'movies': movies,
                'genres': genres,
                'genre_object': genre_object
            },
        )


class MovieboxList(ListView):
    """
    Takes the movie object from Movie model
    and returns list of approved = True
    and in order of when they were created
    in the Moviebox page
    """
    model = Movie
    queryset = Movie.objects.filter(
        movie_approved=True).order_by('-movie_created_on')
    template_name = 'moviebox.html'
    paginate_by = 8
    context_object_name = 'moviebox'

    def get_queryset(self):
        """
        Gets the user input in the search field
        in the template and returns a list of movie
        from the Movie model filtered by title,
        director and synposis and the movie
        has approved = True
        """
        name = self.request.GET.get('search', '')
        object_list = Movie.objects.filter(movie_approved=True)
        if name:
            object_list = object_list.filter(
                Q(movie_title__icontains=name) | Q(director__icontains=name) |
                Q(synopsis__icontains=name))
        return object_list


class AddMovie(LoginRequiredMixin, CreateView):
    """
    View verifying if user is logged in before accessing
    form template.
    Calls AddMovieForm from forms.py
    """
    template_name = 'add_movie.html'
    form_class = AddMovieForm

    def get_success_url(self):
        """
        sets the reverse url for the
        successful addition of the book
        to the database
        """
        return reverse('moviebox')

    def form_valid(self, form):
        """
        validates the form and adds a success message
        to the template once movie is successfully added
        Sets the automatic slug for the object created
        from the user input on the movie_title and director
        fields
        """
        form = form.save(commit=False)
        messages.success(
            self.request,
            'Thank you for adding a new movie. It has been flagged for validation!')
        form.slug = slugify(form.movie_title + "-" + form.director)
        return super().form_valid(form)
