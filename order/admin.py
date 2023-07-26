from django.contrib import admin
from .models import Order
import requests
import json
from freight.models import Freight
from django.shortcuts import render


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
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjI5YTY1YWUyNjEzMjkyOGM2MjFhNDNiYmUzZDI1NjQ1MGJjMzk2YWE0NTBlYTYzYTIzMmYzOTRlOTYzZjkzY2FiY2RjMWVhNmVjYjNlOTE3In0.eyJhdWQiOiI5NTYiLCJqdGkiOiIyOWE2NWFlMjYxMzI5MjhjNjIxYTQzYmJlM2QyNTY0NTBiYzM5NmFhNDUwZWE2M2EyMzJmMzk0ZTk2M2Y5M2NhYmNkYzFlYTZlY2IzZTkxNyIsImlhdCI6MTY5MDMxNjU0OSwibmJmIjoxNjkwMzE2NTQ5LCJleHAiOjE3MjE5Mzg5NDksInN1YiI6IjFlZjMzOTNkLTBkNWMtNDc4ZC1iMDEyLTQ1M2U0OWVlN2IwOSIsInNjb3BlcyI6WyJzaGlwcGluZy1jYWxjdWxhdGUiXX0.t2Ei-Gg9mIrhMMXPzeTdW-KlY7RNv8FvJtsE0ABh6RaJRvIIuvl64o7A_RDuGRTWsVtKJeieEocEzvR_XsrsEJsAjC0rmPHBETjw9Jyva72G9dMjEceX-T6_Q-7O8oH8Cpsk6l4SMWcwWHesQQYjG7mq9L80DGWGq2JPMdTAx-Xp_JpT4OhaD7WxTj2EKOA-WMiBXpLboHu1eo-BJ-fR91nJOIucFiNZZiOK3hGJf8nqzEznvD8j9nCMF2wCqkhdZ3WnXO9BuAl6UX3tnbk3Gu1Mq_EDJZferppKSrkCTh-LBUPWIuKQBd11cW0TFN2KOUsMVBaCQD3LDzx6_P5MFmsk57LNSki1NPuEd615S3t01N1dD-oapyvzBfSu0OKe9PtzdxGXj9F137QgPXqPbHpgtKZD-QnKdvAlA0Rowh0QpylwOVzAi9nAXiL0MUqTpkhBUuiRfWftWHS4FQqHYIoOHGqWavQ4tQ_ix5OBB60_Dd_qWzSdE3hOEErKP6mZUmuPEkQhJ8VMeLV-kZe2QN-5Xs6cQGs1wgayHIXb_Nd_NM5I4J6wIqFUl3DqkQAJEAG-Pjkdzwfv3hSCAgZ4_boZ99vLKGEdc6XZG1aZ2EYO0tdZQzCjuEIrKM8_RbVNikzBVp96yQhJh9u2rBKyLGEOhBLPyWzyQ8tQ95Q1R3Q"
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
