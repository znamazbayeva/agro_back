from django.shortcuts import render
from .serializers import OrderSerializer
from .models import Order
from rest_framework import viewsets

class OrderViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()