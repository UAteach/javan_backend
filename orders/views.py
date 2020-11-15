from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

from .models import Order, OrderContent
from .serializers import OrderSerializer, OrderContentSerializer


## Order
class ListOrder(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['bin_number', 'master_teacher', 'members']


class Order(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


## OrderContent
class ListOrderContent(generics.ListCreateAPIView):
    queryset = OrderContent.objects.all()
    serializer_class = OrderContentSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order']


class OrderContent(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderContent.objects.all()
    serializer_class = OrderContentSerializer
