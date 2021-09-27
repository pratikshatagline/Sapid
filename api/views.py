from django.db.models import query
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, RestaurantSerializer
from django.contrib.auth import login
from rest_framework import permissions, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.views import APIView
from .models import Restaurant
from rest_framework import filters
from django.contrib.auth.models import User

# Create your views here.

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

class RestaurantAPI(APIView):

    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

class RestaurantListAPI(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class SearchAPI(APIView):
    def get(self, request):
        location = request.GET.get("location")
        queryset = Restaurant.objects.filter(location=location)
        response = []
        if queryset:
            fields = [
                    "name",
                    "location",
                    "item_name",
                    "like",
                ]
            for obj in (queryset):
                data_dict = dict()
                for field in fields:
                    data_dict[field] = getattr(obj, field, None)
                response.append(data_dict)
        return Response(response)