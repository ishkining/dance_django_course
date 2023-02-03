from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('type/', views.types),
    path('type/<str:type_name>', views.certain_type, name='certain-type-name'),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<int:month>/<int:day>', views.find_by_date),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope-name'),
]
