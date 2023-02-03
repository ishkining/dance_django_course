from math import pi

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def find_rectangle(request, width, height):
    return HttpResponse(f'The area of rectangle is {width * height}')


def find_square(request, width):
    return HttpResponse(f'The area of square is {width ** 2}')


def find_circle(request, radius):
    return HttpResponse(f'The are of circle is {pi * radius ** 2}')


def get_rectangle(request, width, height):
    redirect_url = reverse('rectangle-name', args=(width, height))
    return HttpResponseRedirect(redirect_url)


def get_square(request, width):
    redirect_url = reverse('square-name', args=(width, ))
    return HttpResponseRedirect(redirect_url)


def get_circle(request, radius):
    redirect_url = reverse('circle-name', args=(radius, ))
    return HttpResponseRedirect(redirect_url)
