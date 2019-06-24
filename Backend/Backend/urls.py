"""Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from menu.api.viewsets import MenuViewSet
from orderitems.api.viewsets import OrderItemsViewSet
from orders.api.viewsets import OrdersViewSet
from restaurants.api.viewsets import RestaurantsViewSet
from reviews.api.viewsets import ReviewsViewSet
from user.api.viewsets import LoginUserAPI, CreateUserAPI

router = routers.DefaultRouter()
router.register(r'restaurants', RestaurantsViewSet, base_name='Restaurants')
router.register(r'reviews', ReviewsViewSet, base_name='Reviews')
router.register(r'menu', MenuViewSet, base_name='Menu')
router.register(r'orders', OrdersViewSet, base_name='Orders')
router.register(r'orderitems', OrderItemsViewSet, base_name='OrderItems')



urlpatterns = [
    path('', include(router.urls)),
    path('api/1.0/login_user/', LoginUserAPI.as_view(), name='api_login_user'),
    path('api/1.0/create_user/', CreateUserAPI.as_view({'post': 'post'}), name='api_create_user'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



"""
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"""
