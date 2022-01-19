from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm


def home(request):
    context = {
        "notes": Note.objects.all(),
        "notes_count": Note.objects.all().count(),
    }
    return render(request, 'notesapp/main.html', context)


def note(request, pk):
    note = Note.objects.get(id=pk)
    context = {
        "note": note,
    }
    return render(request, 'notesapp/note.html', context)


def make_note(request):
    form = NoteForm()

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {
        'form': form,
    }

    return render(request, 'notesapp/note_form.html', context)


def edit_note(request, pk):
    note = Note.objects.get(id=pk)
    form = NoteForm(instance=note)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {
        'form': form,
    }
    return render(request, 'notesapp/note_form.html', context)


def delete_note(request, pk):
    note = Note.objects.get(id=pk)

    if request.method == 'POST':
        note.delete()
        return redirect('home')

    context = {
        'object': note,
    }
    return render(request, 'notesapp/delete_template.html', context)

    pass