from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_ship_request/', add_ship_request, name='add_ship_request'),
    path('about', about, name='about'),
    path('login', login, name='login'),
    path('ship/<slug:ship_slug>', show_ship_request, name='ship'),
    path('delivered_status/<int:delivered_status_id>', show_delivered_status, name='delivered_status'),

]


