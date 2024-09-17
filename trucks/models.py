from django.db import models

class Truck(models.Model):
    code = models.CharField(max_length=10)
    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    capacity = models.FloatField()

    def __str__(self):
        return f"{self.brand} - {self.model} - {self.code}"
