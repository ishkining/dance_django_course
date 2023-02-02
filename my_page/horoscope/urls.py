from django.urls import path
from . import views

urlpatterns = [
    path('<sign_zodiac>', views.get_info_about_sign_zodiac),
]
