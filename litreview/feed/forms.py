from django import forms

from . import models


class EditTicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']
        labels = {'title': 'Titre'}


class EditReviewForm(forms.ModelForm):

    class Meta:
        model = models.Review
        fields = ['rating', 'headline', 'body']
        labels = {
            'rating': "Note",
            'headline': "Titre",
            'body':
            "Commentaire"
        }
