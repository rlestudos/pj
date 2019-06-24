from django.db import models

from orderitems.models import OrderItems


class Orders(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    email = models.CharField(max_length=500, null=True, blank=True)
    emailConfirmation = models.CharField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    optionalAddress = models.CharField(max_length=500, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    paymentOption = models.CharField(max_length=500, null=True, blank=True)
    orderItems = models.ManyToManyField(OrderItems)


    def __str__(self):
        return self.email
