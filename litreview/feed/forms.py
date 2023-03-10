from django import forms
from .widgets import RatingWidget


from . import models


class EditTicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']
        labels = {'title': 'Titre'}


class EditReviewForm(forms.ModelForm):
    """
    Implement a form choicefield rating with a customized widget RatingWidget
    which associated template will transform the radio buttons in stars.
    """

    RATING_CHOICES = (
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
    )

    rating = forms.ChoiceField(
        label='',
        choices=RATING_CHOICES,
        widget=RatingWidget
    )

    class Meta:
        model = models.Review
        fields = ['rating', 'headline', 'body']
        labels = {
            'rating': "Note",
            'headline': "Titre",
            'body':
            "Commentaire"
        }
