from django.db.models import fields
from api.models import Menu, Restaurant, MenuLikes
from rest_framework import serializers
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

# Restaurant Serializer
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'item_name')

class RestaurantSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(many=True,read_only=True)
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'location', 'menu')

class MenuLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuLikes
        fields = '__all__'

class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'item_name', 'favourite')