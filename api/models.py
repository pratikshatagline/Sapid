from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=1024)
    item_name = models.CharField(max_length=100, null=True)
    like = models.BooleanField(default=False, null=True)
