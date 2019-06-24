from rest_framework.serializers import ModelSerializer

from orderitems.models import OrderItems


class OrdersItemsSerializer(ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ('id','menuId', 'quantity')
