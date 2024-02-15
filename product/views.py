from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Product
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.pagination import PageNumberPagination
# Create your views here.
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    pagination_class = StandardResultsSetPagination
    parser_classes = [(MultiPartParser)]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()