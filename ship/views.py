from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from ship.models import *

menu = [{'title': 'Главная', 'url_name': 'index'},
        {'title': 'Контакты', 'url_name': 'about'},
        {'title': 'Добавить заявку', 'url_name': 'add_ship_request'},
        {'title': 'Войти', 'url_name': 'login'}
]

def index(request):
    ship_request = Shipping_request.objects.all()
    context = {
        'ship_request': ship_request,
        'menu': menu[:-1],
        'title': 'Главная страница'
    }
    return render(request, 'ship/index.html', context=context)


def deliv_status(request):
    return HttpResponse("Статусы заявки")


def about(request):
    context = {
        'menu': menu[:-1],
        'title': 'Контакты'
    }
    return render(request, 'ship/about.html', context=context)

def login(request):
    context = {
        'menu': menu[:-1],
        'title': 'login'
    }
    return render(request, 'ship/login.html', context=context)


def add_ship_request(request):
    context = {
        'menu': menu,
        'title': 'Добавить заявку'
    }
    return render(request, 'ship/add_ship_request.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")


def show_ship_request(request, ship_slug):
    return HttpResponse(f'Заказ на отгрузку: {ship_slug}')
    # return render(request, 'ship/ship_detail.html', context=context)

