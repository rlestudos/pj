from django.db import models


class OrderItems(models.Model):
    menuId = models.CharField(max_length=500, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.id