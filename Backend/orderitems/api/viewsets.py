import django_filters
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from orderitems.models import OrderItems
from .serializers import OrdersItemsSerializer


class OrderItemsViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    """
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    """
    serializer_class = OrdersItemsSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('id','menuId','quantity')

    def get_queryset(self):
        id = self.request.query_params.get('id', None)

        queryset = OrderItems.objects.all()

        if id:
            queryset = OrderItems.objects.filter(pk=id)

        return queryset.order_by('-id')
