from django.shortcuts import render
from .models import Movie


def show_all_movie(request):
    movies = Movie.objects.all()
    return render(request, 'mive_app/all_movies.html', context= {
        'movies': movies,
    })
