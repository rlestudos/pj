from django.db import models


class Reviews(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateTimeField()
    rating = models.DecimalField(max_digits=10, decimal_places=2)
    comments = models.CharField(max_length=500)
    restaurantId = models.IntegerField(null=True)

    def __str__(self):
        return self.name
