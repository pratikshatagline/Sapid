from django.urls import path
from .views import RegisterAPI, LoginAPI, RestaurantAPI, RestaurantListAPI, SearchAPI

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/restaurant/', RestaurantAPI.as_view(), name='restaurant'),
    path('api/restaurantlist/', RestaurantListAPI.as_view(), name='restaurants'),
    path('api/search/', SearchAPI.as_view(), name='search'),
]