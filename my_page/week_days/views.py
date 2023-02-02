from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def day_of_week(request, day):
    if day == 'monday':
        return HttpResponse('Deals at Monday:\n'
                            'Clean teeth\n'
                            'Clear Abyss\n'
                            'Quality time w/ ur mom')
    elif day == 'tuesday':
        return HttpResponse('Deals at Tuesday:\n'
                            'Same as Monday but\n'
                            'w/ ur dad')
    else:
        return HttpResponseNotFound(f'Not found this {day}')
