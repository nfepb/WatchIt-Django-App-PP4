from .models import Review, Movie
from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput


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
        fields = ('movie_title', 'director', 'year_released', 'movie_poster',
                  'synopsis', 'movie_genre')
        widgets = {
            'year_released': DatePickerInput(options={"format": "MM/DD/YYYY"})
        }
