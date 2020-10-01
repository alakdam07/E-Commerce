from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *


@api_view(['GET'])
def apiOverview(request):
    api_urls ={
        'List': '/customer-list/',
        'Detail View': '/customer-detail/<str:pk>/',
        'Create':'/customer-create/',
        'Update': '/customer-update/<str:pk>/',
        'Delete': '/customer-delete/<str:pk>/',
        'Order List': '/order-list/'
    }
    return Response(api_urls)


@api_view(['GET'])
def orderList(request):
	orders = Order.objects.all()
	serializer = OrderSerializer(orders, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def orderCreate(request):
	serializer = OrderSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['GET'])
def customerList(request):
	customers = Customer.objects.all()
	serializer = CustomerSerializer(customers, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def customerDetail(request, pk):
	customers = Customer.objects.get(id=pk)


	serializer = CustomerSerializer(customers, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def customerCreate(request):
	serializer = CustomerSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def customerUpdate(request, pk):
	customer = Customer.objects.get(id=pk)
	serializer = CustomerSerializer(instance=customer, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def customerDelete(request, pk):
	customer = Customer.objects.get(id=pk)
	customer.delete()

	return Response("Item deleted")



"""Order"""
""" @api_view(['GET'])
def orderApiOverview(request):
    api_urls ={
        'List': '/order-list/',
        'Detail View': '/customer-detail/<str:pk>/',
        'Create':'/customer-create/',
        'Update': '/customer-update/<str:pk>/',
        'Delete': '/customer-delete/<str:pk>/'
    }
    return Response(api_urls)


@api_view(['GET'])
def customerList(request):
	customers = Customer.objects.all()
	serializer = CustomerSerializer(customers, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def customerDetail(request, pk):
	customers = Customer.objects.get(id=pk)
	serializer = CustomerSerializer(customers, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def customerCreate(request):
	serializer = CustomerSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def customerUpdate(request, pk):
	customer = Customer.objects.get(id=pk)
	serializer = CustomerSerializer(instance=customer, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)



@api_view(['DELETE'])
def customerDelete(request, pk):
	customer = Customer.objects.get(id=pk)
	customer.delete()

	return Response("Item deleted")
 """
