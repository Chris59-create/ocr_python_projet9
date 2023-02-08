from django import forms
from authentication.models import User

from . import models


class EditTicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']
