from django.urls import path
from . import views

urlpatterns = [
    path('<day>/', views.day_of_week, name='day-of-week-name'),
]