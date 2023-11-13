from django.db import models


class rakesh(models.Model):
    name = models.CharField(max_length=255, default='Default Name')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    quantity = models.PositiveIntegerField(default=0)


class bapon(models.Model):
    name = models.CharField(max_length=255, default='Default Name')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    quantity = models.PositiveIntegerField(default=0)