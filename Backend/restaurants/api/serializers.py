from rest_framework.serializers import ModelSerializer

from restaurants.models import Restaurants


class RestaurantsSerializer(ModelSerializer):
    class Meta:
        model = Restaurants
        fields = (
            'id', 'name', 'category', 'deliveryEstimate', 'rating', 'imagePath', 'about', 'hours')
