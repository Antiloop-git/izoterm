from django.contrib import admin

from .models import *

class ShipRequestAdmim(admin.ModelAdmin):
    list_display = ('id', 'slug', 'datetime_create', 'deliverier', 'consignee', 'cargo_quantity')
    list_display_links = ('id', 'slug')
    search_fields = ('slug', 'deliverier', 'consignee')
    prepopulated_fields = {'slug': ('slug',)}


class DeliveredStatusAdmim(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Shipping_request, ShipRequestAdmim)

admin.site.register(Delivered_status, DeliveredStatusAdmim)
