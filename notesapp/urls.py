from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("note/<str:pk>", views.note, name="note"),
    path("make-note", views.make_note, name="make-note"),
    path("edit-note/<str:pk>", views.edit_note, name="edit-note"),
]