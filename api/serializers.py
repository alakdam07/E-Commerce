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
        fields = ['name','id', 'tags']



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'id', 'email', 'phone']


class CustomerWithProductsSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    def get_products(self, customer):
        # the customer is passed in to this method
        # we want to get all of the products for that customer, but there's
        # no way to query for that, since the customer model is not connected
        # to the product model
        # - so we need to go through the order model, like so
        #   customer => all orders => all products within those orders

        # 1. get all of the customers orders
        orders_query = Order.objects.filter(customer=customer)

        # 2. get all of the products that are part of those orders
        products = Product.objects.filter(orders__in=orders_query)

        # Q() F()

        # 3. return the products
        return ProductSerializer(products, many=True).data

    class Meta:
        model = Customer
        fields = ['name', 'id', 'email', 'phone', 'products']


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    product = ProductSerializer()
    class Meta:
        model = Order
        fields = ['status', 'customer', 'product']

