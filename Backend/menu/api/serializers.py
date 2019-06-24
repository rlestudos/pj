from rest_framework.serializers import ModelSerializer

from menu.models import Menu


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = (
            'id', 'imagePath', 'name', 'description', 'price', 'restaurantId')
