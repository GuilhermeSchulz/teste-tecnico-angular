from django.test import TestCase
from .models import Order


class OrderTest(TestCase):
    def setUp(self):
        self.order_data = {
            "number": 1,
            "amount": 2.0,
            "weight": 2.5,
            "width": 10.0,
            "height": 5.0,
            "length": 15.0,
            "zip_from": "92310200",
            "zip_to": "92870000",
        }
        self.order = Order.objects.create(**self.order_data)

    def test_order_creation(self):
        self.assertEqual(Order.objects.count(), 1)

    def test_order_str_representation(self):
        expected_str = f"{self.order.id} - {self.order.number} - {self.order.amount} - {self.order.weight} - {self.order.width} - {self.order.height} - {self.order.length} - {self.order.zip_from} - {self.order.zip_to}"
        self.assertEqual(str(self.order), expected_str)

    def test_order_fields(self):
        self.assertEqual(self.order.number, self.order_data["number"])
        self.assertEqual(self.order.amount, self.order_data["amount"])
        self.assertEqual(self.order.weight, self.order_data["weight"])
        self.assertEqual(self.order.width, self.order_data["width"])
        self.assertEqual(self.order.height, self.order_data["height"])
        self.assertEqual(self.order.length, self.order_data["length"])
        self.assertEqual(self.order.zip_from, self.order_data["zip_from"])
        self.assertEqual(self.order.zip_to, self.order_data["zip_to"])
