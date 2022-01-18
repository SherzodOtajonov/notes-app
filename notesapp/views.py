from django.shortcuts import render
from .models import Note

def home(request):
    context = {
        "notes": Note.objects.all(),
    }
    return render(request, 'notesapp/main.html', context)

def note(request, pk):
    note = Note.objects.get(id=pk)
    context = {
        "note": note,
    }
    return render(request, 'notesapp/note.html', context)