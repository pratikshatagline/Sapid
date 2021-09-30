from django.db.models import query
from django.shortcuts import get_object_or_404, render
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, RestaurantSerializer,MenuSerializer, MenuLikeSerializer, FavouriteSerializer
from django.contrib.auth import login
from rest_framework import permissions, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.views import APIView
from .models import Menu, Restaurant, MenuLikes
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
    queryset = Restaurant.objects.select_related()
    serializer_class = RestaurantSerializer

class SearchAPI(APIView):
    def get(self, request):
        location = request.GET.get("location")
        queryset = Restaurant.objects.filter(location__icontains=location)
        serializer = RestaurantSerializer(queryset, many=True)
        return Response(serializer.data)

class MenuAPI(APIView):

    def post(self, request):
        serializer = MenuSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
        
    def get(self, request):
        tasks = Menu.objects.all()
        serializer = MenuSerializer(tasks, many=True)
        return Response(serializer.data)

class LikedAPI(APIView):

    def get(self, request):
        post = MenuLikes.objects.all()
        serializer = MenuLikeSerializer(post,many=True)
        return Response(serializer.data)

    def post(self,request):
        id = request.GET.get("id")
        likeusers = request.user
        likemenu = Menu.objects.filter(id=id)
        serializer = MenuLikeSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save(likeusers,likemenu)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class FavouriteAPI(APIView):
    bad_request_message = 'An error has occurred'

    def post(self,request):
        menu = get_object_or_404(Menu,id=request.data.get('id'))
        user = request.user
        serializer = FavouriteSerializer(menu,many=True)
        if user not in menu.favourite.all():
            menu.favourite.add(user)
            return Response({'detail': 'User added to item'}, status=status.HTTP_200_OK)
        return Response({'detail': self.bad_request_message}, status=status.HTTP_400_BAD_REQUEST)


        #return Response("Added to favourite")

class FavouriteListAPI(APIView):

    def get(self,request):
        user = request.user
        print(user)
        favourite_list = Menu.objects.filter(favourite=user)
        serializer = FavouriteSerializer(favourite_list,many=True)

        return Response(serializer.data)
