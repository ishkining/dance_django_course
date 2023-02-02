from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

zodiac_dict = {
    'taurus': 'Знак зодиака Тельца',
    'aries': 'Знак зодиака Овена',
    'scorpio': 'Знак зодиака Скорпиона',
    'leo': 'Знак зодиака Льва',
}


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Unknown request - {sign_zodiac}')


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    if sign_zodiac <= len(zodiac_dict):
        return HttpResponseRedirect(f'/horoscope/{list(zodiac_dict)[sign_zodiac - 1]}/')
    return HttpResponse(f'Unknown number - {sign_zodiac}')