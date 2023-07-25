from django.db import models
import uuid
from order.models import Order


class Freight(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    carrier = models.CharField(max_length=100)
    delivery_time = models.IntegerField()
    delivery_cost = models.CharField(max_length=100)
    external_freight_id = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name="freight",
                              related_query_name="freight",)

    def __str__(self):
        return f"{self.carrier} - {self.external_freight_id} - {self.delivery_time} - {self.delivery_cost} - {self.order}"
