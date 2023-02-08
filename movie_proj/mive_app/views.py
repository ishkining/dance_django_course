from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import F, Sum, Max, Min, Count, Avg, Value


def show_all_movie(request):
    movies = Movie.objects.order_by('rating')
    for movie in movies:
        movie.save()
    movies = Movie.objects.annotate(new_field_bool=Value(True))
    return render(request, 'mive_app/all_movies.html', context= {
        'movies': movies,
    })


def show_one_movie(request, slug_movie:str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'mive_app/one_movie.html', context={
        'movie': movie,
    })

