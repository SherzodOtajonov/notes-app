from django.forms import ModelForm 
from django.db.models import fields
from .models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']