from django.db import models
from django.utils import timezone

class Assortment(models.Model):
 Editor = models.ForeignKey('auth.User',on_delete=models.CASCADE)
 Category = models.CharField(max_length=200)
 Type = models.CharField(max_length=200)
 Composition = models.CharField(max_length=200)
 Price = models.IntegerField()
 created_date = models.DateTimeField(default=timezone.now)
 

class Order(models.Model):
    Name = models.CharField(max_length=200)
    Goods = models.CharField(max_length=200)
    Quantity = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    
  
