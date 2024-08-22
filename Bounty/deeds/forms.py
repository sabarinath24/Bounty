from django import forms
from .models import Deed

class DeedForm(forms.ModelForm):
    class Meta:
        model = Deed
        fields = ['title', 'description']
