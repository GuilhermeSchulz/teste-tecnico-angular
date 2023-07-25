from django.db import models
import uuid


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField()
    amount = models.FloatField()
    weight = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    length = models.FloatField()
    zip_from = models.CharField(max_length=8)
    zip_to = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.id} - {self.number} - {self.amount} - {self.weight} - {self.width} - {self.height} - {self.length} - {self.zip_from} - {self.zip_to}"
