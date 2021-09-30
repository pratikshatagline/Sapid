from django.urls import path
from .views import RegisterAPI, LoginAPI, RestaurantAPI, RestaurantListAPI, SearchAPI, MenuAPI, LikedAPI, FavouriteAPI, FavouriteListAPI
urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/restaurant/', RestaurantAPI.as_view(), name='restaurant'),
    path('api/restaurantlist/', RestaurantListAPI.as_view(), name='restaurants'),
    path('api/search/', SearchAPI.as_view(), name='search'),
    path('api/menu/', MenuAPI.as_view(), name='menu'),
    path('api/menu/like', LikedAPI.as_view(), name='like'),
    path('api/favourite/', FavouriteAPI.as_view(), name='favourite'),
    path('api/favouritelist/', FavouriteListAPI.as_view(), name='favouritelist'),
]