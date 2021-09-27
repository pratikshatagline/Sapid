from django.contrib import admin
from .models import Restaurant
from django.db.models import Sum
from django.contrib.auth.models import User
from django.shortcuts import render

# Register your models here.
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location', 'item_name', 'like']

class MyModelAdmin(admin.ModelAdmin):
    def get_total(self,request):
        #functions to calculate users...
        context={'usercount':User.objects.all().count()}
        return render(request,context)