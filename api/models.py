# ##################
# ##### MODELS #####
# ##################
from __future__ import unicode_literals

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200, null= True)
    email =  models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)
    date_created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name= models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY=(
         ('Indoor', 'Indoor'),
         ('Outdoor', 'Outdoor'),

            )

    name= models.CharField(max_length=200, null=True)
    price= models.FloatField(null=True)
    category=models.CharField(max_length=200,null=True, choices=CATEGORY)
    description= models.CharField(max_length=200,null=True, blank= True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    tags= models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS =(
         ('Pending', 'Pending'),
         ('Out of delivery', 'Out of delivery'),
         ('Delivered', 'Delivered'),
    )
    status= models.CharField(max_length=200, null=True,choices= STATUS)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    customer = models.ForeignKey(Customer, null= True, on_delete= models.SET_NULL, related_name='orders')
    product = models.ForeignKey(Product, null= True, on_delete= models.SET_NULL, related_name='orders')
