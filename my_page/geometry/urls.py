from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>', views.find_rectangle, name='rectangle-name'),
    path('square/<int:width>', views.find_square, name='square-name'),
    path('circle/<int:radius>', views.find_circle, name='circle-name'),
    path('get_rectangle/<int:width>/<int:height>', views.get_rectangle),
    path('get_square/<int:width>', views.get_square),
    path('get_circle/<int:radius>', views.get_circle),
]