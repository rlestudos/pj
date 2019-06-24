import django_filters
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from restaurants.models import Restaurants
from .serializers import RestaurantsSerializer


class RestaurantsViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    """
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    """
    serializer_class = RestaurantsSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('id', 'name', 'category')

    def get_queryset(self):

        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        category = self.request.query_params.get('category', None)

        queryset = Restaurants.objects.all()

        if id:
            queryset = Restaurants.objects.filter(pk=id)

        if name:
            queryset = Restaurants.objects.filter(name=name)

        if category:
            queryset = Restaurants.objects.filter(category=category)

        return queryset.order_by('-id')
