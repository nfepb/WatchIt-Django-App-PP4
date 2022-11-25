from .models import Review, Movie
from django import forms


class MovieForm(forms.ModelForm):
    """
    Form for Movie Review
    """
    class Meta:
        """
        Form has field of review_detail
        from Review model
        It has a custom name of Review
        """
        model = Review
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = 'Review'


class AddMovieForm(forms.ModelForm):
    """
    Form to add a new movie
    """
    class Meta:
        """
        Form has the user facing fields from the
        movie model
        """
        model = Movie
        fields = ('movie_title', 'director', 'movie_poster',
                  'synopsis', 'movie_genre')
