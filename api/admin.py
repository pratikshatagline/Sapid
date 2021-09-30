from django.contrib import admin
from .models import Restaurant, Menu, MenuLikes
from django.db.models import Sum
from django.contrib.auth.models import User
from django.shortcuts import render

# Register your models here.
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location']


admin.site.register(Menu)
admin.site.register(MenuLikes)

class MyModelAdmin(admin.ModelAdmin):
    def get_total(self):
        #functions to calculate users...
        context={'usercount':User.objects.all().count()}
        return render(context)