from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404

from ship.models import *

menu = [{'title': 'Главная', 'url_name': 'index'},
        {'title': 'Контакты', 'url_name': 'about'},
        {'title': 'Добавить заявку', 'url_name': 'add_ship_request'},
        {'title': 'Войти', 'url_name': 'login'}
]

def index(request):
    ship_requests = Shipping_request.objects.all()
    deliv_statuses = Delivered_status.objects.all()
    context = {
        'ship_requests': ship_requests,
        'deliv_statuses': deliv_statuses,
        'menu': menu[:-1],
        'title': 'Список заявок на отгрузку',
        'delivered_status_selected': 0
    }
    return render(request, 'ship/index.html', context=context)


# def deliv_status(request):
#     return HttpResponse("Статусы заявки")


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
    ship_request = get_object_or_404(Shipping_request, slug=ship_slug)
    context = {
        'ship_request': ship_request,
        'menu': menu[:-1],
        'title': ship_request.uuid_shipping_request

    }
    return render(request, 'ship/ship_detail.html', context=context)


def show_delivered_status(request, delivered_status_id):
    ship_requests = Shipping_request.objects.filter(delivered_status_id=delivered_status_id)
    deliv_statuses = Delivered_status.objects.all()

    if len(ship_requests) == 0:
        raise Http404()

    context = {
        'ship_requests': ship_requests,
        'deliv_statuses': deliv_statuses,
        'menu': menu[:-1],
        'title': 'Отображение по статусам',
        'delivered_status_selected': delivered_status_id,

    }
    return render(request, 'ship/index.html', context=context)

