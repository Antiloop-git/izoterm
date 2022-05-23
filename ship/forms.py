from django import forms
from django.forms import ModelForm

from .models import *


class AddShipForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['delivered_status'].empty_label = 'статус не выбран'

    class Meta:
        model = Shipping_request
        # delivered_status: forms.ModelChoiceField(queryset=Delivered_status.objects.all(), to_field_name='delivered_status', label="Статус заявки")

        fields = ['slug', 'delivery_information', 'deliverier', 'deliverier_phone', 'delivered_status']
        widgets = {
            'slug': forms.TextInput(attrs={'class': 'form-control form-input'}),
            'delivery_information': forms.TextInput(attrs={'class': 'form-control form-input', 'id': "basic-addon1"}),
            'deliverier': forms.TextInput(attrs={'class': 'form-control form-input'}),
            'deliverier_phone': forms.TextInput(attrs={'class': 'form-control form-input'}),
            'delivered_status': forms.Select(attrs={'class': 'form-select form-control'}),

            # 'delivered_status': forms.ModelChoiceField(queryset=Delivered_status.objects.all(),
            #                                                to_field_name='delivered_status', label="Статус заявки")
        }


    # delivery_information = forms.CharField(max_length=255, label="Информация для перевозчика")
    # slug = forms.SlugField(max_length=255, label="URL")
    # # uuid_shipping_request = forms.UUIDField(max_length=255,  label="UUID")
    # deliverier = forms.CharField(max_length=255, label="Перевозчик")
    # deliverier_phone = forms.CharField(max_length=255, label="Телефон перевозчика")
    # delivered_status = forms.ModelChoiceField(queryset=Delivered_status.objects.all(), label="Статус заявки",
    #                                           empty_label='Статус заявки не выбран')

