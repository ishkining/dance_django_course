from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def get_info_about_sign_zodiac(request, sign_zodiac):
    if sign_zodiac == 'taurus':
        return HttpResponse('Знак зодиака Тельца')
    elif sign_zodiac == 'aries':
        return HttpResponse('Знак зодиака Овена')
    elif sign_zodiac == 'scorpio':
        return HttpResponse('Знак зодиака Скорпиона')
    elif sign_zodiac == 'leo':
        return HttpResponse('Знак зодиака Льва')
    else:
        return HttpResponseNotFound(f'Unknown request - {sign_zodiac}')
