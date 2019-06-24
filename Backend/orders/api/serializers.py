from rest_framework.serializers import ModelSerializer

from orderitems.models import OrderItems
from orders.models import Orders
from orderitems.api.serializers import OrdersItemsSerializer


class OrdersSerializer(ModelSerializer):
    orderItems = OrdersItemsSerializer(many=True)

    class Meta:
        model = Orders
        fields = (
            'id', 'address', 'email', 'emailConfirmation', 'name', 'optionalAddress', 'number', 'paymentOption',
            'orderItems')

    def cria_orderitems(self, orderItems, order):
        for orderitems in orderItems:
            at = OrderItems.objects.create(**orderitems)
            order.orderItems.add(at)

    def create(self, validated_data):
        orderItems = validated_data['orderItems']
        del validated_data['orderItems']

        order = Orders.objects.create(**validated_data)
        self.cria_orderitems(orderItems, order)

        return order