from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movie),
]