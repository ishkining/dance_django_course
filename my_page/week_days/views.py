from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

dict_days = {
    'monday': 'Deals at Monday:\n'
              'Clean teeth\n'
              'Clear Abyss\n'
              'Quality time w/ ur mom',
    'tuesday': 'Deals at Tuesday:\n'
               'Same as Monday but\n'
               'w/ ur dad',
}


def day_of_week(request, day):
    is_it_digital = True
    try:
        int(day)
    except ValueError:
        is_it_digital = False
    if is_it_digital:
        if int(day) <= len(dict_days):
            redirect_url = reverse('day-of-week-name', args=[list(dict_days)[int(day) - 1]])
            return HttpResponseRedirect(f'/todo_week/{list(dict_days)[int(day) - 1]}/')
        else:
            return HttpResponseNotFound(f'Not found this number {day}')
    else:
        description = dict_days.get(day, None)
        if description:
            return HttpResponse(description)
        else:
            return HttpResponseNotFound(f'Not found this {day}')

