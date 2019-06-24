import django_filters
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from menu.models import Menu
from .serializers import MenuSerializer


class MenuViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    """
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    """
    serializer_class = MenuSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('id', 'restaurantId')

    def get_queryset(self):

        id = self.request.query_params.get('id', None)
        restaurantId = self.request.query_params.get('restaurantId', None)

        queryset = Menu.objects.all()

        if id:
            queryset = Menu.objects.filter(pk=id)

        if restaurantId:
            queryset = Menu.objects.filter(restaurantId=restaurantId)

        return queryset.order_by('-id')
