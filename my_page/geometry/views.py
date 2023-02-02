from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from math import pi


def find_rectangle(request, width, height):
    return HttpResponse(f'The area of rectangle is {width * height}')


def find_square(request, width):
    return HttpResponse(f'The area of square is {width ** 2}')


def find_circle(request, radius):
    return HttpResponse(f'The are of circle is {pi * radius ** 2}')


def get_rectangle(request, width, height):
    return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}')


def get_square(request, width):
    return HttpResponseRedirect(f'/calculate_geometry/square/{width}')


def get_circle(request, radius):
    return HttpResponseRedirect(f'/calculate_geometry/circle/{radius}')
