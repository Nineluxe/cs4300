from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('movies-file/', views.moviesListTest, name='movies')
]
