from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('deliv_status', deliv_status, name='deliv_status'),

]
