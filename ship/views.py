from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return HttpResponse("Главная")


def deliv_status(request):
    return HttpResponse("Статусы заявки")


def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")
