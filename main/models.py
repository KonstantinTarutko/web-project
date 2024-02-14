from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=128, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    number = models.DecimalField(max_digits=11, decimal_places=0, null=False)
    message = models.TextField(null=True, blank=True)
