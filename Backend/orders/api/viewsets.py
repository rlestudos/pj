import django_filters
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from orders.models import Orders
from .serializers import OrdersSerializer


class OrdersViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    """
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    """
    serializer_class = OrdersSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('id', 'address', 'optionalAddress', 'number', 'paymentOption')

    def get_queryset(self):
        id = self.request.query_params.get('id', None)

        queryset = Orders.objects.all()

        if id:
            queryset = Orders.objects.filter(pk=id)

        return queryset.order_by('-id')
