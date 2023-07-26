from django.test import TestCase
from .models import Freight
from order.models import Order


class FreightTest(TestCase):
    def setUp(self):
        self.order_data = {
            "number": 123,
            "amount": 100.0,
            "weight": 2.5,
            "width": 10.0,
            "height": 5.0,
            "length": 15.0,
            "zip_from": "92310200",
            "zip_to": "92870000",
        }
        self.order = Order.objects.create(**self.order_data)

        self.freight_data = {
            "carrier": "Correios Sedex",
            "delivery_time": 3,
            "delivery_cost": "100.00",
            "external_freight_id": 1,
            "order": self.order,
        }
        self.freight = Freight.objects.create(**self.freight_data)

    def test_freight_creation(self):
        self.assertEqual(Freight.objects.count(), 1)

    def test_freight_str_representation(self):
        expected_str = f"{self.freight.carrier} - {self.freight.external_freight_id} - {self.freight.delivery_time} - {self.freight.delivery_cost} - {self.freight.order}"
        self.assertEqual(str(self.freight), expected_str)

    def test_freight_fields(self):
        self.assertEqual(self.freight.carrier, self.freight_data["carrier"])
        self.assertEqual(self.freight.delivery_time,
                         self.freight_data["delivery_time"])
        self.assertEqual(self.freight.delivery_cost,
                         self.freight_data["delivery_cost"])
        self.assertEqual(self.freight.external_freight_id,
                         self.freight_data["external_freight_id"])
        self.assertEqual(self.freight.order, self.order)

    # Adicione mais testes, se necessário
