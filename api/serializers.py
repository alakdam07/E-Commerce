from rest_framework import serializers
from .models import *

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]

class ProductSerializer(serializers.ModelSerializer):
    tags =  TagSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    products: ProductSerializer(many=True)
    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    product = ProductSerializer()
    class Meta:
        model = Order
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    products: ProductSerializer(many=True)
    orders: OrderSerializer(many=True)
    class Meta:
        model = Customer
        fields = ['id','name','email', 'phone']
