from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("note/<str:pk>", views.note, name="note"),
]