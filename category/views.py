from django.shortcuts import render
from .serializers import SubcategorySerializer, CategorySerializer
from .models import Subcategory, Category
from rest_framework import viewsets
# from rest_framework.parsers import MultiPartParser
# from rest_framework.pagination import PageNumberPagination
# Create your views here.
# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 1000

class SubcategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = SubcategorySerializer
    queryset = Subcategory.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

