from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movie),
    path('directors/', views.show_all_directors),
    path('directors/<int:id_director>', views.show_one_director, name='director_name'),
    path('actors/', views.show_all_actors),
    path('actors/<int:id_actor>', views.show_one_actor, name='actor_name'),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie_detail'),
]