from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import (
    ListView, View, CreateView, UpdateView, DeleteView)
from .models import Movie, Review, WatchlistItem, Genre
from .forms import AddMovieForm, MovieForm
from django.utils.text import slugify
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.db.models import Q


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
        in_watchlists = False
        if movie.in_watchlists.filter(id=self.request.user.id).exists():
            in_watchlists = True

        return render(
            request,
            'movie_details.html',
            {
                'movie': movie,
                'reviews': reviews,
                'reviewed': False,
                'in_watchlists': in_watchlists,
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
        in_watchlists = False
        if movie.in_watchlists.filter(id=self.request.user.id).exists():
            in_watchlists = True

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
            'movie_details.html',
            {
                'movie': movie,
                'reviews': reviews,
                'reviewed': True,
                'in_watchlists': in_watchlists,
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


class WatchlistMovie(View):
    """
    Users can add or remove the movie object
    to their watchlist
    """
    def post(self, request, slug, *args, **kwargs):
        """
        Gets the specific movie from Movie model
        Checks if the user has added the movie to the watchlist
        and adds or removes the user which will be called
        via template movie_details
        """
        movie = get_object_or_404(Movie, slug=slug)

        if movie.in_watchlists.filter(id=request.user.id).exists():
            movie.in_watchlists.remove(request.user)
        else:
            movie.in_watchlists.add(request.user)

        return HttpResponseRedirect(reverse('movie_details', args=[slug]))


class MyWatchlist(LoginRequiredMixin, CreateView):
    """
    Gets all the current users saved movies from watchlist
    and all the user's reviews and displays them
    on the template
    If the user is logged in, the my_watchlist template
    can be accessed
    """

    def get(self, request, *args, **kwargs):
        """
        Establishes the current user
        Gets all the movies where in_watchlists =
        current user
        Gets all the reviews where the author =
        current user
        returns the user movies watchlisted and user reviews
        and the current user username
        """
        username = request.user
        user_watchlist = Movie.objects.filter(in_watchlists=request.user)
        author = Review.objects.filter(author=username)
        return render(
            request, 'my_watchlist.html', {
                'user_watchlist': user_watchlist,
                'author': author,
                'username': username,
            })


class EditReview(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """
    Logged in user can edit any reviews they posted
    template is edit_review.html
    reverse url is my_watchlist.html
    """

    model = Review
    fields = [
        'content',
    ]
    template_name = 'edit_review.html'
    success_url = reverse_lazy('my_watchlist')
    success_message = "You have updated your review succesfully!"

    def get_context_data(self, **kwargs):
        """
        Get the object instance's movie title
        """
        context = super().get_context_data(**kwargs)
        context['movie_title'] = self.object.reviewed_movie

        return context

    def form_valid(self, form):
        """
        Validate form
        Save and return the new object
        """
        form.save()
        return super().form_valid(form)


class DeleteReview(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    """
    Delete the current's user's review
    template is delete_review.html
    reverse url is my_watchlist.html
    """
    model = Review
    success_url = reverse_lazy('my_watchlist')
    success_message = "Review successfully deleted!"
    template_name = 'delete_review.html'

    def get_context_data(self, **kwargs):
        """
        Get and return the object instance movie_title,
        content, current user's username,
        review date created on
        """
        context = super().get_context_data(**kwargs)
        context['reviewed_movie'] = self.object.reviewed_movie
        context['content'] = self.object.content
        context['user'] = self.object.author
        context['date'] = self.object.review_created_on

        return context


class AdminOnly(UserPassesTestMixin, ListView):
    """
    Checks that the user = superuser
    Gets list of movies from Movie model with
    movie_approved = False
    Gets a list of reviews from Review
    template is admin_only.html
    """

    def test_func(self):
        """
        Checks if the current user is
        a superuser and allows access to
        the template if they are
        """
        return self.request.user.is_superuser

    template_name = 'admin_only.html'
    model = Movie
    queryset = Movie.objects.filter(
        movie_approved=False).order_by('-movie_created_on')
    context_object_name = 'for_approval'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        """
        Gets the review from the Review model
        """
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.order_by(
            '-review_created_on'
            )
        return context


class EditMovieListing(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """
    Checks the user = superuser
    Gets the movie object from
    Movie model and allows superuser
    to update the movie object
    template is approve_movie.html
    """

    model = Movie
    fields = [
        'movie_title',
        'director',
        'synopsis',
        'year_released',
        'movie_genre',
    ]
    template_name = 'approve_movie.html'
    success_url = reverse_lazy('admin_only')
    success_message = "You approved the movie"

    def test_func(self):
        """
        Checks if the current user = superuser 
        and allows access to template if yes
        """
        return self.request.user.is_superuser

    def form_valid(self, form):
        """
        Validate form
        Set the movie_approved status to True
        Save and return the new object
        """
        form.instance.movie_approved = True
        form.save()
        return super().form_valid(form)


class DeleteMovie(SuccessMessageMixin, DeleteView):
    """
    Gets the movie object instance from
    Movie model and allows the superuser
    to delete the movie object
    """
    model = Movie
    success_url = reverse_lazy('admin_only')
    success_message = "Movie successfully deleted!"
