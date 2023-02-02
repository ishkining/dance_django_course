from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>', views.find_rectangle),
    path('square/<int:width>', views.find_square),
    path('circle/<int:radius>', views.find_circle),
    path('get_rectangle/<int:width>/<int:height>', views.get_rectangle),
    path('get_square/<int:width>', views.get_square),
    path('get_circle/<int:radius>', views.get_circle),
]