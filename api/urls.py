from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview" ),
    path('customer-list/', views.customerList, name="customer-list" ),
    path('customer-detail/<str:pk>/', views.customerDetail, name="single-customer"),
    path('customer-create/', views.customerCreate, name="customer-create"),
    path('customer-update/<str:pk>/', views.customerUpdate, name="customer-update"),
    path('customer-delete/<str:pk>/', views.customerDelete, name="customer-delete"),
    path('order-list/', views.orderList, name="order-list" ),
     path('create-order/', views.orderCreate, name="order-create"),

]
