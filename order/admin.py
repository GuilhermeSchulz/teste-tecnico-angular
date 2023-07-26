from django.contrib import admin
from .models import Order
import requests
import json
from freight.models import Freight
from django.shortcuts import render
from dotenv import load_dotenv
import os

load_dotenv()


class FreightInline(admin.TabularInline):
    model = Freight
    extra = 0
    readonly_fields = ['carrier', 'delivery_time',
                       'delivery_cost', 'external_freight_id']


class AdminModel(admin.ModelAdmin):
    list_display = ('id', 'number', 'amount', 'weight', 'width',
                    'height', 'length', 'zip_from', 'zip_to')
    inlines = [FreightInline]
    actions = ['calculate_freight']

    def api_calculate_freight(self, data):
        url = "https://sandbox.melhorenvio.com.br/api/v2/me/shipment/calculate"
        token = os.getenv("TOKEN")
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "Aplicação gui.schulz@gmail.com"
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response

    def calculate_freight(self, request, queryset):
        order = Order.objects.get(pk=queryset.values()[0]['id'])
        data = {
            "from": {"postal_code": queryset.values()[0]['zip_from']},
            "to": {"postal_code": queryset.values()[0]['zip_to']},
            "products": [
                {
                    "id": queryset.values()[0]['number'],
                    "width": queryset.values()[0]['width'],
                    "height": queryset.values()[0]['height'],
                    "length": queryset.values()[0]['length'],
                    "weight": queryset.values()[0]['weight'],
                    "insurance_value": 100.0,
                    "quantity": queryset.values()[0]['amount']
                }
            ],
            "options": {
                "receipt": True,
                "own_hand": False
            }
        }
        response = self.api_calculate_freight(data)
        if response.status_code == 200:
            response_data = response.json()
            for item in response_data:
                if "error" not in item:
                    freight_data = {
                        "order": order,
                        "carrier": f"{item['company']['name']} - {item['name']}",
                        "delivery_time": item['delivery_time'],
                        "delivery_cost": item['price'],
                        "external_freight_id": item['company']['id']
                    }
                    freight = Freight.objects.create(**freight_data)


admin.site.register(Order, AdminModel)
