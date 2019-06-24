from django.db import models


class Restaurants(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    deliveryEstimate = models.CharField(max_length=150)
    rating = models.DecimalField(max_digits=10, decimal_places=2)
    imagePath = models.ImageField(upload_to='fotos_restaurantes', null=True)
    about = models.CharField(max_length=150)
    hours = models.CharField(max_length=150)

    def __str__(self):
        return self.name
