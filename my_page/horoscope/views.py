from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from dataclasses import dataclass

zodiac_dict = {
    'aries': ['Знак зодиака Овена', (3, 21), (4, 19)],
    'taurus': ['Знак зодиака Тельца', (4, 20), (5, 20)],
    'leo': ['Знак зодиака Льва', (7, 23), (8, 22)],
    'scorpio': ['Знак зодиака Скорпиона', (10, 23), (11, 21)],
}

types_nature = {
    'fire': ['scorpio'],
    'water': ['aries'],
    'geo': ['taurus'],
    'wind': ['leo'],
}


def index(request):
    response = '<ol>'
    for sign in zodiac_dict.keys():
        redirect_url = reverse('horoscope-name', args=[sign])
        response += f'<li> <a href="{redirect_url}">{sign.title()}</a> </li>'
    response += '</ol>'
    return HttpResponse(response)


def types(request):
    response = '<ol>'
    for type_name in types_nature.keys():
        redirect_url = reverse('certain-type-name', args=[type_name])
        response += f'<li> <a href="{redirect_url}">{type_name.title()}</a> </li>'
    response += '</ol>'
    return HttpResponse(response)


def certain_type(request, type_name):
    response = '<ol>'
    if not types_nature.get(type_name, None):
        return HttpResponseNotFound(f'Unknown nature for us {type_name}')
    list_of_certain_type = types_nature[type_name]
    for sign in list_of_certain_type:
        redirect_url = reverse('horoscope-name', args=[sign])
        response += f'<li> <a href="{redirect_url}">{sign.title()}</a> </li>'
    response += '</ol>'
    return HttpResponse(response)


def find_by_date(request, month, day):
    our_date = (month, day)
    for sing_data in zodiac_dict.keys():
        if zodiac_dict[sing_data][1] < our_date < zodiac_dict[sing_data][2]:
            redirect_url = reverse('horoscope-name', args=[sing_data])
            return HttpResponseRedirect(redirect_url)
    return HttpResponseNotFound(f'Not found by this date {month}-{day}')


@dataclass
class Person:
    name: str
    age: int

    def __str__(self):
        return f'This is {self.name} and {self.age} years old'


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac, None)
    data = {
        'description_zodiac': description[0],
        'sign_zodiac': sign_zodiac.title(),
        'my_class': Person('Will', 55)
    }
    if description:
        return render(request, 'horoscope/info-zodiac.html', context=data)
    else:
        return HttpResponseNotFound(f'Unknown request - {sign_zodiac}')


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    if sign_zodiac <= len(zodiac_dict):
        redirect_url = reverse('horoscope-name', args=[list(zodiac_dict)[sign_zodiac - 1]])
        return HttpResponseRedirect(redirect_url)
    return HttpResponse(f'Unknown number - {sign_zodiac}')
