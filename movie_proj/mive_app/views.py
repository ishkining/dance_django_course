from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from django.db.models import F, Sum, Max, Min, Count, Avg, Value


def show_all_movie(request):
    movies = Movie.objects.order_by('rating')
    for movie in movies:
        movie.save()
    movies = Movie.objects.annotate(new_field_bool=Value(True))
    return render(request, 'mive_app/all_movies.html', context={
        'movies': movies,
    })


def show_all_directors(request):
    directors = Director.objects.all()
    return render(request, 'mive_app/directors.html', context={
        'directors': directors
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'mive_app/one_movie.html', context={
        'movie': movie,
    })


def show_one_director(request, id_director: int):
    director = Director.objects.get(id=id_director)
    return render(request, 'mive_app/director_info.html', context={
        'director': director
    })


def show_all_actors(request):
    actors = Actor.objects.all()
    return render(request, 'mive_app/actors.html', context={
        'actors': actors
    })


def show_one_actor(request, id_actor: int):
    actor = Actor.objects.get(id=id_actor)
    return render(request, 'mive_app/actors_info.html', context={
        'actor': actor
    })
