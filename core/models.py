from django.db import models

from core import Currencies


class Item(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.CharField(max_length=3, choices=Currencies.CHOICE, default='usd')

    def __str__(self):
        return f'{self.name}|{self.price}'
