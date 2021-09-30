from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=1024)

class Menu(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu')
    item_name = models.CharField(max_length=100, null=True)

class MenuLikes(models.Model):
    likeusers = models.ManyToManyField(User)
    likemenu = models.ForeignKey(Menu,on_delete=models.CASCADE,null=True,related_name='likemenu')
