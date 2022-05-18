from django.contrib import admin

from .models import *

class ShipRequestAdmim(admin.ModelAdmin):
    list_display = ('id', 'uuid_shipping_request', 'slug', 'datetime_create', 'deliverier', 'consignee', 'cargo_quantity')
    list_display_links = ('id', 'uuid_shipping_request')
    search_fields = ('uuid_shipping_request', 'deliverier', 'consignee')
    prepopulated_fields = {'slug': ('uuid_shipping_request',)}


class DeliveredStatusAdmim(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Shipping_request, ShipRequestAdmim)

admin.site.register(Delivered_status, DeliveredStatusAdmim)
