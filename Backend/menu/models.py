from django.db import models

class Menu(models.Model):
    imagePath = models.ImageField(upload_to='fotos_menu', null=True)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    restaurantId = models.IntegerField(null=True)

    def __str__(self):
        return self.description
