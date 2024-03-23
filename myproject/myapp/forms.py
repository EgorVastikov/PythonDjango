from django import forms
from .models import Note

class ModelForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text']